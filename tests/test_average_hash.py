import pytest
from conftest import ResourceFunc
from imghash import average_hash


def test_average_hash(resource: ResourceFunc):
    # Arrange
    img_path = resource("test.png")

    # Act
    hash = average_hash(img_path.absolute().as_posix())

    # Assert
    assert hash
    assert hash.hex() == "ffffff0e00000301"
    assert hash.bits()


def test_average_hash_with_txt_file(resource: ResourceFunc):
    # Arrange
    img_path = resource("test.txt")

    # Act
    with pytest.raises(RuntimeError) as e:
        average_hash(img_path.absolute().as_posix())

    # Assert
    assert e.match("image format")
