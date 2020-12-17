use std::collections::HashMap;

fn main() {
    println!("hashmap!");

//    HashMap<K,V>

//    TODO 创建

//    let mut scores: HashMap<&str, i32> = HashMap::new();
//    scores.insert("cheng", 100);
//    scores.insert("kun", 200);
    let mut scores: HashMap<String, i32> = HashMap::new();
    scores.insert(String::from("cheng"), 100);
    scores.insert(String::from("kun"), 200);

    let keys = vec![String::from("cheng"), String::from("kun")];
    let values = vec![10, 20];
//    let mut scores: HashMap<_, _> = keys.iter().zip(values.iter()).collect();

    let k = String::from("cheng");
    let v = scores.get(&k);
//    if Some(v) {
////          ^ `std::option::Option<&&{integer}>` cannot be formatted with the default formatter
//        println!("v = {}",v);
//    }
    if let Some(v) = scores.get(&k) {
        println!("v = {}", v);
    }

    match v {
        Some(v) => println!("v = {}", v),
        None => {}
    }

//    TODO 读取
//    for elem in &scores{
//        println!("{}",elem);// ^^^^ `(&&str, &i32)` cannot be formatted with the default formatter
//
//    }


//    TODO 遍历
    for (key, value) in &scores {
        println!("{} ,{}", key, value);
    }
//    TODO 为什么在这添加不了,目前不知道具体为什么，就是因为上面
    /**
     let mut scores: HashMap<_, _> = keys.iter().zip(values.iter()).collect();

    **/
    scores.insert(String::from("cheng"), 99990);

    for (key, value) in &scores {
        println!("{} ,{}", key, value);
    }

//    TODO 更新
//    直接插入
    let mut ss = HashMap::new();
    ss.insert(String::from("one"), 1);
    ss.insert(String::from("two"), 2);
    ss.insert(String::from("three"), 3);
    println!("ss = {:?}", ss);
//    键不存在时候插入
    let mut ss1 = HashMap::new();
    ss1.insert(String::from("one"), 1);
    ss1.insert(String::from("two"), 2);
    ss1.insert(String::from("three"), 3);
    ss1.entry(String::from("one")).or_insert(3);
    println!("ssl = {:#?}", ss1);
//    根据旧值更新新的值?????????????????????????????
//    count什么时候插入到map了？？？？？？？？？？？？？
    let text = "hello world wonderful world";
    let mut map = HashMap::new();
    for word in text.split_whitespace() {
        let count = map.entry(word).or_insert(0);
        *count += 1;
    }
    println!("map = {:#?}", map);
}
