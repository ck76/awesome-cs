////1、 trait用于定义与其它类型共享的功能，类似于其它语言中的【接口】。
////(1)可以通过trait以抽象的方式定义【共享的行为】。
////(2)可以使用traitbounds指定泛型是任何拥有特定行为的类型。
////2、 定义trait

include!("trait2.rs");


pub trait GetInformation {
    fn get_name(&self) -> &String;
    fn get_age(&self) -> u32;
    fn get_hahaha() {
        println!("hahahha");
    }
}
////3、 实现trait

pub struct Student {
    pub name: String,
    pub age: u32,
}

//貌似没什么用
impl GetInformation for Student {
    fn get_name(&self) -> &String {
        &self.name
    }

    fn get_age(&self) -> u32 {
        self.age
    }
}

////4、 默认实现:可以在定义trait的时候提供默认的行为，trait的类型可以使用默认的行为。
////5、 trait作为参数【主要是提供约束】
fn print_information(item: &impl GetInformation) {
    println!("{},{}", item.get_name(), item.get_age());
}

fn main() {
    println!("Hello, world!");
    let xiaoming = Student {
        name: String::from("xiaoming"),
        age: 10,
    };

    print_information(&xiaoming);
    println!("{},{}", xiaoming.get_name(), xiaoming.get_age());

    return_with_trait();
}

