struct Counter {
    count: u32,
}

impl Counter {
    fn new() -> Counter {
        Counter { count: 0 }
    }
}

impl Iterator for Counter {
    //    TODO  type关联类型
    type Item = u32;
    fn next(&mut self) -> Option<Self::Item> {
        self.count += 1;
        if self.count < 6 {
            Some(self.count)
        } else {
            None
        }
    }
}

fn main2() {
    let mut counter = Counter::new();
    for i in (0..6) {
        if let Some(v) = counter.next() {
            println!("i = {}, v = {}", i, v);
        } else {
            println!("i = {}, at end", i);
            break;
        }
    }

    println!("Hello, world!");
}
