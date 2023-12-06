const excel = (column) => {
  const alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
  if (column.length > 1) {
    let as_value = (column.slice(1).length) * 26
    let first_value = alphabet.indexOf(column[0]) + 1
    return first_value + as_value
  }
  return alphabet.indexOf(column) + 1
}

excel("A")
excel("Z")
excel("AA")
excel("CA")
excel("CAA")
