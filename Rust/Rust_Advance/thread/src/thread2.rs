use std::thread;

fn main() {
    let v = vec![1, 2, 3];

//    不能保证v的生命周期存活多久,所以线程必须有v的所有权
    let handle = thread::spawn(move || {
        println!("v: {:?}", v);
    });

    //println!("in main thread, v: {:?}", v);
    handle.join().unwrap();
    println!("Hello, world!");
}

//fn main() {
//    let v = vec![1, 2, 3];
//
//    let handle = thread::spawn(|| {
//        //sleep(10)
//        println!("v: {:?}", v);
//    });
//
//    //drop(v);    //【假设被drop了】
//
//    handle.join().unwrap();
//    println!("Hello, world!");
//}
