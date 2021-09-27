use std::fs::File;

use std::io;
use std::io::Read;

fn main() {


//    TODO 传播错误
    let result = read_username_from_file();
    print_result(&result);

    let simple_result = simply();
    print_result(&simple_result);

    let simple_simple_result = simply_simple();
    print_result(&simple_simple_result);
}

/**
打印结果
**/
fn print_result(result: &Result<String, io::Error>) {
    match result {
        Ok(s) => { println!("s = {}", s) }
        Err(err) => { println!("err = {}", err) }
    }
}

fn read_username_from_file() -> Result<String, io::Error> {
//    //1、 当编写一个函数，但是该函数可能会失败，此时除了在函数中处理错误外，
// 还可以将错误传给调用者，让调用>者决定如何处理，这被称为传播错误。
////2、 传播错误的简写方式，提倡的方式
////3、更进一步的简写
//// TODO 4、什么时候用panic!，什么时候用Result
//
// (1) 示例、代码源性、测试用panic!/unwrap/expect
// (2) 实际项目用Result
////5、 pt ion和Result
    let f = File::open("hello.txt");
    let mut f = match f {
        Ok(file) => file,
        Err(err) => return Err(err),
    };

    let mut s = String::new();
    match f.read_to_string(&mut s) {
        Ok(_) => Ok(s),
        Err(err) => Err(err),
    }
}

fn simply() -> Result<String, io::Error> {
    let mut f = File::open("hello.txt")?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
}

fn simply_simple() -> Result<String, io::Error> {
    let mut s = String::new();
    File::open("hello.txt")?.read_to_string(&mut s);
    Ok(s)
}

fn basic() {
    //  1、(1)rust语言将错误分为两个类别:可恢复错误和不可恢复错误
//      可恢复错误通常代表向用户报告错误和重试操作是合理的情况，例如未找到文件。
//      rust中使用Result<T,E>来实现。
////    (2)不可恢复错误是bug的同义词，如尝试访问超过数组结尾的位置。rust中通过panic!来实现。
////2、 panic !
////3、 使用BACKTRACE=1
////4、 Result<T, E>{
//          Ok(T),
//          Err(E),
//      }
////5、 简写
    println!("Error");
    let f = File::open("hello.txt");
    let r = match f {
        Ok(file) => { file }
        Err(err) => { panic!("error : {:?}", err) }
    };

    let f = File::open("hello.txt").unwrap();
    let f = File::open("hello.txt").expect("Fialed ");
    panic!("crash here");
}
