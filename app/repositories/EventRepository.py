from typing import List
from tortoise.queryset import QuerySet
from app.models import Event

class EventRepository:
    async def get_all_events(self) -> List[Event]:
        """
        Retrieve all events from the database.
        """
        return await Event.all()

    async def get_event_by_id(self, event_id: int) -> Event:
        """
        Retrieve an event by ID from the database.

        Args:
            event_id: The ID of the event to retrieve.

        Returns:
            The `Event` object with the specified ID, if it exists.
        """
        return await Event.get(id=event_id)

    async def create_event(self, event_data: dict) -> Event:
        """
        Create a new event with the given data.

        Args:
            event_data: A dictionary containing the data for the new event.

        Returns:
            The newly created `Event` object.
        """
        return await Event.create(**event_data)

    async def update_event(self, event_id: int, event_data: dict) -> None:
        """
        Update an event with the given ID using the provided data.

        Args:
            event_id: The ID of the event to update.
            event_data: A dictionary containing the updated data for the event.

        Returns:
            None
        """
        event = await Event.get(id=event_id)
        await event.update_from_dict(event_data)
        await event.save()

    async def delete_event(self, event_id: int) -> None:
        """
        Delete an event with the given ID from the database.

        Args:
            event_id: The ID of the event to delete.

        Returns:
            None
        """
        event = await Event.get(id=event_id)
        await event.delete()