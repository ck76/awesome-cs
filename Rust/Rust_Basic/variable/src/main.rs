const MAX_VALUE: u32 = 100;

fn main() {
    println!(" ---------------- ");

//    1 定义
    let a = 1;
    println!("a = {}", a);

    let mut b: u32 = 1;
    println!("b = {}", b);

    b = 2;
    println!("b = {}", b);

//    2 隐藏
    let b: f32 = 1.1;
    println!("b = {}", b);
//    3 常量
    println!("MAX_VALUE = {}", MAX_VALUE);


    println!(" ---------------- ");

    let is_true: bool;
    let is_false: bool;

//    在rust里char是32位的，可以是汉字也可以是普通字符

    let a = "a";
    let a = 'a';
    let a: i8;
    let a: i16;
    let a: i32;
    let a: u8;
    let a: u16;
    let a: u32;
    let a: f32;
    let a: f64;

//    自适应类型【长度随着平台不同不一样】
    println!("max = {}", usize::max_value());
//    max = 18446744073709551615

    println!(" ---------------- ");

//    数组
//    [Type ; size]
    let arr: [u32; 5] = [1, 2, 3, 4, 5];
    println!("arr[1] = {}", arr[1]);
    show(arr);

    println!(" ---------------- ");

//  元祖
    let tup = (-2, 3.6, '好');
    let (x, y, z) = tup;
//    show_tuple(tup); 打印不了，没有实现iterator接口
    println!(" ---------------- ");

//    控制流

    let y = 1;
    if y == 1 {
        println!("y = 1", );
    } else {
        println!("y != 1", );
    }

    let conditon = true;
    let x = if conditon {
        5
    } else {
        6
    };


//    循环
    println!(" ---------------- ");
    let mut counter = 0;
    loop {
        counter = counter + 1;
        if counter == 10 {
            break;
        }
    }

    println!("counter = {}", counter);
    let result = loop {
        counter += 1;
        if counter == 20 {
//            貌似返回的这个counter没起作用，始终都是counter==20；
            break 2 * counter;
        }
    };
    println!("counter = {}", counter);
//    while
    let mut i = 0;
    while i != 10 {
        i = i + 1;
    }

//    for
    let arr: [u32; 5] = [1, 2, 3, 4, 5];
    for element in arr.iter() {
        println!(" {}", element);
    }

    for element in &arr {
        println!(" {}", element);
    }
}

fn show(arr: [u32; 5]) {
    println!(" ---------------- ");
    for i in &arr {
        println!(" {}", i);
    }
    println!(" ---------------- ");
}

//
//编译都编译不过
//fn show_tuple(tuple:(i32,f64,char)) {
//    println!(" ---------------- ");
//    for i in &show_tuple {
////         ^^^^^^^^^^^ `&fn((i32, f64, char)) {show_tuple}` is not an iterator
//        println!(" {}", i);
//    }
//    println!(" ---------------- ");
//}
