use std::thread;
use std::sync::mpsc;
use std::time::Duration;

//TODO 多生产者消费者

//Got: hi
//Got: hi
//Got: A
//Got: a
//Got: B
//Got: b
//Got: from
//Got: c
//Got: the
//Got: C
//Got: d
//Got: D
//Got: thread
//Hello, world!
fn main4() {
    let (tx, rx) = mpsc::channel();
    let tx1 = mpsc::Sender::clone(&tx);
    let tx2 = mpsc::Sender::clone(&tx);
//    let rx1 = mpsc::Receiver::clone(&rx);
    thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];

        for val in vals {
            tx1.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    thread::spawn(move || {
        let vals = vec![
            String::from("A"),
            String::from("B"),
            String::from("C"),
            String::from("D"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    thread::spawn(move || {
        let vals = vec![
            String::from("a"),
            String::from("b"),
            String::from("c"),
            String::from("d"),
        ];

        for val in vals {
            tx2.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

//    消费者
    for rec in rx {
        println!("Got: {}", rec);
    }

    println!("Hello, world!");
}
