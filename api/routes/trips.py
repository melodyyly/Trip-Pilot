from fastapi import APIRouter

from agents.planner_agent import (
    PlannerAgent
)

router = APIRouter()

planner = PlannerAgent()


@router.post("/trip-plan")
def plan_trip(request: dict):

    return planner.plan_trip(
        request
    )