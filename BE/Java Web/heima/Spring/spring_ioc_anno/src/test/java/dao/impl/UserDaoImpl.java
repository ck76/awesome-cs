package dao.impl;

import dao.UserDao;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;

//<bean id="userDao" class="dao.impl.UserDaoImpl"></bean>
//@Component("userDao")   //值相当于id
@Repository("userDao")  //表示dao层，可读性更强
public class UserDaoImpl implements UserDao {
    public void save() {
        System.out.println("save running...");
    }
}
