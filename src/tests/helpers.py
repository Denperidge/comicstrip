from glob import glob
from os import makedirs
from os.path import dirname, join



test_data = join(dirname(__file__), "test_data/")

test_jpg = join(test_data, "test.jpg")

test_originals_dir = join(test_data, "output_from_original/")
test_output_dir = join(test_data, "output_from_tests/")

makedirs(test_output_dir, exist_ok=True)



def list_original_images():
    return glob("*.jpg", root_dir=test_originals_dir)

def list_generated_images():
    return glob("*.jpg", root_dir=test_output_dir)

def read_image(path):
    with open(path, "rb") as file:
        content = file.read()
    
    return content

def read_images(path1, path2):
    return [read_image(path1), read_image(path2)]

def read_test_images(filename):
    return read_images(
        test_originals_dir + filename,
        test_output_dir + filename
    )
