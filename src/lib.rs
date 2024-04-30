use pyo3::prelude::*;
use std::path;

use imghash::ImageHasher;

// struct to hold the hash
#[pyclass]
pub struct Hash {
    #[pyo3(get)]
    pub bits: Vec<Vec<bool>>,

    #[pyo3(get)]
    pub hex: String,
}

#[pyfunction]
pub fn average_hash(img_path: &str, width: u32, height: u32) -> Option<Hash> {
    let hasher = imghash::average::AverageHasher {
        width,
        height,
        ..Default::default()
    };

    match hasher.hash_from_path(path::Path::new(img_path)) {
        Ok(hash) => {
            return Some(Hash {
                bits: hash.matrix.clone(),
                hex: hash.encode(),
            });
        }
        Err(_) => return None,
    }
}

// difference hash

// perceptual hash

#[pymodule]
fn imghashpy(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<Hash>()?;
    m.add_function(wrap_pyfunction!(average_hash, m)?)?;
    Ok(())
}
