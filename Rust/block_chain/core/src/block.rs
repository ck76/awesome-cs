pub struct BlockHeader {
    pub time: i64,
    pub tx_hash: String,
    pub pre_hash: String,
}


pub struct Block {
    pub header: BlockHeader,
    pub hash: String,
    pub data: String,
}

//序列化区块头
//对自己的区块头求哈希
//impl Block {
//    pub fn hash() -> String {
//
//    }
//}

