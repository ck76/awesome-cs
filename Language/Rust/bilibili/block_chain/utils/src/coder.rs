use bincode;
use serde::{Deserialize, Serialize};
use crypto::digest::Digest;
use crypto::sha3::Sha3;

// pub fn serialize<T: ?Sized>(value: &T) -> Result<Vec<u8>>
// where
//     T: Serialize,
pub fn my_serialize<T: ?Sized>(value: &T) -> Vec<u8>
    where T: Serialize,
{
    let seialized = bincode::serialize(value).unwrap();
    seialized
}

// pub fn deserialize<'a, T>(bytes: &'a [u8]) -> Result<T>
// where
//     T: Deserialize<'a>,
pub fn my_deserialize<'a, T>(bytes: &'a[u8]) -> T
    where T: Deserialize<'a>,
{
    let deserialized = bincode::deserialize(bytes).unwrap();
    deserialized
}
