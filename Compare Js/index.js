let myStr = "ABCDEFGHIJKLM";
[...myStr].forEach((item) => console.log(item));
console.log("hello world");
console.log([...myStr]);


const string = "12345";
const forbidden = "-";
myStr = [...string].filter((c) => !forbidden.includes(c)).map((c) => parseInt(c));
console.log(myStr);

myStr = [...string].map(c => c)
console.log(myStr)

console.log(myStr.length>2?true:false)