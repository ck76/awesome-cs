package dao.impl;

import dao.UserDao;
import domain.User;

import java.util.List;
import java.util.Map;
import java.util.Properties;

public class UserDaoImpl implements UserDao {
//    private String username;
//    private int age;

    private List<String> strList;
    private Map<String, User> userMap;
    private Properties properties;

//    public void setUsername(String username) {
//        this.username = username;
//    }
//
//    public void setAge(int age) {
//        this.age = age;
//    }

    public List<String> getStrList() {
        return strList;
    }

    public void setStrList(List<String> strList) {
        this.strList = strList;
    }

    public Map<String, User> getUserMap() {
        return userMap;
    }

    public void setUserMap(Map<String, User> userMap) {
        this.userMap = userMap;
    }

    public Properties getProperties() {
        return properties;
    }

    public void setProperties(Properties properties) {
        this.properties = properties;
    }

    /*
    public UserDaoImpl() {
        System.out.println("UserDaoImpl创建...");
    }

    public void init() {
        System.out.println("初始化方法...");
    }

    public void destroy() {
        System.out.println("销毁方法...");
    }
*/

    public void save() {
//        System.out.println(username + "====" + age);
        System.out.println(strList);
        System.out.println(userMap);
        System.out.println(properties);
        System.out.println("save running...");
    }
}
