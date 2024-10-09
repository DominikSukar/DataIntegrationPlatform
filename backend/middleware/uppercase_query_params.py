from starlette.requests import Request


class UpperCaseServerParamMiddleware:
    def __init__(
        self,
        some_attribute: str,
    ):
        self.some_attribute = some_attribute

    async def __call__(self, request: Request, call_next):
        path = request.scope["path"]
        fragmented_path = path.strip("/").split("/")

        # This middleware is supposed to detect servername in path, so don't capitalize URLs with path consisting of one variable
        if (
            "datadragon" not in fragmented_path
            and "docs" not in fragmented_path
            and "openapi.json" not in fragmented_path
            and "servers" not in fragmented_path
            and "items" not in fragmented_path
            and "champions" not in fragmented_path
            and "summoner_spells" not in fragmented_path
            and "perks" not in fragmented_path
            and "database" not in fragmented_path
            and "seasons" not in fragmented_path
        ):
            fragmented_path[1] = fragmented_path[1].upper()
            whole_path = "/".join(fragmented_path)
            request.scope["path"] = f"/{whole_path}/"

        response = await call_next(request)

        return response
