# Image Hashing powered by Rust

This package is a thin wrapper that contains Python bindings for the Rust crate `imghash-rs` that allows you to generate various image hashes. the following hashes are supported:

* Average Hash
* Difference Hash
* Perceptual Hash

If you want to know more about the different hashes or how they get encoded / decoded, check the documentation of [`imghash-rs`](https://github.com/YannickAlex07/imghash-rs).

## Getting Started

To get started add the package to your project:

```shell
pip install imghash-rs
```

Then you can use it by importing the different functions:

```python
from imghash import average_hash, difference_hash, perceptual_hash

ahash = average_hash("path/to/image")

print(ahash.hex()) # will return the hash encoded as string
print(ahash.bits()) # will return a 2D list of bools that are the encoded bits
```

To learn more about the underlying bit matrix that gets generated, check this [document](https://github.com/YannickAlex07/imghash-rs/blob/main/docs/encoding.md).