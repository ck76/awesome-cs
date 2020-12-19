//TODO 【..】
fn main() {
    let numbers = (1, 2, 3, 4, 5, 6, 7);
    match numbers {
        (first, .., last) => {
//            TODO 输出1、7
            println!("first: {}, last: {}", first, last);
        },
    };

    //TODO 【error】
    //match numbers {
    //    (.., second, ..) => {
    //        println!("{}", second);
    //    },
    //};
    println!("Hello, world!");
}
