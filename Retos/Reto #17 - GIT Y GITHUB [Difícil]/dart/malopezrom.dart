import 'dart:convert';
import 'package:http/http.dart' as http;


/**
 * Interface que representa un commit de GitHub
 */
class Commit {
  final String sha;
  final CommitDetails commit;

  Commit({required this.sha, required this.commit});

  factory Commit.fromJson(Map<String, dynamic> json) {
    return Commit(
      sha: json['sha'],
      commit: CommitDetails.fromJson(json['commit']),
    );
  }
}

/**
 * Interface que representa el detalle de un commit de GitHub
 */
class CommitDetails {
  final Author author;
  final String message;

  CommitDetails({required this.author, required this.message});

  factory CommitDetails.fromJson(Map<String, dynamic> json) {
    return CommitDetails(
      author: Author.fromJson(json['author']),
      message: json['message'],
    );
  }
}

/**
 * Interface que representa el autor de un commit de GitHub
 */
class Author {
  final String name;
  final String date;
  final String email;

  Author({required this.name, required this.date, required this.email});

  factory Author.fromJson(Map<String, dynamic> json) {
    return Author(
      name: json['name'],
      date: json['date'],
      email: json['email'],
    );
  }
}


/**
 * Clase que representa un cliente de GitHub
 */
class GitHub{
  final String repositoryName;
  final String GIT_API_URL = 'https://api.github.com/repos/';
  GitHub({required this.repositoryName});


  Future<List<Commit>> readCommits(int commits) async {
    final url = '$GIT_API_URL$repositoryName/commits?per_page=$commits';
    final response = await http.get(Uri.parse(url));
    final data = jsonDecode(response.body) as List<dynamic>;
    return data.map((commitJson) => Commit.fromJson(commitJson)).toList();
  }
  void printCommits(List<Commit> commits) {
    for (var i = 0; i < commits.length; i++) {
      final hash = commits[i].sha.substring(0, 7);
      final name = commits[i].commit.author.name;
      final msg = commits[i].commit.message;
      final date = DateTime.parse(commits[i].commit.author.date);
      print('${'Commit ${i + 1}'} | '
          '${hash} | '
          '${name} | '
          '${msg} | '
          '${date.toLocal().toString()} |');
    }
  }

}

/**
 * Función principal
 */
void main() async {
  final String repositoryName = 'mouredev/retos-programacion-2023';
  final github = GitHub(repositoryName: repositoryName);
  final commits = await github.readCommits(10);
  github.printCommits(commits);
}