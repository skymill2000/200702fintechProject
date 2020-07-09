var fs = require("fs");

console.log("first func");
var readData = "none";
function callbackFunc(callback) {
  fs.readFile("./example/test.txt", "utf8", function (err, result) {
    if (err) {
      console.error(err);
      throw err;
    } else {
      readData = result;
      callback(readData);
    }
  });
}

callbackFunc(function (data) {
  console.log(data);
  console.log("third");
});
