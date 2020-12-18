
////1、泛型是具体类型或者其它属性的抽象替代，用于减少代码重复.
////2、在函数定义中使用泛型。
////3、在结构体中使用泛型。
////4、 枚举中的泛型。
////5、 方法中的泛型
////6、 总结:使用泛型并不会造成程序性能上的损失。
//  rust通过在编译时进行泛型代码的单>态化来保证效率。
// 单态化时通过填充【编译时使用的具体类型】，将通用代码转换为特定代码的过程。
fn main() {
    println!("泛型");

//    函数
    let num_list = vec![2, 1, 4, 5, 100, 2];
    let result = largest(&num_list);
    println!("{}", result);


//    结构体
    let integer = Point {
        x: 1,
        y: 1.23,
    };
    println!("{:#?}", integer);
    println!("{}", integer.get_x());
    let hellp = Point {
        x: "hellop",
        y: "world",
    };
    let p=integer.get_new(hellp);
    println!("{}",p.get_x());
}

//TODO 函数中
//按序比较和右Copy的特征
fn largest<T: PartialOrd + Copy>(list: &[T]) -> T {
    let mut larger = list[0];
    for &item in list.iter() {
        if item > larger {
            larger = item;
        }
    }
    return larger;
}


//TODO 结构体中
#[derive(Debug)]
struct Point<T, Z> {
    x: T,
    y: Z,
}

impl<T, Z> Point<T, Z> {
    fn get_x(&self) -> &T {
        &self.x
    }

    fn get_new<A, B>(&self, other: Point<A, B>) -> Point<A, B> {
        Point {
            x: other.x,
            y: other.y,
        }
    }
}

//TODO 枚举中
enum Option<T> {
    Some(T),
    None,
}

enum Result<T, E> {
    Ok(T),
    Err(E),
}
