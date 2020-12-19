use mac;

fn main() {
    let v = mac::my_vec![1, 2, 3];
    //mac::my_vec![1, 2, 3] 等价于
    //let mut temp_vec = Vec::new();
    //temp_vec.push(1);
    //temp_vec.push(2);
    //temp_vec.push(3);
    //temp_vec

    println!("v = {:?}", v);
    println!("Hello, world!");
    main2();
}

use hello_macro::HelloMacro;
use hello_macro_derive::HelloMacro;

#[derive(HelloMacro)]
struct Main;

fn main2() {
    Main::hello_macro();
    println!("Hello, world!");
}
