//TODO C语言调用Rust
#![crate_type = "staticlib"]
#[no_mangle]
pub extern fn foo(i:i32) {
    println!("use rust {}",i);
}
