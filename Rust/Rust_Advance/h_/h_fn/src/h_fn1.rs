//TODO 1、函数指针 函数指针作为另一个函数的参数
//函数指针允许我们使用函数作为另一个函数的参数。
//函数的类型是 fn ，fn 被称为 函数指针。指定参数为函数指针的语法类似于闭包。
fn add_one(x: i32) -> i32 {
    x + 1
}

fn do_twice(f: fn(i32) -> i32, val: i32) -> i32 {
    f(val) + f(val)
}

//T 必须实现Fn这个特征
fn wapper_func<T>(t: T, v: i32) -> i32
    where T: Fn(i32) -> i32 {
    t(v)
}

fn func(v: i32) -> i32 {
    v + 1
}

fn main() {
    let r = do_twice(add_one, 5);
    println!("r = {}", r);

    //+++++++++++++++++
    let a = wapper_func(|x| x+1, 1);
    println!("a = {}", a);

    let b = wapper_func(func, 1);
    println!("b = {}", b);


    println!("Hello, world!");
}

//TODO 闭包的三个特征 函数指针实现了Fn【直接使用】、FnMut【可变】、FnOnce【消费】

