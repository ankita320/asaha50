function fac(n){
    if (n == 1) {
        return 1;}
    else {
        n*fac(n-1)
}    
}
console.log(fac(3))

function fib(n){
    if (n <== 1) {
        return n;}
    else {
        fib(n-1)+fib(n-2)
}    
}
console.log(fib(3))
