//mod factory {
//    pub mod produce_refrigerator {
//        pub fn produce_re() {
//            println!("produce refrigerator");
//        }
//    }
//
//    mod produce_washing_mechine {
//        fn produce_wash() {
//            println!("produce washing mechine");
//        }
//    }
//}

pub mod produce_refrigerator {
    pub fn produce_re() {
        println!("produce refrigerator");
    }
}

pub mod produce_washing_mechine {
    pub fn produce_wash() {
        println!("produce washing mechine");
    }
}


pub mod modA {
    #[derive(Debug)]
    pub struct A {
        pub number: i32,
        pub name: String,
    }

    impl A {
        pub fn new_a() -> A {
            A {
                number: 1,
                name: String::from("cheng kun"),
            }
        }

        pub fn print_a(&self) {
            println!("number: {}, name: {}", self.number, self.name);
        }
    }

    pub mod modB {
        pub fn print_B() {
            println!("b")
        }

        pub mod modC {
            pub fn print_C() {
                println!("C");
                super::print_B();
            }
        }
    }
}
