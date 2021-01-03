fn main() {
    println!("vector");
//创建空的vector: Vec<T>
    let v: Vec<i32> = Vec::new();
//    v.push(1);// cannot borrow as mutable
    let mut v: Vec<i32> = Vec::new();
    v.push(1);


//    创建包含初始值的Vector【使用宏】
    let v = vec![1, 2, 3];


//    丢弃Vector
    {
        let v = vec![1, 2, 3];
    }

//    更新元素
    let mut v2: Vec<i32> = Vec::new();
    v2.push(1);
    v2.push(2);
    v2.push(3);


//    读取元素[会把里面的元素统统丢弃]

    let one: &i32 = &v[0];
    let v = vec![1, 2, 3];
    println!("one = {}", one);

//    TODO 没执行到？？？？？？？？？？？？？？？？？？？？？？？？？？？？
    match v2.get(4) {
        Some(value) => println!("value = {}", value),
        _ => {}
    }
//    不可变遍历
    for element in &v {
        println!("{}", element);
    }

//    可变遍历
    for element in &mut v2 {
        *element += 1;
        println!("{}", element);
    }

//    使用枚举
    let v_enum: Vec<Context> = vec![
        Context::Text(String::from("a")),
        Context::Float(2.0),
        Context::Int(100), ];

//    补充
    let mut v = vec![1, 2, 3, 4, 5];
    let first = &v[0];//不可变
    v.push(6);//可变
//    first;//可变之后不能再使用不可变了。
    /**
56 |     let first=&v[0];
   |                - immutable borrow occurs here
57 |     v.push(6);
   |     ^^^^^^^^^ mutable borrow occurs here
58 |     first;
   |     ----- immutable borrow later used here

    **/
}

enum Context {
    Text(String),
    Float(f32),
    Int(i32),
}
