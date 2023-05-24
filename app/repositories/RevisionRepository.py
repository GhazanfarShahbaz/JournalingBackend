from typing import List
from app.models import Revision

class RevisionRepository:
    async def get_all_revisions(self) -> List[Revision]:
        """
        Retrieve all revisions from the database.
        """
        return await Revision.all()

    async def get_revision_by_id(self, revision_id: int) -> Revision:
        """
        Retrieve a single revision by ID from the database.

        Args:
            revision_id: The ID of the revision to retrieve.

        Returns:
            The `Revision` object with the specified ID, if it exists.
        """
        return await Revision.get(id=revision_id)

    async def create_revision(self, revision_data: dict) -> Revision:
        """
        Create a new revision with the given data.

        Args:
            revision_data: A dictionary containing the data for the new revision.

        Returns:
            The newly created `Revision` object.
        """
        return await Revision.create(**revision_data)

    async def update_revision(self, revision_id: int, revision_data: dict) -> None:
        """
        Update a revision with the given ID using the provided data.

        Args:
            revision_id: The ID of the revision to update.
            revision_data: A dictionary containing the updated data for the revision.

        Returns:
            None
        """
        revision = await Revision.get(id=revision_id)
        await revision.update_from_dict(revision_data)
        await revision.save()

    async def delete_revision(self, revision_id: int) -> None:
        """
        Delete a revision with the given ID from the database.

        Args:
            revision_id: The ID of the revision to delete.

        Returns:
            None
        """
        revision = await Revision.get(id=revision_id)
        await revision.delete()