use pyo3::{exceptions::PyRuntimeError, prelude::*};
use std::path;

use imghash::{ImageHash, ImageHasher};

// struct to hold the hash
#[pyclass]
pub struct Hash {
    hash: ImageHash,
}

#[pymethods]
impl Hash {
    pub fn bits(&self) -> Vec<Vec<bool>> {
        self.hash.matrix.clone()
    }

    pub fn hex(&self) -> String {
        self.hash.encode()
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
        Err(e) => return Err(PyRuntimeError::new_err(e.to_string())),
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
        Err(e) => return Err(PyRuntimeError::new_err(e.to_string())),
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
        Err(e) => return Err(PyRuntimeError::new_err(e.to_string())),
    }
}

#[pymodule]
#[pyo3(name = "imghash")]
fn imghashpy(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<Hash>()?;

    m.add_function(wrap_pyfunction!(average_hash, m)?)?;
    m.add_function(wrap_pyfunction!(difference_hash, m)?)?;
    m.add_function(wrap_pyfunction!(perceptual_hash, m)?)?;

    Ok(())
}
