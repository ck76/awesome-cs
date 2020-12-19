
//// (1) 进程是资源分配己的最小单位，线程是CPU调度的最小单位。
//// (2) 在使用多线程时，经常会遇到的一些问题
////
//1
//竞争状态:多个线程以不一致的顺序访问数据或资源;
////
//2.死锁:两个线程相互等待对方停止使用其所拥有的资源，造成两者都永久等待; //A: 1->2->3 B:
////
//2->1->3
//t1: A:1, B:2
//接下来等待: A:2; B:1
////
//3.只会发生在特定情况下且难以稳定重现和修复的bug
//// (3) 编程语言提供的线程叫做绿色线程，如go语言，在底层实现了M:N的模型，即M个绿色线程对应N个0S线程。但
//是
//Rust标准库只提供1: 1的线程模型的实现，即一个Rust线程对应一个0s线程。
////
//运行时代表二进制文件中包含的由语言本身提供的代码，这些代码根据语言的不同可大可小，不过非汇>
//编语言都会有一定数量的运行时代码。通常，大家说一个语言“没有运行时”，是指这个语言的“运行时"很小。Rust、
//C都是几乎没有运行时的。


//fn main() {
//    let handle = thread::spawn(|| {
//        for i in 1..10 {
//            println!("number {} in spawn thread!", i);
//            thread::sleep(Duration::from_millis(1));
//        }
//    });
//
//    for i in 1..5 {
//        println!("number {} in main thread!", i);
//        thread::sleep(Duration::from_millis(1));
//    }
//
//    println!("Hello, world!");
//    handle.join().unwrap();
//}

use std::thread;
use std::time::Duration;

fn main() {
//    zero(); 没有等待子线程执行结束
    one();
}

//+++++++++++++++++++++
//number 1 in main thread!
//number 1 in spawn thread!
//number 2 in main thread!
//number 2 in spawn thread!
//number 3 in main thread!
//number 3 in spawn thread!
//number 4 in main thread!
//number 4 in spawn thread!
//Hello, world!
//number 5 in spawn thread!
fn zero(){
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("number {} in spawn thread!", i);
            thread::sleep(Duration::from_millis(1));
        }
    });


    println!("+++++++++++++++++++++");
    for i in 1..5 {
        println!("number {} in main thread!", i);
        thread::sleep(Duration::from_millis(1));
    }

    println!("Hello, world!");
}

//number 1 in spawn thread!
//number 2 in spawn thread!
//number 3 in spawn thread!
//number 4 in spawn thread!
//number 5 in spawn thread!
//number 6 in spawn thread!
//number 7 in spawn thread!
//number 8 in spawn thread!
//number 9 in spawn thread!
//+++++++++++++++++++++
//number 1 in main thread!
//number 2 in main thread!
//number 3 in main thread!
//number 4 in main thread!
//Hello, world!
fn one(){
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("number {} in spawn thread!", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

//    t.join()方法只会使主线程(或者说调用t.join()的线程)进入等待池
// 并等待t线程执行完毕后才会被唤醒。
// 并不影响同一时刻处在运行状态的其他线程。
//    【等待子线程结束再执行main】
    handle.join().unwrap();

    println!("+++++++++++++++++++++");
    for i in 1..5 {
        println!("number {} in main thread!", i);
        thread::sleep(Duration::from_millis(1));
    }

    println!("Hello, world!");
}



















//（1）进程是资源分配的最小单位，线程是CPU调度的最小单位。
//（2）在使用多线程时，经常会遇到的一些问题：
//         1. 竞争状态：多个线程以不一致的顺序访问数据或资源；
//          2.死锁：两个线程相互等待对方停止使用其所拥有的资源，造成两者都永久等待；A: 1->2->3  B:
//            2->1->3    t1: A:1, B:2    接下来： A：2， B：1   造成死锁
//          3.只会发生在特定情况下且难以稳定重现和修复的bug
//（3）编程语言提供的线程叫做绿色线程，如go语言，在底层实现了M:N的模型，即M个绿色线程对应N个OS线程。但是，Rust标准库只提供1：1的线程模型的实现，即一个Rust线程对应一个Os线程。
//         运行时代表二进制文件中包含的由语言本身提供的代码，这些代码根据语言的不同可大可小，不过非汇编语言都会有一定数量的运行时代码。通常，大家说一个语言“没有运行时”，是指这个语言的“运行时”很小。Rust、C都是几乎没有运行时的。
