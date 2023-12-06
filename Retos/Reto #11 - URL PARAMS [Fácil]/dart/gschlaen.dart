void main() {
  print(urlParameters(""));
  print(urlParameters("http://example.com"));
  print(urlParameters("https://www.example.com"));
  print(urlParameters("http://example.com?"));
  print(urlParameters("http://example.com?a"));
  print(urlParameters("http://example.com?a="));
  print(urlParameters("http://example.com?a=hello"));
  print(urlParameters("http://example.com?a=hello&"));
  print(urlParameters("http://example.com?a=hello&b"));
  print(urlParameters("http://example.com?a=hello&b="));
  print(urlParameters("http://example.com?a=hello&b=bye"));
  print(urlParameters("http://example.com?a=hello&b&c=hey"));
  print(urlParameters("http://example.com?a=hello&b=&c=hey"));
  print(urlParameters("http://example.com?a=hello&=hey"));
}

urlParameters(String url) {
  final parameters = [];
  List<String> urlSplitted = url.split("&");
  for (String e in urlSplitted) {
    final splitted = e.split("=");
    splitted.remove("");
    if (splitted.length == 2) {
      parameters.add(splitted[1]);
    }
  }
  return parameters;
}
