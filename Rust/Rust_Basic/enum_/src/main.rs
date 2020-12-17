//    类似C语言定义方式
#[derive(Debug)]
enum IpAddKind {
    V4,
    V6,
}

struct IpAddr {
    kind: IpAddKind,
    address: String,
}


//    Rust提倡的方式
enum IpAddr2 {
    V4(String),
    V6(String),
}

//    可以使不同类型
enum IpAddr3 {
    V4(u8, u8, u8, u8),
    V6(String),
}

//    经典用法
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    Change(i32, i32, i32),
}

//    等同于
struct QuiteMessage;

//类单元结构体
struct MoveMessage {
    x: u32,
    y: u32,
}

struct WriteMessage(String);

struct Chang(i32, i32, i32, i32);


//    枚举类型的方法及match

fn main() {
    println!("enum");
    let ip1 = IpAddr {
        kind: IpAddKind::V4,
        address: String::from("127. 0.0.1"),
    };
    let ip1 = IpAddr2::V4(String::from("127.0.1.1"));

//    println!("{:#?}",ip1);

    let quit=Message::Quit;
    quit.print();
    let move_=Message::Move {x:10,y:100};
    move_.print();
}

impl Message {
    fn print(&self) {
//        解引用
        match *self {
            Message::Quit => println!("Quit"),
            Message::Move{x, y} => println!("Move"),
//            TODO  有问题
//            Message::Write(&s) => println!("Write"),
            Message::Change(a,b,c) => println!("Change"),
            _ => println!("default"),
        }
    }
}
