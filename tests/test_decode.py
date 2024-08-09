import pytest
from imghash import decode


def test_decode_with_correct_shape():
    # Arrange
    hash_str = "24f0"

    # Act
    hash = decode(hash_str, width=4, height=4)

    # Assert
    assert hash.encode() == hash_str


def test_decode_with_incorrect_shape():
    # Arrange
    hash_str = "24f0"

    # Act
    with pytest.raises(ValueError) as e:
        decode(hash_str, width=5, height=4)

    # Assert
    assert e.match("too short or too long")
