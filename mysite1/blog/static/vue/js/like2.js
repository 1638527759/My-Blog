// VTTCue.createApp({
//     data() {
//         return {
//             goal: [],

//         }
//     }
// }).mount('.content')


// var string = "Fuck Konami";
// var array = string.split("");
// // window.alert("?????");
// var submenus = new array("首页", "系统", "教务", "科研", "人事")
// var a1 = new array("a", "b", "c")
// var a2 = new array("x", "y", "z")
// submenus[0] = [0]
// for (i in submenus) {
//     document.write(submenus[i] + "<br/>")
// }
// document.write(string);

// alert("?????")
// var num = "????";

// document.write(num == NaN)

// document.write(1 + '1')
// document.write(8 % '3')
// document.write('1' + '1')
// document.write('4' - 2)


// var m = parseInt(prompt("请输入一个整数"));
// var n = parseInt(prompt("请再次输入一个整数"));
// var myfun = function(x, y) {
//     return x * y;
// }
// var myfun2 = function(x) {
//     y = n;
//     return x * y;
// }
// document.write("the value of myfun is:" + myfun(m, n) + "</br>");
// document.write("the value of myfun2 is:" + myfun2(m, n));

// function fn() {
//     var a = 1;
// }
// document.write(a);

// function test1(Func, str) {
//     test2("就爱学习")
// }

// function test2(data) {
//     document.write(data);
// }
// test1(test2);


// var m = parseInt(prompt("请输入一个整数"));
// var n = parseInt(prompt("请再次输入一个整数"));
// //使用变量初始化函数，即匿名函数
// var myfun = function(x, y) { return x * y; }
// var myfun2 = function(x) { var y = n; return x * y; }

// document.write("the value of myfun is:" + myfun(m, n) + "</br>");
// document.write("the value of myfun2 is:" + myfun2(m, n));

// var row = parseInt(prompt(" 请设置表格的行数 "));
// var col = parseInt(prompt(" 请输入表格的列数 "));
// createTable(row, col);
// function createTable(row, col) {
//     var table = document.createElement('table');
//     for (var i = 0; i < row; i++) {
//         var trs = document.createElement('tr');
//         table.appendChild(trs);
//         for (var j = 0; j < col; j++) {
//             var tds = document.createElement('td');
//             var tdwidth = document.createAttribute("width");
//             var tdheight = document.createAttribute("height");
//             tds.innerHTML = (Math.floor(Math.random() * (100 - 0)) + min);
//             tdwidth.value = "160px";
//             tdheight.value = "40px";
//             trs.appendChild(tds);
//         }
//     }
//     document.body.appendChild(table);
// }

alert("????");
var para = document.createElement("p");
var nide = document.createTextNode("这是一个新段落");
para.appendChild(node);
var attr = document.createAttribute("class");
attr.value = "p1";
para.setAttribute(attr);
document.body, appendChild(para);