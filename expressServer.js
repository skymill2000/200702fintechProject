const express = require("express");
const app = express();

app.set("views", __dirname + "/views");
app.set("view engine", "ejs");

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use(express.static(__dirname + "/public"));

app.get("/signup", function (req, res) {
  res.render("signup");
});

app.listen(3000, function () {
  console.log("Example app listening at http://localhost:3000");
});
