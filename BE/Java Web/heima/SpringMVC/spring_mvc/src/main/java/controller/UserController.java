
package controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import domain.User;
import domain.VO;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.File;
import java.io.IOException;
import java.util.Arrays;
import java.util.Date;
import java.util.List;

//控制器类
@Controller
@RequestMapping("/user")
public class UserController {

    //请求地址 http://localhost:8080/user/quick?username=xxx
    //请求映射
    @RequestMapping(value = "/quick", method = RequestMethod.GET, params = {"username"})
    public String save() {
        System.out.println("Controller save running...");
        return "success";   //默认为jsp的名字
    }

    @RequestMapping(value = "/quick2")
    public ModelAndView save2() {
        /**
         * Model：模型 作用封装数据
         * View：视图 作用展示数据
         * */
        ModelAndView modelAndView = new ModelAndView();
        //设置模型数据
        modelAndView.addObject("username", "test");
        //设置视图名称
        modelAndView.setViewName("success");
        return modelAndView;
    }

    //SpringMVC可以对方法的参数进行注入，可以在内部直接使用
    @RequestMapping(value = "/quick3")
    public ModelAndView save3(ModelAndView modelAndView) {
        //设置模型数据
        modelAndView.addObject("username", "test?!");
        //设置视图名称
        modelAndView.setViewName("success");
        return modelAndView;
    }

    //类似形式1
    @RequestMapping(value = "/quick4")
    public String save4(Model model) {
        model.addAttribute("username", "test!!!");
        return "success";
    }

    @RequestMapping(value = "/quick5")
    public String save5(HttpServletRequest request) {
        request.setAttribute("username", "test???");
        return "success";
    }

    //写回数据 通过SpringMVC框架注入的response对象，使用response.getWriter().print
    @RequestMapping(value = "/quick6")
    public void save6(HttpServletResponse response) throws IOException {
        response.getWriter().print("hello test");
    }

    //写回数据
    //通过@ResponseBody注解告知SpringMVC框架，方法返回的字符串不是跳转是直接在http响应体中返回
    @ResponseBody   //告知SpringMVC不进行视图跳转，直接进行数据响应
    @RequestMapping(value = "/quick7")
    public String save7() {
        return "hello test";
    }

    //写回json格式字符串
    @ResponseBody
    @RequestMapping(value = "/quick8")
    public String save8() {
        return "{\"username\":\"zhangsan\",\"age\":18}";
    }

    //写回json格式字符串
    @ResponseBody
    @RequestMapping(value = "/quick9")
    public String save9() throws Exception {
        User user = new User();
        user.setUsername("lisi");
        user.setAge(30);
        //使用json转换工具，将对象转换成json格式字符串再返回
        ObjectMapper objectMapper = new ObjectMapper();
        String json = objectMapper.writeValueAsString(user);
        //{"username":"lisi","age":30}
        return json;
    }

    /**
     * 返回对象或集合
     * 期望SpringMVC自动将User转换成json格式的字符串
     */
    @ResponseBody
    @RequestMapping(value = "/quick10")
    public User save10() throws Exception {
        User user = new User();
        user.setUsername("lisi");
        user.setAge(45);

        return user;    //{"username":"lisi","age":45}
    }

    //请求：http://localhost:8080/user/quick11?username=zhangsan&age=18
    //获取请求参数
    @ResponseBody   //带上，表示不进行页面跳转
    @RequestMapping(value = "/quick11")
    public void save11(String username, int age) {
        System.out.println(username);   //zhangsan
        System.out.println(age);        //18
    }

    //请求：http://localhost:8080/user/quick12?username=zhangsan&age=19
    //获取请求参数
    @ResponseBody   //带上，表示不进行页面跳转
    @RequestMapping(value = "/quick12")
    public void save12(User user) {
        System.out.println(user);   //User{username='zhangsan', age=19}
    }

    //请求：http://localhost:8080/user/quick13?strs=aaa&strs=bbb&strs=ccc
    //获取请求参数
    @ResponseBody   //带上，表示不进行页面跳转
    @RequestMapping(value = "/quick13")
    public void save13(String[] strs) {
        System.out.println(Arrays.asList(strs));    //[aaa, bbb, ccc]
    }

