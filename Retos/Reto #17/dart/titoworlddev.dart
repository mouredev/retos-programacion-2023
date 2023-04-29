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

import 'package:http/http.dart' as http;
import 'dart:convert';

const URL = 'https://api.github.com';
const USER = 'mouredev';
const REPO = 'retos-programacion-2023';

void main() async {
  print(await http
      .get(Uri.parse('$URL/repos/$USER/$REPO/commits?per_page=10'))
      .then((res) => jsonDecode(res.body)));
}
