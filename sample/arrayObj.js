var car = {
  name: "sonata",
  ph: "500ph",
  start: function () {
    console.log("engine is starting");
  },
  stop: function () {
    console.log("engine is stoped");
  },
};

var car2 = {
  name: "bmw",
  ph: "500ph",
  start: function () {
    console.log("engine is starting");
  },
  stop: function () {
    console.log("engine is stoped");
  },
};

var car3 = {
  name: "fiat",
  ph: "500ph",
  start: function () {
    console.log("engine is starting");
  },
  stop: function () {
    console.log("engine is stoped");
  },
};

var cars = [car, car2, car3];

//#work2 자동차 배열을 확인한 뒤 bmw 라는 자동차가 있으면 hello 출력해주세요 for / if 활용
function findCar(carname) {
  for (var i = 0; i < cars.length; i++) {
    var car = cars[i];
    if (car.name == carname) {
      console.log("find!");
    }
  }
}
findCar("bmw");
