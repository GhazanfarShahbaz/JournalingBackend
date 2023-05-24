from typing import List
from app.models import Location

class LocationRepository:
    async def get_all_locations(self) -> List[Location]:
        """
        Retrieve all locations from the database.
        """
        return await Location.all()

    async def get_location_by_id(self, location_id: int) -> Location:
        """
        Retrieve a single location by ID from the database.

        Args:
            location_id: The ID of the location to retrieve.

        Returns:
            The `Location` object with the specified ID, if it exists.
        """
        return await Location.get(id=location_id)

    async def create_location(self, location_data: dict) -> Location:
        """
        Create a new location with the given data.

        Args:
            location_data: A dictionary containing the data for the new location.

        Returns:
            The newly created `Location` object.
        """
        return await Location.create(**location_data)

    async def update_location(self, location_id: int, location_data: dict) -> None:
        """
        Update a location with the given ID using the provided data.

        Args:
            location_id: The ID of the location to update.
            location_data: A dictionary containing the updated data for the location.

        Returns:
            None
        """
        location = await Location.get(id=location_id)
        await location.update_from_dict(location_data)
        await location.save()

    async def delete_location(self, location_id: int) -> None:
        """
        Delete a location with the given ID from the database.

        Args:
            location_id: The ID of the location to delete.

        Returns:
            None
        """
        location = await Location.get(id=location_id)
        await location.delete()