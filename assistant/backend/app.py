import os
from pathlib import Path
from connexion import AsyncApp
from connexion.resolver import MethodResolver
from connexion.middleware import MiddlewarePosition
from starlette.middleware.cors import CORSMiddleware
from backend.db import init_db
from common.utils import get_env_key

def create_backend_app():
    # Initialize the database
    init_db()

    apis_dir = Path(__file__).parent.parent / 'apis' / 'paios'
    connexion_app = AsyncApp(__name__, specification_dir=apis_dir)
    
    allow_origins = get_env_key(
        'PAIOS_ALLOW_ORIGINS',
        'http://localhost:5173,https://localhost:8443,https://localhost:3000'
    )
    
    allow_origins = [origin.strip() for origin in allow_origins.split(',')]

    # Add PAIOS server URL if environment variables are set
    paios_scheme = get_env_key('PAIOS_SCHEME', 'https')
    paios_host = get_env_key('PAIOS_HOST', 'localhost')
    paios_port = get_env_key('PAIOS_PORT', '8443')

    if paios_host:
        paios_url = f"{paios_scheme}://{paios_host}"
        if paios_port:
            paios_url += f":{paios_port}"
        allow_origins.append(paios_url)

    # Allow overriding origins from environment variables
    additional_origins = os.environ.get('PAIOS_ALLOW_ORIGINS')
    if additional_origins:
        allow_origins.extend(additional_origins.split(','))

    # Add CORS middleware
    connexion_app.add_middleware(
       CORSMiddleware,
       position=MiddlewarePosition.BEFORE_EXCEPTION,
       allow_origins=["https://localhost:3000","https://localhost:8443"],
       allow_credentials=True,
       allow_methods=["GET","POST","PUT","DELETE","PATCH","HEAD","OPTIONS"],
       allow_headers=["Authorization", "Content-Type", "Content-Range", "X-Total-Count"],
       expose_headers=["Content-Range", "X-Total-Count"],
    )

    # Add API with validation
    connexion_app.add_api(
        'openapi.yaml',
        resolver=MethodResolver('backend.api'),
        resolver_error=501,
        # TODO: Validation has a performance impact and may want to be disabled in production
        validate_responses=True,  # Validate responses against the OpenAPI spec
        strict_validation=True    # Validate requests strictly against the OpenAPI spec
    )
    return connexion_app