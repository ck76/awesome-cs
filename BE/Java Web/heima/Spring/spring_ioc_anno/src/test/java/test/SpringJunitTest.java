package test;

import config.SpringConfiguration;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import service.UserService;

import javax.sql.DataSource;
import java.sql.SQLException;

@RunWith(SpringJUnit4ClassRunner.class)
//@ContextConfiguration("classpath:applicationContext.xml")   //使用注解引入配置文件
@ContextConfiguration(classes = SpringConfiguration.class)  //全注解方式进行配置，导入核心配置类
public class SpringJunitTest {
    @Autowired
    private UserService userService;

    @Autowired
    private DataSource dataSource;

    @Test
    public void test1() throws SQLException {
        userService.save();     //save running...
        System.out.println(dataSource.getConnection());     //com.mchange.v2.c3p0.impl.NewProxyConnection@24aed80c
    }
}
