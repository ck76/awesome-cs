// TODO trait_bound语法

//TODO 指定多个trait_bound

//TODO 返回trait的类型

//fn print_information2<T: GetInfromation>(item: &impl GetInformation) {
//    println!("{},{}", item.get_name(), item.get_age());
//}

trait GetName {
    fn get_name(&self) -> String;
}

trait GetAge {
    fn get_age(&self) -> u32;
}

struct Ck {}

impl GetName for Ck {
    fn get_name(&self) -> String {
        String::from("ccc")
    }
}

impl GetAge for Ck {
    fn get_age(&self) -> u32 {
        100
    }
}

trait GetBABA {
    fn get_baba();
}

fn print_hhhh<T: GetAge + GetName>(item: T) {}

fn print_hhhh2<T>(item: T) where T: GetName + GetAge {}

//返回值要求实现特征

fn return_with_trait() -> impl GetAge + GetName {
    Ck {}
//    如果有CK1和Ck2都实现了trait，也不能通过if else 返回不同的类
}
