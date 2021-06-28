<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>form</title>
</head>
<body>
    <form action="${pageContext.request.contextPath}/user/quick14" method="post">
        <!--表明是第一个User对象的username和age-->
        <input type="text" name="userList[0].username"> <br/>
        <input type="text" name="userList[0].age"> <br/>
        <!--表明是第二个User对象的username和age-->
        <input type="text" name="userList[1].username"> <br/>
        <input type="text" name="userList[1].age"> <br/>
        <!--表明是第三个User对象的username和age-->
        <input type="text" name="userList[2].username"> <br/>
        <input type="text" name="userList[2].age"> <br/>
        <input type="submit" value="提交">
    </form>
</body>
</html>
