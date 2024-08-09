import pytest
from imghash import decode


def test_hash_distance_with_same_shape():
    # Arrange
    hash1 = decode("24f0", width=4, height=4)
    hash2 = decode("3efa", width=4, height=4)

    # Act
    distance = hash1.distance(hash2)

    # Assert
    assert distance == 5


def test_hash_distance_with_different_shape():
    # Arrange
    hash1 = decode("24f0", width=4, height=4)
    hash2 = decode("3efaa3ea3", width=6, height=6)

    # Act
    with pytest.raises(ValueError) as e:
        hash1.distance(hash2)

    # Assert
    assert e.match("different size")
