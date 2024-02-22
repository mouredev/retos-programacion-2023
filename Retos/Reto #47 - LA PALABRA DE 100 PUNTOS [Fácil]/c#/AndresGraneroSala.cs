using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.Text;
using System;
using System.Globalization;
using System.Text;

/*
 *Este script está hecho para unity el proyecto completo está en https://github.com/AndresGraneroSala/retos-semanales-mouredev
 */


public class ManagerInput : MonoBehaviour
{
    [SerializeField] private InputField input;
    private const  int numA32bit= 97;
    private const  int numÑAlphabet= 15;
    private const int totalLettersInAlphabet=27;

    [SerializeField] private GameObject prefab;
    [SerializeField] private Transform content;

    private void Start()
    {
        GoBackEdit();
    }

    public void SubmitWord()
    {
        if (string.IsNullOrEmpty( input.text)) {return;}
        if (string.IsNullOrWhiteSpace( input.text)) {return;}

        string word = input.text;

        if(input.text==""){return;}
        
        char[] letters = word.Replace(" ","").ToCharArray();

        int points = 0;

        foreach (var letter in letters)
        {
            points += GetPointsLetter(letter);
        }
        
        GameObject textPoints = Instantiate(prefab,content);
        textPoints.GetComponent<Text>().text = $"Points: {points} - Word: {word}";

        if (points==100)
        {
            textPoints.GetComponent<Text>().color= Color.yellow;
        }
        
        
        input.text = "";

    }

    int GetPointsLetter(char letter)
    {
        if (char.ToLower(letter) == 'ñ'){return numÑAlphabet;}

        
        int points = 0;

        char letterClear = letter.ToString().Normalize(NormalizationForm.FormD).ToLower()[0];
        print(letter);

        int letterPos32bit = Convert.ToInt32(char.ToLower(letterClear));

        if (letterPos32bit<numA32bit|| letterPos32bit>numA32bit+26)
        {/*no letter*/ return 0;}
        
        
        bool isUpperÑ = letterPos32bit >= numA32bit + numÑAlphabet - 1;

        points += letterPos32bit - (numA32bit - 1);
        points += isUpperÑ ? 1 : 0;
        return points;
    }

    public void GoBackEdit()
    {
        input.ActivateInputField();
    }
}
