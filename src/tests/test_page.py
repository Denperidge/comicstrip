import unittest

from ..comicstrip.Page import Page
from .helpers import test_jpg, test_data, read_test_images, list_original_images, list_generated_images

class TestPage(unittest.TestCase):
    
    def test_save(self):
        Page(test_jpg).save(test_data + "output_from_tests/cstrip-")

        original_images = list_original_images()
        generated_images = list_generated_images()

        self.assertEqual(
            len(original_images), len(generated_images),
            f"There is a different amount of images generated ({len(generated_images)}) than originally ({len(original_images)})"
            )

        for filename in original_images:
            original_image, generated_image = read_test_images(filename)
            self.assertEqual(original_image, generated_image,
                             f"The generated output for {filename} is different than originally")
            

   


if __name__ == "__main__":
    unittest.main()