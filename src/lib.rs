use pyo3::{exceptions::PyValueError, prelude::*};
use std::path;

use imghash::{ImageHash, ImageHasher};

// struct to hold the hash
#[pyclass]
pub struct Hash {
    hash: ImageHash,
}

#[pymethods]
impl Hash {
    pub fn matrix(&self) -> Vec<Vec<bool>> {
        #[allow(deprecated)]
        self.hash.matrix()
    }

    pub fn encode(&self) -> String {
        self.hash.encode()
    }

    pub fn distance(&self, other: &Hash) -> PyResult<usize> {
        let result = self.hash.distance(&other.hash);
        match result {
            Ok(d) => Ok(d),
            Err(e) => Err(PyValueError::new_err(e.to_string())),
        }
    }

    pub fn shape(&self) -> (usize, usize) {
        self.hash.shape()
    }
}

// average hash

#[pyfunction]
#[pyo3(signature = (img_path, width=8, height=8))]
pub fn average_hash(img_path: &str, width: u32, height: u32) -> PyResult<Hash> {
    let hasher = imghash::average::AverageHasher {
        width,
        height,
        ..Default::default()
    };

    match hasher.hash_from_path(path::Path::new(img_path)) {
        Ok(hash) => {
            return Ok(Hash { hash });
        }
        Err(e) => return Err(PyValueError::new_err(e.to_string())),
    }
}

// difference hash

#[pyfunction]
#[pyo3(signature = (img_path, width=8, height=8))]
pub fn difference_hash(img_path: &str, width: u32, height: u32) -> PyResult<Hash> {
    let hasher = imghash::difference::DifferenceHasher {
        width,
        height,
        ..Default::default()
    };

    match hasher.hash_from_path(path::Path::new(img_path)) {
        Ok(hash) => {
            return Ok(Hash { hash });
        }
        Err(e) => return Err(PyValueError::new_err(e.to_string())),
    }
}

// perceptual hash

#[pyfunction]
#[pyo3(signature = (img_path, width=8, height=8))]
pub fn perceptual_hash(img_path: &str, width: u32, height: u32) -> PyResult<Hash> {
    let hasher = imghash::perceptual::PerceptualHasher {
        width,
        height,
        ..Default::default()
    };

    match hasher.hash_from_path(path::Path::new(img_path)) {
        Ok(hash) => {
            return Ok(Hash { hash });
        }
        Err(e) => return Err(PyValueError::new_err(e.to_string())),
    }
}

// decoding
#[pyfunction]
#[pyo3(signature = (hash, width=8, height=8))]
pub fn decode(hash: &str, width: u32, height: u32) -> PyResult<Hash> {
    match ImageHash::decode(hash, width, height) {
        Ok(hash) => {
            return Ok(Hash { hash });
        }
        Err(e) => return Err(PyValueError::new_err(e.to_string())),
    }
}

#[pymodule]
#[pyo3(name = "imghash")]
fn imghashpy(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<Hash>()?;

    m.add_function(wrap_pyfunction!(average_hash, m)?)?;
    m.add_function(wrap_pyfunction!(difference_hash, m)?)?;
    m.add_function(wrap_pyfunction!(perceptual_hash, m)?)?;
    m.add_function(wrap_pyfunction!(decode, m)?)?;

    Ok(())
}
