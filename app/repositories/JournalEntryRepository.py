from typing import List
from tortoise.query_utils import Q
from app.models import JournalEntry


class JournalEntryRepository:
    async def get_all_entries(self) -> List[JournalEntry]:
        """
        Retrieve all journal entries from the database.

        Returns:
            A list of all `JournalEntry` objects in the database.
        """
        return await JournalEntry.all()

    async def get_entry_by_id(self, entry_id: int) -> JournalEntry:
        """
        Retrieve a single journal entry by ID from the database.

        Args:
            entry_id: The ID of the journal entry to retrieve.

        Returns:
            The `JournalEntry` object with the specified ID, if it exists.
        """
        return await JournalEntry.get(id=entry_id)

    async def create_entry(self, entry_data: dict) -> JournalEntry:
        """
        Create a new journal entry with the given data.

        Args:
            entry_data: A dictionary containing the data for the new journal entry.

        Returns:
            The newly created `JournalEntry` object.
        """
        return await JournalEntry.create(**entry_data)

    async def update_entry(self, entry_id: int, entry_data: dict) -> None:
        """
        Update a journal entry with the given ID using the provided data.

        Args:
            entry_id: The ID of the journal entry to update.
            entry_data: A dictionary containing the updated data for the journal entry.

        Returns:
            None
        """
        entry = await JournalEntry.get(id=entry_id)
        await entry.update_from_dict(entry_data)
        await entry.save()

    async def delete_entry(self, entry_id: int) -> None:
        """
        Delete a journal entry with the given ID from the database.

        Args:
            entry_id: The ID of the journal entry to delete.

        Returns:
            None
        """
        entry = await JournalEntry.get(id=entry_id)
        await entry.delete()