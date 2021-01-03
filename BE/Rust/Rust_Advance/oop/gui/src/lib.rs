//TODO 【多态】

pub trait Draw {
    fn draw(&self);
}

pub struct Screen {
    pub components: Vec<Box<dyn Draw>>, //trait对象，使用dyn关键字
}


impl Screen {
    pub fn run(&self) {
        for comp in self.components.iter() {
            comp.draw();
        }
    }
}

// TODO 【为什么不用泛型】
//TODO 【trait动态分发】类似c++的虚指针
//【泛型静态推导一次定型单态化的处理，第一次加Button，第二次加SelectBox当然不行】
//
//pub struct Screen<T: Draw> {
//    pub components: Vec<T>,
//}
//--------------------------------
//impl<T> Screen <T>
//    where T: Draw {
//    pub fn run(&self) {
//        for comp in self.components.iter() {
//            comp.draw();
//        }
//    }
//}

pub struct Button {
    pub width: u32,
    pub height: u32,
    pub label: String,
}

impl Draw for Button {
    fn draw(&self) {
        println!("draw button, width = {}, height = {}, label = {}",
                 self.width, self.height, self.label);
    }
}

pub struct SelectBox {
    pub width: u32,
    pub height: u32,
    pub option: Vec<String>,
}

impl Draw for SelectBox {
    fn draw(&self) {
        println!("draw selectBox, width = {}, height = {}, option = {:?}",
                 self.width, self.height, self.option);
    }
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
