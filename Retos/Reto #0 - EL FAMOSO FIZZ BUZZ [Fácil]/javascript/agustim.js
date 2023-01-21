for(x = 1;x <= 100;x++){
    let ret = ""
    if (x % 3 === 0) ret += "fizz"
    if (x % 5 === 0) ret += "buzz"
    if (ret === "") ret = x
    console.log(ret)
}