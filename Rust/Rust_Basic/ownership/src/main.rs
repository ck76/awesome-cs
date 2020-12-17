fn take_ownership(some_string: String) -> String {
    println!("s = {}", some_string);
    some_string
}

fn make_copy(i: u32) {
    println!("i = {}", i);
}


fn main() {
    let mut ownership = String::from("ownership");
    println!("{}", &mut ownership);

    ownership.push_str("  hhhhh");
    println!("{}", &ownership);//String离开作用于会调用drop方法

    let l3 = ownership.clone();
    println!("{}", l3);

//    copy trait 栈拷贝
//    常用的具备copy特征：程序的内建类型，包括元祖
    let a = 1;
    let b = a;
    println!("a = {}, b = {}", a, b);

//    函数作用域
    let s = String::from("hello");
    take_ownership(s);

    let i = 1;
    make_copy(i);
    println!("i = {},栈变量还能用", i);

//    引用
//    以书为例子，有书才能借给别人，书本身是不是可以更改的，书借出去的时候是不是可以更改的

    /**
    可以同时存在多个不可变引用
    但是以可变引用借出去之后就暂且不可使用不可变引用
    因为rust不知道你可能在操作那个可变引用的时候对变量做了什么更改，所以就再编译的时候限制
35 |     let ref_s=&mut s;
   |               ------ mutable borrow occurs here
...
38 |     let ref_s4= & s;
   |                 ^^^ immutable borrow occurs here
39 |     let size = caculate_length(ref_s);
   |                                ----- mutable borrow later used here


    **/
    let mut s = String::from("ck");
    let im_ref1 = &s;
    let im_ref2 = &s;
    let ref_s = &mut s;
//    let ref_s3= &mut s;//second mutable borrow occurs here
//    let ref_s4= & s;// ^^^ immutable borrow occurs here
// ----- mutable borrow later used here
    let size = caculate_length(ref_s);
    let im_ref = &s;

//    println!("{}",im_ref2);

    println!("{} 的size = {}", s, size);


//    悬垂引用。野指针
    let ref_null = dangle();
}

//引用 & [借用]，创建一个指向值的引用，但是并不拥有值，
// 因为不拥用值，引用离开作用于后，值也不会被回收，因为书本来就不是我的
fn caculate_length(s: &mut String) -> usize {
    s.push_str(",,,,,");
    return s.len();
}

fn dangle() -> &String {
//      ^ help: consider giving it a 'static lifetime: `&'static`
    let s = String::from("hello");
    &s
}

