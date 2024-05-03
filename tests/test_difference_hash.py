import pytest
from conftest import ResourceFunc
from imghashpy import difference_hash


def test_difference_hash(resource: ResourceFunc):
    # Arrange
    img_path = resource("test.png")

    # Act
    hash = difference_hash(img_path.absolute().as_posix())

    # Assert
    assert hash
    assert hash.hex() == "cc99717ed9ea0627"
    assert hash.bits()


def test_difference_hash_with_txt_file(resource: ResourceFunc):
    # Arrange
    img_path = resource("test.txt")

    # Act
    with pytest.raises(RuntimeError) as e:
        difference_hash(img_path.absolute().as_posix())

    # Assert
    assert e.match("image format")