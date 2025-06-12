from ninja import NinjaAPI

api = NinjaAPI()
api.add_router("user", "user.views.router")
api.add_router("goal_star", "goal_star.views.router")
