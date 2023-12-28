import 'dart:io';

void main(List<String> args) {
  stdout.writeln("Ingrese la tabla de multiplicar: ");
  FindOut();
}

void FindOut() {
  String? table = stdin.readLineSync();

  if (table == null || table.isEmpty || int.tryParse(table) == null) {
    print("¡¡¡Ingrese un valor correcto!!!");
    FindOut();
  } else {
    Calculetion(table);
  }
}

void Calculetion(String table) {
  print('Estas seria las tablas de multiplicar de $table');
  final numTable = int.tryParse(table)!;

  for (int i = 1; i <= 10; i++) {
    print("$table x $i = ${numTable * i}");
  }
}
