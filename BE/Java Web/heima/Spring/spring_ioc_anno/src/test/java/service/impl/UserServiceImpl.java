package service.impl;

import dao.UserDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;
import service.UserService;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;
import javax.annotation.Resource;

//<bean id="userService" class="service.impl.UserServiceImpl">
//@Component("userService")   //值相当于id
@Service("userService") //表示service层，可读性更强
//@Scope("prototype")
@Scope("singleton")
public class UserServiceImpl implements UserService {

    @Value("${jdbc.driver}")    //可以读取配置文件
    private String driver;

    //<property name="userDao" ref="userDao"></property>
    //@Autowired  //按照数据类型从Spring容器中进行匹配
    //@Qualifier("userDao")   //按照id值从容器中进行匹配，但是此处要结合@Autowired一起使用
    @Resource(name = "userDao") //相当于@Autowired+@Qualifier，简化写法
    private UserDao userDao;

    public void setUserDao(UserDao userDao) {
        this.userDao = userDao;
    }

    public void save() {
        System.out.println(driver);
        userDao.save();
    }

    @PostConstruct  //构造之后
    public void init() {
        System.out.println("Service对象的初始化方法");
    }

    @PreDestroy     //销毁之前
    public void destroy() {
        System.out.println("Service对象的销毁方法");
    }
}
