function friday13(month,year) {
    // Crear un objeto Date con el mes y año indicados
    const fecha = new Date(year, month - 1, 13);
    
    // Verificar si el día de la semana es viernes (5 es el número que representa el viernes en JavaScript)
    if (fecha.getDay() === 5) {
      return true;
    } else {
      return false;
    }
  }

console.log(friday13(1,2023)) // true
console.log(friday13(2,2023)) // false
console.log(friday13(3,2022)) // false
console.log(friday13(3,2020)) // true
console.log(friday13(10,2023)) // true
console.log(friday13(8,2023)) // false
console.log(friday13(9,2024)) // true