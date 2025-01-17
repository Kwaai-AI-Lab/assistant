from starlette.responses import JSONResponse, Response
from backend.managers.PersonasManager import PersonasManager
from common.paths import api_base_url
from backend.pagination import parse_pagination_params
from backend.schemas import PersonaCreateSchema


class PersonasView:
    def __init__(self):
        self.pm = PersonasManager()

    async def get(self, id: str):
        persona = await self.pm.retrieve_persona(id)
        if persona is None:
            return JSONResponse({"error": "Persona not found"}, status_code=404)
        return JSONResponse(persona.dict(), status_code=200)

    async def post(self, body: PersonaCreateSchema):
        valid_msg = await self.pm.validate_persona_data(body)
        if valid_msg == None:
            voice_id = await self.pm.create_persona(body)
            persona = await self.pm.retrieve_persona(voice_id)
            return JSONResponse(persona.dict(), status_code=201, headers={'Location': f'{api_base_url}/personas/{persona.id}'})
        return JSONResponse({"error": " Invalid persona: " + valid_msg}, status_code=400)

    async def put(self, id: str, body: PersonaCreateSchema):
        await self.pm.update_persona(id, body)
        persona = await self.pm.retrieve_persona(id)
        if persona is None:
            return JSONResponse({"error": "Persona not found"}, status_code=404)
        return JSONResponse(persona.dict(), status_code=200)

    async def delete(self, id: str):
        success, error_message = await self.pm.delete_persona(id)
        if not success and not error_message:
            return JSONResponse({"error": "Persona not found"}, status_code=404)
        elif not success and error_message:
            return JSONResponse({"error": error_message}, status_code=400)
        return Response(status_code=204)

    async def search(self, filter: str = None, range: str = None, sort: str = None):
        result = parse_pagination_params(filter, range, sort)
        if isinstance(result, JSONResponse):
            return result

        offset, limit, sort_by, sort_order, filters = result

        personas, total_count = await self.pm.retrieve_personas(
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            sort_order=sort_order,
            filters=filters
        )
        headers = {
            'X-Total-Count': str(total_count),
            'Content-Range': f'personas {offset}-{offset + len(personas) - 1}/{total_count}'
        }
        return JSONResponse([persona.dict() for persona in personas], status_code=200, headers=headers)