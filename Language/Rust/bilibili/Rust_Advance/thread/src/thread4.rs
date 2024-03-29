//RefCell\Rc\Box

//RefCell<T>/Rc<T> 【与】 Mutex<T>/Arc<T>

//1、Mutex<T>提供内部可变性，类似于RefCell
//2、RefCell<T>/Rc<T>是【非】线程安全的， Mutex<T>/Arc<T>是线程安全的
use std::sync::Mutex;
use std::thread;
//use std::rc::Rc;
use std::sync::Arc;

// TODO 多线程mutex
//Arc<T>
fn main() {
    //let counter = Mutex::new(0);
    //let counter = Rc::new(Mutex::new(0));  //rc不能再线程间安全发送
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

//    10个线程要拿到线程的所有权，所以
    for _ in 0..10 {
        let cnt = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = cnt.lock().unwrap();
            *num += 1;
        });

        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("resut = {}", *counter.lock().unwrap());
    println!("Hello, world!");
}

//fn main() {
//    //Rc<T> 不是线程安全的
//    //let counter = Mutex::new(0);
//    let counter = Rc::new(Mutex::new(0));
//    let mut handles = vec![];
//
//    for _ in 0..10 {
//        let cnt = Rc::clone(&counter);
//        let handle = thread::spawn(move || {
//            let mut num = cnt.lock().unwrap();
//            *num += 1;
//        });
//
//        handles.push(handle);
//    }
//
//    for handle in handles {
//        handle.join().unwrap();
//    }
//
//    println!("resut = {}", *counter.lock().unwrap());
//    println!("Hello, world!");
//}
//fn main() {
//    let counter = Mutex::new(0);
//    let mut handles = vec![];
//
//    for _ in 0..10 {
//        let handle = thread::spawn(move || {
//            let mut num = counter.lock().unwrap();
//            *num += 1;
//        });
//
//        handles.push(handle);
//    }
//
//    for handle in handles {
//        handle.join().unwrap();
//    }
//
//    println!("resut = {}", *counter.lock().unwrap());
//    println!("Hello, world!");
//}
