const request = require("request");
var parseString = require("xml2js").parseString;

var url =
  // "http://newsapi.org/v2/top-headlines?" +
  // "country=kr&" +
  // "apiKey=78bc6ddd8cdb48ceac76f5f9b9dfc4c5";
  "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnld=109";
request(url, function (error, response, body) {
  parseString(body, function (err, result) {
    console.dir(result.rss.channel[0].item[0].description[0].header[0].wf[0]);
  });
});
