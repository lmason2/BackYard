from Handlers.RouteHandlers.base_route_handler import BaseRouteHandler
from Handlers.RouteHandlers.get_all_jobs_handler import GetAllJobsRouteHandler
from Handlers.RouteHandlers.get_all_users_handler import GetAllUsersRouteHandler
from Handlers.RouteHandlers.get_roles_for_user import GetRolesForUser
from Handlers.RouteHandlers.create_user_handler import CreateUserRouteHandler
from Handlers.RouteHandlers.get_job_by_user_id_handler import GetJobByUserIdRouteHandler

ROUTE_MAP = {
    'get-all-jobs': GetAllJobsRouteHandler,
    'get-all-users': GetAllUsersRouteHandler,
    'get-roles-for-user': GetRolesForUser,
    'create-user': CreateUserRouteHandler,
    'get-job-by-user-id': GetJobByUserIdRouteHandler
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
    