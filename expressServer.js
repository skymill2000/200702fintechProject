const express = require("express");
const app = express();

app.set("views", __dirname + "/views");
app.set("view engine", "ejs");

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use(express.static(__dirname + "/public"));

app.get("/", function (req, res) {
  res.send("Hello World");
});

app.get("/hello", function (req, res) {
  res.send("안녕하세요 !");
});

app.get("/htmlTest", function (req, res) {
  res.send("<html><h1>안녕하세요</h1><hr/><p>만들기 어렵습니다</p></html>");
});

app.get("/ejsTest", function (req, res) {
  res.render("test");
});

app.get("/inputTest", function (req, res) {
  res.render("inputTest");
});

app.get("/designTest", function (req, res) {
  res.render("design");
});

app.post("/getLoginData", function (req, res) {
  var userId = req.body.ajaxUserId;
  var userPassword = req.body.ajaxUserPassword;
  console.log("req body : ", req.body);
  console.log(userId, userPassword);

  res.json(userId + "분의 로그인 성공입니다.");
});

app.listen(3000, function () {
  console.log("Example app listening at http://localhost:3000");
});