    //请求：http://localhost:8080/form.jsp
    //获取请求参数
    @ResponseBody   //带上，表示不进行页面跳转
    @RequestMapping(value = "/quick14")
    public void save14(VO vo) {
        System.out.println(vo); //根据表单提交内容输出
        //VO{userList=[User{username='zhangsan', age=18}, User{username='lisi', age=20}, User{username='wangwu', age=25}]}
    }

    //请求：http://localhost:8080/ajax.jsp
    //获取请求参数
    @ResponseBody   //带上，表示不进行页面跳转
    @RequestMapping(value = "/quick15")
    public void save15(@RequestBody List<User> userList) {
        System.out.println(userList);   //[User{username='zhangsan', age=18}, User{username='lisi', age=28}]
    }

    //请求：http://localhost:8080/user/quick16?name=zhangsan
    //获取请求参数
    @ResponseBody   //带上，表示不进行页面跳转
    @RequestMapping(value = "/quick16")
    public void save16(@RequestParam(value = "name", required = false, defaultValue = "test") String username) {
        System.out.println(username);   //zhangsan，没有注解的话是null
        /*
         * 若此时连接为http://localhost:8080/user/quick16?username=zhangsan
         * 则输出为默认值 test
         * */
    }

    //请求：http://localhost:8080/user/quick17/zhangsan
    //获取请求参数
    @ResponseBody   //带上，表示不进行页面跳转
    @RequestMapping(value = "/quick17/{name}")
    public void save17(@PathVariable(value = "name", required = true) String name) {
        System.out.println(name);   //zhangsan
    }

    //请求：http://localhost:8080/user/quick18?date=2020-12-21
    //获取请求参数
    @ResponseBody   //带上，表示不进行页面跳转
    @RequestMapping(value = "/quick18")
    public void save18(Date date) {
        System.out.println(date);   //Mon Dec 21 00:00:00 CST 2020
    }

    //请求：http://localhost:8080/user/quick19
    //获取请求参数
    @ResponseBody   //带上，表示不进行页面跳转
    @RequestMapping(value = "/quick19")
    public void save19(HttpServletRequest request, HttpServletResponse response, HttpSession session) {
        System.out.println(request);    //org.apache.catalina.connector.RequestFacade@3b177b4b
        System.out.println(response);   //org.apache.catalina.connector.ResponseFacade@3acb6d1
        System.out.println(session);    //org.apache.catalina.session.StandardSessionFacade@4c38d4ca
    }

    //请求：http://localhost:8080/user/quick20
    //获取请求参数
    @ResponseBody   //带上，表示不进行页面跳转
    @RequestMapping(value = "/quick20")
    public void save20(@RequestHeader(value = "User-Agent", required = false) String user_agent) {
        System.out.println(user_agent);
        //Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
    }

    //请求：http://localhost:8080/user/quick21
    //获取请求参数
    @ResponseBody   //带上，表示不进行页面跳转
    @RequestMapping(value = "/quick21")
    public void save21(@CookieValue(value = "JSESSIONID", required = false) String jsessionId) {
        System.out.println(jsessionId); //553D8B2168B88FC0943F629469DF95C5
    }

    //请求：http://localhost:8080/upload.jsp
    //获取请求参数
    @ResponseBody   //带上，表示不进行页面跳转
    @RequestMapping(value = "/quick22")
    public void save22(String username, MultipartFile uploadFile, MultipartFile uploadFile2) throws IOException {
        //注意：参数名称要与表单name一致
        System.out.println(username);   //zhangsan
        System.out.println(uploadFile); //org.springframework.web.multipart.commons.CommonsMultipartFile@4f648ed3
        //获得上传文件的名称
        String originalFilename = uploadFile.getOriginalFilename();
        uploadFile.transferTo(new File("F:\\java\\upload\\" + originalFilename));
        String originalFilename2 = uploadFile2.getOriginalFilename();
        uploadFile.transferTo(new File("F:\\java\\upload\\" + originalFilename2));
    }

    //请求：http://localhost:8080/upload.jsp
    //获取请求参数
    @ResponseBody   //带上，表示不进行页面跳转
    @RequestMapping(value = "/quick23")
    public void save23(String username, MultipartFile[] uploadFile) throws IOException {
        //注意：参数名称要与表单name一致
        System.out.println(username);   //zhangsan
        for (MultipartFile file : uploadFile) {
            String originalFilename = file.getOriginalFilename();
            file.transferTo(new File("F:\\java\\upload\\" + originalFilename));
        }
    }
}
