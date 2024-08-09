from imghash import decode


def test_shape():
    # Arrange
    hash = decode("24f0", width=4, height=4)

    # Act
    shape = hash.shape()

    # Assert
    assert shape == (4, 4)
