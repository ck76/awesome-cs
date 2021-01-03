fn main() {
//    字符串slice是String中一部分值的引用
    println!("Silce!");


    let s = String::from("hello,world!");
    let h = &s[0..5];
    let h = &s[0..=4];
    let h = &s[..4];
    println!("h = {}", h);

    let w = &s[6..11];
    let w = &s[6..=10];
    let w = &s[6..];
    let w = &s[..];
    println!("w = {}", w);

    let ss = String::from("你好");
    let w1 = &ss[9..1];
//    thread 'main' panicked at 'byte index 9 is out of bounds of `你好`', src/libcore/str/mod.rs:2051:9
//note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace.
    println!("w1 = {}", w1);


}
