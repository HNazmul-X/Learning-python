// const isPrime = (n)=> {
//     let Factors =[]
//     n.forEach(number => sum = sum+number)


// }

const string = "1234-5";
const forbidden = "-";

console.log([...string].filter((c) => !forbidden.includes(c)).map((c) => parseInt(c)));