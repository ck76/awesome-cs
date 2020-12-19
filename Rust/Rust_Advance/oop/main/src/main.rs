use getaver;

fn main() {
    gui();
}

fn aver() {
    //    使用AverCollect的时候希望带上前面的一层又便于区分
    let mut a = getaver::AverCollect::new();

    a.add(1);
    println!("average = {}", a.average());

    a.add(2);
    println!("average = {}", a.average());

    a.add(3);
    println!("average = {}", a.average());

    a.remove();
    println!("average = {}", a.average());

}

use gui::{Screen, Button, SelectBox};

fn gui() {
    let s = Screen {
        components: vec![
            Box::new(Button {
                width: 50,
                height: 10,
                label: String::from("ok"),
            }),
            Box::new(SelectBox {
                width: 60,
                height: 40,
                option: vec![
                    String::from("Yes"),
                    String::from("No"),
                    String::from("MayBe"),
                ],
            }),
        ],
    };

    //let s = Screen {
    //    components: vec![
    //        Button {
    //            width: 50,
    //            height: 10,
    //            label: String::from("ok"),
    //        },
    //        SelectBox {
    //            width: 60,
    //            height: 40,
    //            option: vec![
    //                String::from("Yes"),
    //                String::from("No"),
    //                String::from("MayBe"),
    //            ],
    //        },
    //    ],
    //};

    s.run();
}
