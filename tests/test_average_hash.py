from imghashpy import average_hash

from conftest import ResourceFunc


def test_average_hash(resource: ResourceFunc):
    # Arrange
    img_path = resource("test.png")

    # Act
    hash = average_hash(img_path.absolute().as_posix(), width=8, height=8)

    # Assert
    assert hash
    assert hash.hex == "ffffff0e00000301"
