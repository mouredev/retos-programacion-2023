import 'dart:io';

void main(List<String> args) {
  print("🔢 Tabla de multiplicar 🔢");
  operation();
}

void operation() {
  print("Ingresa algun numero entero");
  String? number = stdin.readLineSync();

  if (number == null || number.isEmpty || int.tryParse(number) == null) {
    print("Porfavor ingresa un formato valido, debe ser un numero entero");
    operation();
  }

  print("La tabla de multiplicar de ${number} es la siguiente:");
  final intNumber = int.tryParse(number!)!;
  for (var i = 1; i <= 10; i++) {
    print("$i x $intNumber = ${i * intNumber}");
  }
}
