class Hash:
    def matrix(self) -> list[list[bool]]:
        """
        Returns a 2D lists of bools that represent the bit-matrix
        behind the hash.

        Returns:
            list[list[bool]]: The 2D matrix of bits
        """
        ...

    def shape(self) -> tuple[int, int]:
        """
        Return the shape of the underlying matrix of the hash

        Returns:
            tuple[int, int]: The shape of the matrix
        """
        ...

    def encode(self) -> str:
        """
        Returns the hexadecimal encoded representation of the hash.

        Returns:
            str: The hexadeicmal encoded hash
        """
        ...

    def distance(self, other: Hash) -> int:
        """
        Computes the hamming distance of the hash to the provided other hash.
        The hamming distance is the number of bits that differ between the two hashes.

        Args:
            other (Hash): The other hash to compute the distance to

        Returns:
            int: The distance as an int
        """
        ...

def average_hash(path: str, width: int = 8, height: int = 8) -> Hash:
    """
    Generates the average hash for an image at the provided path.

    Args:
        path (str): The path of the image
        width (int, optional): The width of the resulting bit matrix. Defaults to 8.
        height (int, optional): The height of the resulting bit matrix. Defaults to 8.

    Returns:
        Hash: An object representing the hash
    """
    ...

def difference_hash(path: str, width: int = 8, height: int = 8) -> Hash:
    """
    Generates the difference hash for an image at the provided path.

    Args:
        path (str): The path of the image
        width (int, optional): The width of the resulting bit matrix. Defaults to 8.
        height (int, optional): The height of the resulting bit matrix. Defaults to 8.

    Returns:
        Hash: An object representing the hash
    """
    ...

def perceptual_hash(path: str, width: int = 8, height: int = 8) -> Hash:
    """
    Generates the perceptual hash for an image at the provided path.

    Args:
        path (str): The path of the image
        width (int, optional): The width of the resulting bit matrix. Defaults to 8.
        height (int, optional): The height of the resulting bit matrix. Defaults to 8.

    Returns:
        Hash: An object representing the hash
    """
    ...

def decode(hash: str, width: int = 8, height: int = 8) -> Hash:
    """
    Decodes a hash with the given shape into a hash. This can fail with a ValueError.

    Args:
        hash (str): The hash to decode
        width (int, optional): The width of the bit matrix. Defaults to 8.
        height (int, optional): The height of the bit matrix. Defaults to 8.

    Returns:
        Hash: The decoded hash
    """
    ...
