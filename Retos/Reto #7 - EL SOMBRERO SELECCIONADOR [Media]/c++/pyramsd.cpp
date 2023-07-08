#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main() {
    unordered_map<char, string> casas = {
        {'a', "Gryffindor"},
        {'b', "Hufflepuff"},
        {'c', "Slytherin"},
        {'d', "Ravenclaw"}
    };

    vector<unordered_map<string, vector<string>>> preguntas_y_alternativas = {
        {
            {"pregunta", {"1. ¿Cuál de las siguientes opciones odiaría más que la gente lo llamara?"}},
            {"alternativas", {"a) Cobarte", "b) Egoísta", "c) Ordinario", "d) Ignorante"}}
        },
        {
            {"pregunta", {"2. Después de su muerte ¿qué es lo que más le gustaría que hiciera la gente cuando escuche su nombre?"}},
            {"alternativas", {"a) Pide mas historias sobre tus aventuras", "b) Te extraña, pero sonríe", "c) Piensa con admiración tus logros", "d) No me importa lo que la gente piense de mí después de mi muerte, es lo que piensan de mi mientras estoy vivo lo que cuenta"}}
        },
        {
            {"pregunta", {"3. Dada la opción, preferirías inventar una poción que garantizara:"}},
            {"alternativas", {"a) Gloria", "b) Amor", "c) Poder", "d) Sabiduría"}}
        },
        {
            {"pregunta", {"4. ¿Cómo le gustaría ser conocido en la historia?"}},
            {"alternativas", {"a) El gran", "b) El bueno", "c) El audaz", "d) El sabio"}}
        },
        {
            {"pregunta", {"5. Tú y dos amigos deben cruzar un puente custodiado por un troll de río que insiste en luchar contra uno de ustedes antes de que los deje pasar a todos. Tú:"}},
            {"alternativas", {"a) ¿Sugiere que los tres deben luchar? (sin decírselo al troll)", "b) Te ofreces como voluntario", "c) ¿Intentas confundir al troll para que te deje pasar a los tres sin luchar?", "d) Sugerir sorteo para decidir quién de ustedes peleará"}}
        }
    };

    unordered_map<char, int> pnts{
        {'a', 0},
        {'b', 0},
        {'c', 0},
        {'d', 0}
    };

    cout << "\t\t\t\t\t\tBienvenido a Hogwarts!" << endl;
    cout << "\t\t\t\t\t\t---------------------" << endl;
    cout << "El sombrero seleccionador se encargará de seleccionar tu casa de Hogwarts" << endl;
    cout << "--------------------------------------------------------------------------";

    bool r_valida = false;

    while (!r_valida)
    {
        try{
            for (const auto& pregunta : preguntas_y_alternativas) {
                const string& texto_pregunta = pregunta.at("pregunta").at(0);
                cout << endl << texto_pregunta << endl;
    
                const vector<string>& alternativas = pregunta.at("alternativas");
                for (const string& alternativa : alternativas){
                    cout << alternativa << endl;
                }

                char r;
                cout << "Respuesta (a, b, c, d): ";
                cin >> r;
                r = tolower(r);
            
                if (pnts.find(r) == pnts.end()){
                    throw invalid_argument("Alternativa no válida");
                }
                pnts[r]++;
            }

            r_valida = true;

        }catch (const exception& e){
            cout << "Intentelo de nuevo" << endl;
            
        }
    }

    char max_pnts = max_element(pnts.begin(), pnts.end(), [](const pair<char, int>& a, const pair<char, int>& b) {
        return a.second < b.second;
    })->first;

    string casa_final = casas[max_pnts];
    cout << endl << "Eres " << casa_final << "!" << endl;

};
