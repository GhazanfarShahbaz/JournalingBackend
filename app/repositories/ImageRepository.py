from typing import List
from app.models import Image

class ImageRepository:
    async def get_all_images(self) -> List[Image]:
        """
        Retrieve all images from the database.
        """
        return await Image.all()

    async def get_image_by_id(self, image_id: int) -> Image:
        """
        Retrieve an image by ID from the database.

        Args:
            image_id: The ID of the image to retrieve.

        Returns:
            The `Image` object with the specified ID, if it exists.
        """
        return await Image.get(id=image_id)

    async def create_image(self, image_data: dict) -> Image:
        """
        Create a new image with the given data.

        Args:
            image_data: A dictionary containing the data for the new image.

        Returns:
            The newly created `Image` object.
        """
        return await Image.create(**image_data)

    async def update_image(self, image_id: int, image_data: dict) -> None:
        """
        Update an image with the given ID using the provided data.

        Args:
            image_id: The ID of the image to update.
            image_data: A dictionary containing the updated data for the image.

        Returns:
            None
        """
        image = await Image.get(id=image_id)
        await image.update_from_dict(image_data)
        await image.save()

    async def delete_image(self, image_id: int) -> None:
        """
        Delete an image with the given ID from the database.

        Args:
            image_id: The ID of the image to delete.

        Returns:
            None
        """
        image = await Image.get(id=image_id)
        await image.delete()