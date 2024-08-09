import pytest
from conftest import ResourceFunc
from imghash import perceptual_hash


def test_perceptual_hash(resource: ResourceFunc):
    # Arrange
    img_path = resource("test.png")

    # Act
    hash = perceptual_hash(img_path.absolute().as_posix())

    # Assert
    assert hash
    assert hash.encode() == "acdbe86135344e3a"
    assert hash.matrix()


def test_perceptual_hash_with_txt_file(resource: ResourceFunc):
    # Arrange
    img_path = resource("test.txt")

    # Act
    with pytest.raises(ValueError) as e:
        perceptual_hash(img_path.absolute().as_posix())

    # Assert
    assert e.match("image format")
