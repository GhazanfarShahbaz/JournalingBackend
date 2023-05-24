from typing import List
from app.models import Goal

class GoalRepository:
    async def get_all_goals(self) -> List[Goal]:
        """
        Retrieve all goals from the database.
        """
        return await Goal.all()

    async def get_goal_by_id(self, goal_id: int) -> Goal:
        """
        Retrieve a single goal by ID from the database.

        Args:
            goal_id: The ID of the goal to retrieve.

        Returns:
            The `Goal` object with the specified ID, if it exists.
        """
        return await Goal.get(id=goal_id)

    async def create_goal(self, goal_data: dict) -> Goal:
        """
        Create a new goal with the given data.

        Args:
            goal_data: A dictionary containing the data for the new goal.

        Returns:
            The newly created `Goal` object.
        """
        return await Goal.create(**goal_data)

    async def update_goal(self, goal_id: int, goal_data: dict) -> None:
        """
        Update a goal with the given ID using the provided data.

        Args:
            goal_id: The ID of the goal to update.
            goal_data: A dictionary containing the updated data for the goal.

        Returns:
            None
        """
        goal = await Goal.get(id=goal_id)
        await goal.update_from_dict(goal_data)
        await goal.save()

    async def delete_goal(self, goal_id: int) -> None:
        """
        Delete a goal with the given ID from the database.

        Args:
            goal_id: The ID of the goal to delete.

        Returns:
            None
        """
        goal = await Goal.get(id=goal_id)
        await goal.delete()