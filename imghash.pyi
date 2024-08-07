class Hash:
    def bits(self) -> list[list[bool]]:
        """
        Returns a 2D lists of bools that represent the bit-matrix
        behind the hash.

        Returns:
            list[list[bool]]: The 2D matrix of bits
        """
        ...

    def hex(self) -> str:
        """
        Returns the hexadecimal encoded representation of the hash.

        Returns:
            str: The hexadeicmal encoded hash
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
