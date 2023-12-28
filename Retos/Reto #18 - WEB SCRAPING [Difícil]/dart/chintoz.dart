import 'package:html/dom.dart';
import 'package:html/parser.dart';
import 'package:http/http.dart' as http;

Future<void> main(List<String> arguments) async {
  var url = Uri.https('holamundo.day');
  var response = await http.get(url);
  var document = parse(response.body);

  var h1Elements = document.getElementsByTagName("h1");
  Element? holaMundoDayH1Element;
  for (var h1Element in h1Elements) {
    if (h1Element.text.contains('Agenda 8 de mayo')) {
       holaMundoDayH1Element = h1Element;
       break;
    }
  }
  Element? blockQuote = holaMundoDayH1Element!.nextElementSibling;
  while (blockQuote!.attributes['class']!.contains('BlockquoteElement___StyledBlockquote-sc-1dtx4ci-0 slate-BlockquoteElement')) {
    print(blockQuote.text);
    blockQuote = blockQuote.nextElementSibling;
  }
}
