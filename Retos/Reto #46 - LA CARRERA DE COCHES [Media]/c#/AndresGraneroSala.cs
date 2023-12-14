/*
 *Este script está hecho para unity el proyecto completo está en https://github.com/AndresGraneroSala/retos-semanales-mouredev
 */

using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class Race : MonoBehaviour
{
    [SerializeField] private InputField input;
    [SerializeField] private string[] possibleBets;

    [SerializeField] private GameObject prefabText;
    [SerializeField] private Transform content;

    [SerializeField] private string carBlue, carRed, finish, tree,crash;

    [SerializeField] private int raceLength;

    
    
    
    public void SubmitBet()
    {
        string bet = input.text;

        input.text = "";

        GameObject race = Instantiate(prefabText,content);

        race.GetComponent<TextMeshProUGUI>().SetText( possibleBets.Contains(bet) ? "Brum Brum Brum..." : "<color=red> Error syntax </color>");
        
        if (possibleBets.Contains(bet))
        {
            StartCoroutine(Racing(race.GetComponent<TextMeshProUGUI>(), bet));
        }
    }



    IEnumerator Racing(TextMeshProUGUI textRace, string bet)
    {
        char[] line1 = InitRoad('0');
        char[] line2 = InitRoad('1');

        textRace.SetText($"{ConvertEmojis(new string(line1))}\n{ConvertEmojis(new string(line2))}");

        while (Winner(line1,line2)=="none")
        {
            yield return new WaitForSeconds(1);
            line1 = MoveCar(line1, '0');
            line2 = MoveCar(line2, '1');
            textRace.SetText($"{ConvertEmojis(new string(line1))}\n{ConvertEmojis(new string(line2))}");
        }

        textRace.text += $"\n The winner is... {Winner(line1,line2)}";
        textRace.text += isLucky(bet,Winner(line1,line2))? "\n <color=yellow>You are right, you are lucky. </color>":"\n Better luck next time.";


        yield return null;
        

    }


    char[] MoveCar(char[] race, char car)
        {
            char[] moveCar = race;
            int movements = Random.Range(1, 4);
            int posCar = new string(race).IndexOf(car);
            int posCrash = new string(race).IndexOf('4');

            if (posCrash != -1)
            {
                moveCar[posCrash] = car;
                return moveCar;
            }

            if (posCar - movements <= 0)
            {
                race[posCar] = '_';
                race[0] = car;
                return race;
            }

            moveCar[posCar] = '_';

            if (moveCar[posCar - movements]=='3')
            {
                moveCar[posCar - movements] = '4';
            }
            else
            {
                moveCar[posCar - movements] = car;
            }

            return moveCar;
        }

    char[] InitRoad(char car)
    {
        char[] road = new char[raceLength + 2];

        for (int i = 0; i < road.Length; i++)
        {
            if (i == 0)
            {
                road[i] = '2';
                continue;
            }

            if (i == road.Length - 1)
            {
                road[i] = car;
                continue;
            }
            
            if (Random.Range(0, 10) == 0)
            {
                road[i] = '3';
            }
            else
            {
                road[i] = '_';
            }
        }

        return road;
    }

    string Winner(char[] line1, char[] line2)
    {
        bool win1= line1[0]=='0';
        bool win2=line2[0] == '1';

        if (win1&& win2)
        {
            return "both cars";
        }
        
        if (win1)
        {
            return "blue car";
        }
        
        if (win2)
        {
            return "red car";

        }

        return "none";
    }


    string ConvertEmojis(string race)
    {
        string raceWithEmojis=race;

        raceWithEmojis = raceWithEmojis.Replace("0", carBlue);
        raceWithEmojis = raceWithEmojis.Replace("1", carRed);
        raceWithEmojis = raceWithEmojis.Replace("2", finish);
        raceWithEmojis = raceWithEmojis.Replace("3", tree);
        raceWithEmojis = raceWithEmojis.Replace("4", crash);

        return raceWithEmojis;
    }

    public bool isLucky(string myBet,string betResult)
    {
        if ((betResult == "both cars"&& myBet=="both"
            )||(betResult == "blue car"&& myBet=="car-blue")||
            (betResult == "red car"&& myBet=="car-red"))
        {
            return true;
        }

        return false;
    }
    
    
}
