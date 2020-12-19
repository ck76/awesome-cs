//1、Drop trait类似于其它语言中的【析构函数】，当值【离开作用域】的时候执行此函数的代码。
//

include!("drop2.rs");

fn main() {
    let a = Dog{name: String::from("mian wangcai")};
    {
        let b = Dog{name: String::from("mian dahuang")};
        println!("0main +++++++++++++++++++");
    }

    println!("1main +++++++++++++++++++");

    println!("main函数结束 +++++++++++++++++++");
    main2();
}
