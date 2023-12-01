function ask() {
  process.stdout.write(
    "Ingresa el número del cual deseas conocer su tabla de multiplicar: \n"
  );
}

function getMultiplicationTable(userNumber) {
  let answers = "";

  for (let index = 1; index <= 10; index++) {    
    answers += `${userNumber} X ${index} = ${userNumber * index} \n`;
  }

  return answers;
}

process.stdin.on("data", (data) => {
  try {
    let userNumber = parseFloat(data.toString().trim());

    if (isNaN(userNumber)) {
      console.log("Debes ingresar un valor numérico");
      process.exit();
    }

    console.log(
      `\n-----------TABLA DE MULTIPLICAR DEL NÚMERO ${userNumber}-----------\n`
    );
    console.log(getMultiplicationTable(userNumber));
    process.exit();
  } catch (error) {
    console.error(error);
    process.exit();
  }
});

ask();
