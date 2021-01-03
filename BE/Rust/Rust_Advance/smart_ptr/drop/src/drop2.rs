struct Dog {
    name: String,
    //count: i32,
}

impl Drop for Dog{
    fn drop(&mut self) {
        println!("Dog {} leave", self.name);
        //self.count -= 1;
    }
}

//rust提供了std::mem::drop()
fn main2() {
    let a = Dog{name: String::from("main2  wangcai")};
    let b = Dog{name: String::from("main2  dahuang")};//先leave
    //b.drop();
    drop(b);
    drop(a);

    println!("0 main2 ++++++++++++++++++++++");
}
