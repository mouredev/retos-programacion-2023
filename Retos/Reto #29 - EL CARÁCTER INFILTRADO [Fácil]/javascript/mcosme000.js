const diff = (str1, str2) => {
  if (str1.length !== str2.length) {
    return "Different lenght"
  }
  arr = []
  for(let i = 0; i <= str1.length; i++) {
    str1[i] !== str2[i] ? arr.push(str2[i]) : ''
  }
  return arr
}

console.log(diff("maria", "nario"))
