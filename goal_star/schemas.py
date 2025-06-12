from ninja import ModelSchema

from .models import Goal


class GoalListSchema(ModelSchema):
    class Meta:
        model = Goal
        fields = "__all__"


class GoalObjectSchema(ModelSchema):
    class Meta:
        model = Goal
        fields = "__all__"
