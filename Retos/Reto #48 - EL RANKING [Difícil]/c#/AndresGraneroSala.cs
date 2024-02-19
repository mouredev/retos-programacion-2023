using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;

/*
 *Este script está hecho para unity el proyecto completo está en https://github.com/AndresGraneroSala/retos-semanales-mouredev
 */
public class ApiManager : MonoBehaviour
{
    private string username = "mouredev";
    private string repoName = "retos-programacion-2023";

    
    private string accessToken = "";

    private string apiUrl => $"https://api.github.com/repos/{username}/{repoName}/commits";


    [SerializeField] private Text textLoading, textNumUsers, textNumCorrections;
    private Dictionary<string,CommitUI> _commits= new Dictionary<string, CommitUI>();

    [SerializeField] private GameObject scroll;
    [SerializeField] private Transform content, contentNonOrdered;

    [SerializeField] private InputField input;

    [SerializeField] private GameObject prefabText;

    private int numCorrections=0;
    
    private void Awake()
    {
        scroll.SetActive(false);
    }


    public void UpdateApiKey()
    {
        if (string.IsNullOrEmpty(input.text))
        {
            return;
        }
        
        accessToken = input.text;
        InitSearchCommits();
    }
    
    public void InitSearchCommits()
    {
        StartCoroutine(GetCommitsCoroutine(apiUrl));
    }

    private IEnumerator GetCommitsCoroutine(string url)
    {
        scroll.SetActive(true);
        
        textLoading.text = "Loading...";
        
        while (!string.IsNullOrEmpty(url))
        {
            using UnityWebRequest webRequest = UnityWebRequest.Get(url);
            webRequest.SetRequestHeader("Authorization", $"Bearer {accessToken}");

            yield return webRequest.SendWebRequest();

            if (webRequest.result == UnityWebRequest.Result.ConnectionError ||
                webRequest.result == UnityWebRequest.Result.ProtocolError)
            {
                Debug.LogError($"Error: {webRequest.error}");
                yield break; 
            }
            else
            {
                
                string json = webRequest.downloadHandler.text;
                Debug.Log(json);
                    
                ExtractMessageFromJson(json);

                // Verify next page
                string linkHeader = webRequest.GetResponseHeader("Link");
                    


                    
                url = ParseLinkHeaderForNextUrl(linkHeader);
            }
        }

        textLoading.text = "Complete";
        
        var dictionaryOrdered = _commits.OrderBy(pair => pair.Value.NumCommits)
            .ToDictionary(pair => pair.Key, pair => pair.Value);

        foreach (var keyAndValue in dictionaryOrdered)
        {
            keyAndValue.Value.TextUI.transform.SetParent(content);
        }


        textNumUsers.text = $"Users: {_commits.Count}";
        textNumCorrections.text = $"Corrections: {numCorrections}";


    }
    private void ExtractMessageFromJson(string json)
    {
        string[] lines = json.Split("\n");


        foreach (var line in lines)
        {
            if (line.Contains("\"message\": \"Merge pull request"))
            {
                print( GetUsernameMessage(line.Trim()));

                string usernameMessage= GetUsernameMessage(line.Trim());

                numCorrections++;
                
                if (!_commits.ContainsKey( usernameMessage))
                {
                    
                    int numCommits = 1;
                    GameObject textUIGameObject = Instantiate(prefabText, contentNonOrdered);
                    Text textUI = textUIGameObject.GetComponent<Text>();

                    CommitUI commitUI = new CommitUI(usernameMessage,numCommits,textUI);
                    commitUI.UpdateTextUI();
                    _commits.Add(usernameMessage,commitUI);
                }
                else
                {
                    int numCommits = _commits[usernameMessage].NumCommits+1;
                    Text textUI = _commits[usernameMessage].TextUI;
                    CommitUI commitUI = new CommitUI(usernameMessage,numCommits,textUI);
                    commitUI.UpdateTextUI();

                    _commits[usernameMessage] = commitUI;

                }
                
            }
        }
    }
    
    private string GetUsernameMessage(string message)
    {

        //TODO: fix
        
        message = message.Substring(9,message.Length-9);

        int posFrom = message.IndexOf("from ")+5;
        int posSlash = message.IndexOf("/");

        message= message.Substring(posFrom, posSlash - posFrom);
        //message = message.Substring(0,message.Length-posBackslash);
        
        
        return message;


    }
    
    

    //Extract link
    private string ParseLinkHeaderForNextUrl(string linkHeader)
    {
        if (string.IsNullOrEmpty(linkHeader))
            return null;

        string[] links = linkHeader.Split(',');

        foreach (var link in links)
        {
            string[] segments = link.Split(';');
            if (segments.Length < 2)
                continue;

            string url = segments[0].TrimStart('<').TrimEnd('>');
            string rel = segments[1].Trim();

            if (rel == "rel=\"next\"")
                return url;
        }

        return null;
    }
}


[Serializable]
class CommitUI
{

    public CommitUI(string username, int numCommits, Text textUI)
    {
        this._username = username;
        this._numCommits = numCommits;
        this._textUI = textUI;
    }
    
    private string _username;
    private int _numCommits;
    private Text _textUI;

    public int NumCommits => _numCommits;

    public Text TextUI => _textUI;
    public void UpdateTextUI()
    {
        _textUI.text = $"{_username}: {_numCommits}";
    }
    
}
