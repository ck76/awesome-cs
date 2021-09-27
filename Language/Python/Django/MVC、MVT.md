# Django 简介

### 基本介绍

Django 是一个由 Python 编写的一个开放源代码的 Web 应用框架。

使用 Django，只要很少的代码，Python 的程序开发人员就可以轻松地完成一个正式网站所需要的大部分内容，并进一步开发出全功能的 Web 服务 Django 本身基于 MVC 模型，即 Model（模型）+ View（视图）+ Controller（控制器）设计模式，MVC 模式使后续对程序的修改和扩展简化，并且使程序某一部分的重复利用成为可能。

MVC 优势：

- 低耦合
- 开发快捷
- 部署方便
- 可重用性高
- 维护成本低
- ...

Python 加 Django 是快速开发、设计、部署网站的最佳组合。

### 特点

- 强大的数据库功能
- 自带强大的后台功能
- 优雅的网址

------

## MVC 与 MTV模型

### MVC 模型

MVC 模式（Model–view–controller）是软件工程中的一种软件架构模式，把软件系统分为三个基本部分：模型（Model）、视图（View）和控制器（Controller）。

MVC 以一种插件式的、松耦合的方式连接在一起。

- 模型（M）- 编写程序应有的功能，负责业务对象与数据库的映射(ORM)。
- 视图（V）- 图形界面，负责与用户的交互(页面)。
- 控制器（C）- 负责转发请求，对请求进行处理。

简易图：

![img](https://www.runoob.com/wp-content/uploads/2020/05/ModelViewControllerDiagramZh.png)

用户操作流程图：

![img](https://tva1.sinaimg.cn/large/008eGmZEly1gn10q3k8pyj30co0bj3zm.jpg)

------

## MTV 模型

Django 的 MTV 模式本质上和 MVC 是一样的，也是为了各组件间保持松耦合关系，只是定义上有些许不同，Django 的 MTV 分别是指：

- M 表示模型（Model）：编写程序应有的功能，负责业务对象与数据库的映射(ORM)。
- T 表示模板 (Template)：负责如何把页面(html)展示给用户。
- V 表示视图（View）：负责业务逻辑，并在适当时候调用 Model和 Template。

除了以上三层之外，还需要一个 URL 分发器，它的作用是将一个个 URL 的页面请求分发给不同的 View 处理，View 再调用相应的 Model 和 Template，MTV 的响应模式如下所示：

简易图：

![img](https://tva1.sinaimg.cn/large/008eGmZEly1gn10q22aslj30ds0agmx6.jpg)

用户操作流程图：

![img](https://tva1.sinaimg.cn/large/008eGmZEly1gn10q5i3m7j30ol0anac4.jpg)

**解析：**

用户通过浏览器向我们的服务器发起一个请求(request)，这个请求会去访问视图函数：

- a.如果不涉及到数据调用，那么这个时候视图函数直接返回一个模板也就是一个网页给用户。
- b.如果涉及到数据调用，那么视图函数调用模型，模型去数据库查找数据，然后逐级返回。

视图函数把返回的数据填充到模板中空格中，最后返回网页给用户。

> 参考地址：
>
> [1]: https://www.cnblogs.com/liuhui0308/p/12189658.html



### 目录说明：

- **HelloWorld:** 项目的容器。
- **manage.py:** 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
- **HelloWorld/__init__.py:** 一个空文件，告诉 Python 该目录是一个 Python 包。
- **HelloWorld/asgi.py:** 一个 ASGI 兼容的 Web 服务器的入口，以便运行你的项目。
- **HelloWorld/settings.py:** 该 Django 项目的设置/配置。
- **HelloWorld/urls.py:** 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
- **HelloWorld/wsgi.py:** 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。

接下来我们进入 HelloWorld 目录输入以下命令，启动服务器：

```
python3 manage.py runserver 0.0.0.0:8000
```