const fibonacci = (n) => {
    if (n===1){
        return 4
    } else if( n==2){
        return 3
    } else {
        return fibonacci(n-1)+fibonacci(n-2) 
    }
}

console.log(fibonacci(9))



//                                                                                                     fibonacci(9-1)+fibonacci(9-2)




//                                                                                   fibonacci(8-1)+fibonacci(8-2)  + fibonacci(7-1)+fibonacci(7-2)






//                                                            fibonacci(7-1)+fibonacci(7-2)  + fibonacci(6-1)+fibonacci(6-2) + fibonacci(6-1)+fibonacci(6-2)  + fibonacci(5-1)+fibonacci(5-2)






// fibonacci(6-1)+fibonacci(6-2)  + fibonacci(5-1)+fibonacci(5-2) + fibonacci(4-1)+fibonacci(5-2)  + fibonacci(4-1)+fibonacci(4-2) fibonacci(5-1)+fibonacci(5-2)  + fibonacci(6-1)+fibonacci(6-2) + fibonacci(6-1)+fibonacci(6-2)  + fibonacci(5-1)+fibonacci(5-2)