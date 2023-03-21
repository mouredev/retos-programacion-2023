/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs:
 * https://github.com/public-apis/public-apis
 */


import 'dart:convert';
import 'package:http/http.dart' as http;
import 'dart:async';

final String API_KEY= 'DEMO_KEY';
final String URL_PHOTOS = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos';
/**
 * Ejemplo de llamada a la API de la NASA para obtener las fotos de Marte del Curiosity
 * filtradas por fecha de la tierra
 * Response:
    2023-03-12 00:00:00.000: https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03767/opgs/edr/fcam/FLB_731921172EDR_F1001084FHAZ00337M_.JPG
    2023-03-12 00:00:00.000: https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03767/opgs/edr/fcam/FRB_731921172EDR_F1001084FHAZ00337M_.JPG
    2023-03-12 00:00:00.000: https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03767/opgs/edr/rcam/RRB_731921206EDR_F1001084RHAZ00337M_.JPG
    2023-03-12 00:00:00.000: https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03767/opgs/edr/rcam/RLB_731921206EDR_F1001084RHAZ00337M_.JPG
 */
void main() async {
  final photos = await getPhotos("2023-03-12");
  photos.forEach((element) {
    print('${element.earthDate}: ${element.imgSrc}');
  });

}




/**
 * Funcion para parsear la URL de la API de la NASA con los parametros de busqueda y el API KEY
 */
Uri _getURLPhotos(String url, String earthDate) {
  String urlString = '$url?earth_date=$earthDate&api_key=$API_KEY';
  return Uri.parse(urlString);
}

/**
 * Funcion para obtener las fotos de Marte del Curiosity filtradas por fecha de la tierra
 * @param earthDate fecha de la tierra
 * @return lista de fotos de Marte
 */
Future<List<MarsPhoto>> getPhotos(String earthDate) async {
  try {
    final response = await http.get(_getURLPhotos(URL_PHOTOS,earthDate));
    if (response.statusCode == 200) {
      final body = jsonDecode(response.body);
      final List<dynamic> photos = body['photos'];
      final List<MarsPhoto> marsPhotos = photos.map((dynamic item) =>
          MarsPhoto.fromJson(item)).toList();
      return marsPhotos;
    }
    else {
      print('Error al obtener las fotos ${response.body}');
      return [];
    }
  } catch (e) {
    print(e);
    return [];
  }
}

/**
 * Clase para parsear la respuesta de la API de la NASA
 * Define el objeto MarsPhotos
 */
class MarsPhoto {
  MarsPhoto({
    required this.id,
    required this.sol,
    required this.camera,
    required this.imgSrc,
    required this.earthDate,
    required this.rover,
  });

  int id;
  int sol;
  Camera camera;
  String imgSrc;
  DateTime earthDate;
  Rover rover;

  factory MarsPhoto.fromJson(Map<String, dynamic> json) => MarsPhoto(
    id: json["id"],
    sol: json["sol"],
    camera: Camera.fromJson(json["camera"]),
    imgSrc: json["img_src"],
    earthDate: DateTime.parse(json["earth_date"]),
    rover: Rover.fromJson(json["rover"]),
  );

  Map<String, dynamic> toJson() => {
    "id": id,
    "sol": sol,
    "camera": camera.toJson(),
    "img_src": imgSrc,
    "earth_date": "${earthDate.year.toString().padLeft(4, '0')}-${earthDate.month.toString().padLeft(2, '0')}-${earthDate.day.toString().padLeft(2, '0')}",
    "rover": rover.toJson(),
  };
}

class Rover {
  Rover({
    required this.id,
    required this.name,
    required this.landingDate,
    required this.launchDate,
    required this.status,
  });

  int id;
  String name;
  DateTime landingDate;
  DateTime launchDate;
  String status;

  factory Rover.fromJson(Map<String, dynamic> json) => Rover(
    id: json["id"],
    name: json["name"],
    landingDate: DateTime.parse(json["landing_date"]),
    launchDate: DateTime.parse(json["launch_date"]),
    status: json["status"],
  );

  Map<String, dynamic> toJson() => {
    "id": id,
    "name": name,
    "landing_date": "${landingDate.year.toString().padLeft(4, '0')}-${landingDate.month.toString().padLeft(2, '0')}-${landingDate.day.toString().padLeft(2, '0')}",
    "launch_date": "${launchDate.year.toString().padLeft(4, '0')}-${launchDate.month.toString().padLeft(2, '0')}-${launchDate.day.toString().padLeft(2, '0')}",
    "status": status,
  };

}


class Camera {
  Camera({
    required this.id,
    required this.name,
    required this.roverId,
    required this.fullName,
  });

  int id;
  String name;
  int roverId;
  String fullName;
  factory Camera.fromJson(Map<String, dynamic> json) => Camera(
    id: json["id"],
    name: json["name"],
    roverId: json["rover_id"],
    fullName: json["full_name"],
  );

  Map<String, dynamic> toJson() => {
    "id": id,
    "name": name,
    "rover_id": roverId,
    "full_name": fullName,
  };
}






