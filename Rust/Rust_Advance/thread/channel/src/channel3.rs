use std::thread;
use std::sync::mpsc;
use std::time::Duration;

//控制台慢慢打印 多个数据
fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    for recv in rx {
//        控制台慢慢打印
        println!("Got: {}", recv);
    }
    println!("Hello, world!");
}
