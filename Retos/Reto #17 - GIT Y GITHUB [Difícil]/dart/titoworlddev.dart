/*
 * ¡Estoy de celebración! He publicado mi primer libro:
 * "Git y GitHub desde cero"
 * - Papel: mouredev.com/libro-git
 * - eBook: mouredev.com/ebook-git
 *
 * ¿Sabías que puedes leer información de Git y GitHub desde la gran
 * mayoría de lenguajes de programación?
 *
 * Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
 * - Hash
 * - Autor
 * - Mensaje
 * - Fecha y hora
 *
 * Ejemplo de salida:
 * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 * 
 */

// import 'package:http/http.dart' as http;
import 'dart:io';
import 'dart:convert';

const URL = 'https://api.github.com';
const USER = 'mouredev';
const REPO = 'retos-programacion-2023';

void main() {
  printCommits(10);
}

void printCommits(int commitsLength) async {
  // final data = await http
  //     .get(Uri.parse('$URL/repos/$USER/$REPO/commits'))
  //     .then((res) => jsonDecode(res.body));

  /* Aunque es mas facil con http, dependiendo de como y donde lo ejecutes se 
    puede hacer la peticion con dart:io ya que http necesita 
    un proyecto de dart para instalar las dependencias y poder usarlas 
    pero dart:io no lo necesita */
  final data = await HttpClient()
      .getUrl(Uri.parse('$URL/repos/$USER/$REPO/commits'))
      .then((req) => req.close())
      .then((res) => res.transform(utf8.decoder).join())
      .then((res) => jsonDecode(res));

  for (int i = 1; i <= commitsLength; i++) {
    final hash = data[i]['sha'].substring(0, 7).toUpperCase();
    final commit = data[i]['commit'];
    final name = commit['author']['name'];
    final message = commit['message'];
    final date = DateTime.parse(commit['author']['date']);
    final dateFormated =
        '${date.day}/${date.month}/${date.year} ${date.hour}:${date.minute}';

    print('Commit $i | $hash | $name | $message | $dateFormated\n\n');
  }
}
