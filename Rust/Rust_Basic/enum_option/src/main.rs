fn main() {
    println!("Option");
//    Option是标准库定义的一个枚举 形如：：
    //enum Option<T> {
////    Some(T),
////    None,
////}


    let sone_number = Some(5);
    let some_string = Some(String::from("a string"));
    let sonme_number: Option<i32> = None;

    let x: i32 = 5;
    let y: Option<i32> = Some(5);
    let mut temp = 0;

    match y {
//        必须匹配所有，否则报错，如何解决？
        Some(i) => {
            temp = i;
        }
        None => {}
    }
    let sum = x + temp;
    println!("sum = {}", sum);
//    let  sum= x+y;

    if let Some(value)=plus_one(y) {
        println!("value = {}",value)
    }else {

    }

}

fn plus_one(x:Option<i32>)-> Option<i32>{
    match x {
        Some(x)=> Some(x+1),
        None=>None ,
    }
}


