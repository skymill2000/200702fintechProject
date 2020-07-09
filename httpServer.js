var http = require("http");

http
  .createServer(function (req, res) {
    var body = "hello Server";
    res.setHeader("Content-Type", "text/html; charset=utf-8");
    res.end(
      "<html><body><h1>Hello Nodejs Server</h1><hr/><h2>내용입니다.</h2></body></html>"
    );
  })
  .listen(3000);
