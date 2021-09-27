package demo;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.context.support.FileSystemXmlApplicationContext;
import service.UserService;
import service.impl.UserServiceImpl;

public class UserController {
    public static void main(String[] args) {
//        ApplicationContext app = new FileSystemXmlApplicationContext("F:\\Java\\Project\\Spring\\spring_ioc\\src\\main\\resources\\applicationContext.xml");
        ApplicationContext app = new ClassPathXmlApplicationContext("applicationContext.xml");
//        UserService userService = (UserService) app.getBean("userService");
        UserService userService = app.getBean(UserService.class);
        userService.save();


//        UserService userService = new UserServiceImpl();
//        userService.save(); //NullPointerException
    }
}
