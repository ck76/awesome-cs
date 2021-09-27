package config;

import org.springframework.context.annotation.*;

//标志该类是Spring的核心配置类
@Configuration
//    <!--配置组件扫描-->
//    <context:component-scan base-package="dao service"/>
@ComponentScan({"dao", "service", "config"})    //Spring在初始化容器时要扫描的包
// <import resource="" />
@Import(DataSourceConfiguration.class)
public class SpringConfiguration {



}
