from pathlib import Path
from backend.app import create_backend_app
from starlette.staticfiles import StaticFiles
from backend.redirector import redirector

def create_app():
    app = create_backend_app()
    add_redirector_app(app)
    add_frontend_app(app)
    return app

def add_frontend_app(app):
    # Add a route for serving static files
    static_dir = Path(__file__).parent / 'frontend' / 'dist'
    app.add_url_rule(
        '/{path:path}', 
        endpoint='frontend', 
        view_func=StaticFiles(directory=static_dir, html=True)
    )

def add_redirector_app(app):
    # Add a route for handling URL redirection for bot access
    app.add_url_rule(
        '/r/{url_key:str}', 
        endpoint='redirector',
        view_func=redirector
    )
