//TODO 2、返回闭包
//编译时不知道类型大小。没有实现Sized 的trait。
//fn return_clo() -> Fn(i32) -> i32 {
//    |x| x+1
//}


fn return_clo() -> Box<dyn Fn(i32)->i32> {
    Box::new(|x| x+1)
}

fn main() {
    let c = return_clo();
    println!("1 + 1 = {}", c(1));
    println!("1 + 1 = {}", (*c)(1));//解引用
    println!("Hello, world!");
}
