import 'dart:convert';

import 'package:http/http.dart' as http;

const baseUrl = "pokeapi.co";
const endpoint = "api/v2/pokemon";

void main() async {
  final pokemons = await getPokemon();
  for (int i = 0; i < pokemons.length; i++) {
    print("${i + 1} - ${pokemons[i].name}");
  }
}

Future<List<Pokemon>> getPokemon() async {
  final url = Uri.https(baseUrl, endpoint, {
    'limit': '100',
  });

  try {
    final response = await http.get(url);
    final body = jsonDecode(response.body);
    final List<dynamic> results = body['results'];
    final List<Pokemon> pokemons = results.map((e) => Pokemon.fromMap(e)).toList();
    return pokemons;
  } catch (e) {
    print(e);
    return [];
  }
}

class Pokemon {
  Pokemon({
    required this.name,
  });

  final String name;

  factory Pokemon.fromMap(Map<String, dynamic> json) => Pokemon(
        name: json["name"],
      );
}
