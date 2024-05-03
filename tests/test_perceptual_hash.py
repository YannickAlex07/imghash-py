import pytest
from conftest import ResourceFunc
from imghashpy import perceptual_hash


def test_perceptual_hash(resource: ResourceFunc):
    # Arrange
    img_path = resource("test.png")

    # Act
    hash = perceptual_hash(img_path.absolute().as_posix())

    # Assert
    assert hash
    assert hash.hex() == "acdbe86135344e3a"
    assert hash.bits()


def test_perceptual_hash_with_txt_file(resource: ResourceFunc):
    # Arrange
    img_path = resource("test.txt")

    # Act
    with pytest.raises(RuntimeError) as e:
        perceptual_hash(img_path.absolute().as_posix())

    # Assert
    assert e.match("image format")