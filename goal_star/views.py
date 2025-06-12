from django.contrib.auth import get_user_model
from ninja import Router

from user.authentication import AuthBearer
from utils.schemas import ErrorSchema, ListSchema, ObjectSchema

from .models import Goal
from .schemas import GoalListSchema, GoalObjectSchema

User = get_user_model()

router = Router(tags=["goal_star"], auth=AuthBearer())


@router.get(
    "/goals",
    response={200: ListSchema[GoalListSchema]},
)
def list_goals(request):
    goals = Goal.objects.filter(user=request.auth)
    return {"items": goals}


@router.get(
    "/goals/{goal_id}",
    response={200: ObjectSchema[GoalObjectSchema], 404: ErrorSchema},
)
def retrieve_goal(request, goal_id: int):
    try:
        goal = Goal.objects.get(user=request.auth, id=goal_id)
        return {"item": goal}
    except Goal.DoesNotExist:
        return 404, {"detail": "Goal not found"}
