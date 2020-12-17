fn main() {
//    定义结构体
//    创建结构体
//    修改结构体字段
//    参数名字和字段名字同名的简写方法


    println!("Hello, world!");

    let mut ck=User{
        name:String::from("cheng kun"),
        age:100,
    };
//    ck.age=200;
//    let age:u32=ck.age;
//    let name=ck.name;

//    let a=User{
//        name:ck.name,
//        age:ck.age,
//    };

    //    从其他结构体创建实例
    let user2=User{
        name:String::from("user2"),
        ..ck
    };
    ck.age;

    //    元祖结构体
    struct Point(u32,u32);
    let a =Point(10,20);
    let b =Point(40,20);


    //    没有任何字段的类单元结构体
    struct Null{};

    //    打印结构体
    println!("{:?}",user2 );
    println!("{:#?}",user2 );

//    结构体方法
    let dog=Dog{
        name:String::from("xiao gou"),
        weight:100.21,
        height:200.9,

    };
    println!("{:#?}",dog);
    Dog::get_name(&dog);
    Dog::wangwang();
}

//自动推导
#[derive(Debug)]
struct User{
    name:String,
    age:u32,
}

#[derive(Debug)]
struct Dog{
    name:String,
    weight:f32,
    height:f32,
}

impl Dog{
    fn get_name(&self) -> &str{
        &(self.name[..])
    }
    fn ge_weight(&self) ->f32{
        self.weight
    }
    fn get_height(&self)-> f32{
        self.height
    }
}

impl Dog{
    fn wangwang(){
        println!("{}","wangwang")

    }
}
