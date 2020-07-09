const express = require("express");
const app = express();

app.set("views", __dirname + "/views");
app.set("view engine", "ejs");

app.get("/", function (req, res) {
  res.send("Hello World");
});

app.get("/hello", function (req, res) {
  res.send("안녕하세요 !");
});

app.get("/htmlTest", function (req, res) {
  res.send("<html><h1>안녕하세요</h1><hr/><p>만들기 어렵습니다</p></html>");
});

app.listen(3000, function () {
  console.log("Example app listening at http://localhost:3000");
});
