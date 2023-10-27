from Handlers.RouteHandlers.get_job_handler import GetJobRouteHandler
from Handlers.RouteHandlers.base_route_handler import BaseRouteHandler

ROUTE_MAP = {
    'get-job': GetJobRouteHandler
}

class RouteHandler:
    def __init__(self, rows) -> None:
        self.results = rows

class RouteFactory:
    @staticmethod
    def get_handler(route_endpoint, request_body):
        route_handler = None
        try:
            if route_endpoint in ROUTE_MAP:
                route_handler = ROUTE_MAP.get(route_endpoint)(request_body)
            else:
                route_handler = BaseRouteHandler(request_body)
        except Exception as e:
            print(e)

        return route_handler