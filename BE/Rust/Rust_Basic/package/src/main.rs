use mylib::factory::produce_refrigerator;
//提倡
use mylib::factory::produce_refrigerator as CK;
use mylib::factory::produce_refrigerator::produce_re;
use mylib::factory::*;
use mylib::factory::modA;

fn main() {
    println!("包和crate");
    let s = "1、定义
                    (1)包: Cargo的一-个功能，允许构建、测试和分享crate。
                    (2) Crate:一个模块的树形结构,形成库或二进制项目。
                    (3)模块:通过use来使用，用来控制作用域和路径的私有性。
                    (4)路径:一个命名例如结构体、函数或模块等项的方式。
                    2、包和Crate
                    (1) crate root是一个源文件，Rust 编译器以它为起始点，并构成你的crate的根模
                    块。
                    (2)包提供一系列功能的一 个或多个Crate。
                    (3) Crate root是src/main.rs或者是src/lib.rs。说明: 如果只有main.rs则说明这个包只
                    有一个crate (main) ，如果同时拥有main。rs和其它的lib.rs (不一 定是这个名字) 则说
                    明拥有多个crate。
                    (4) crate会将一 个作用域的相关功能分组到- -起，使得该功能可以很方便的在多个项目
                    之间共享。";
    println!("{}", s);

//    factory::produce_refrigerator::produce_re();

//    绝对路径
    mylib::factory::produce_refrigerator::produce_re();
    produce_refrigerator::produce_re();
    produce_re();//分不清
    CK::produce_re();

    use_mode_a();
    use_external();
}

fn use_mode_a() {
    let a = modA::A::new_a();
    a.print_a();

    let number = a.number;
    let name = a.name;
    println!("{},{}", number, name);
    modA::modB::modC::print_C();
}


extern crate crypto;

use crypto::digest::Digest;
use crypto::sha3::Sha3;

fn use_external() {
    let mut hasher = Sha3::sha3_256();
    hasher.input_str("hello world");
    let result = hasher.result_str();
    println!("hash = {}", result);
}

