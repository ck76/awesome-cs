var node_description = "简单的说 Node.js 就是运行在服务端的 JavaScript " +
    "Node.js 是一个基于Chrome JavaScript 运行时建立的一个平台 " +
    "Node.js是一个事件驱动I/O服务端JavaScript环境，基于Google的V8引擎，V8引擎执行Javascript的速度非常快，性能非常好。"

var http = require("http");
http.createServer(function (request, response){
    // 发送 HTTP 头部
    // HTTP 状态值: 200 : OK
    // 内容类型: text/plain
    response.writeHead(200, {'Content-Type': 'text/plain'});

    // 发送响应数据 "Hello World"
    response.end('Hello World from chengkun\n');
}).listen(8888);
