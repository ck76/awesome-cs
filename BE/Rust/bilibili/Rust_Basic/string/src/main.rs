fn main() {
    println!("String");


//    TODO 创建一个空字符串
    let mut s0 = String::new();
    s0.push_str("cheng kun ");
    println!("s0 = {}", s0);

//    TODO 更新字符串
    let mut hello = String::from("hello,");
    hello.push_str("world ");
    let tan = " !".to_string();
    hello.push_str(&tan);
    println!("{}", hello);

    hello.push('x');
//    hello.push("x");   ^^^ expected char, found reference
    println!("{}", hello);

//    TODO 字符串想加
//    let s1="s1";
//    let s2="s2";
//    let s3=s1+s2;//`+` cannot be used to concatenate two `&str` strings

    let s1 = "s1".to_string();
    let s2 = String::from("s2");
    let s3 = s1 + &s2;
//    s1;//  ^^ value used here after move s1的所有权被移走了，s3拿走s1的所有权，然后再把s2加到自己上
    s2;//可以

//  TODO format
    let cheng = String::from("cheng");
    let kun = String::from("kun");
    let chengkun = format!("{}+{}", cheng, kun);
    println!("{}", chengkun);

//    TODO String类是不能被索引的
    let cheng=String::from("cheng");
//    cheng[1];//  ^^^^^^^^ `std::string::String` cannot be indexed by `{integer}`
    let kun="kun";
//    &kun[1]; //^^^^^^ string indices are ranges of `usize`
    &kun[1..];

//    TODO 遍历 chars
//    按字符
    for c in String::from("你好").chars(){
        println!("{}",c);
    }
//    按字节
    for c in String::from("你好").bytes(){
        println!("{}",c);
    }

}
