import java.util.Scanner;

public class Qv1ko {

  public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    String userText=" ";
    System.out.print("Write: ");
    userText=sc.nextLine();
    leetTranslator(userText);
    sc.close();
  }//main

  private static void leetTranslator(String text) {
    String translatedText="Text in leet -> ";
    for(int i=0;i<text.length();i++) {
      switch(text.toLowerCase().charAt(i)) {
        case 'a':translatedText+='4';break;
        case 'b':translatedText+="I3";break;
        case 'c':translatedText+='[';break;
        case 'd':translatedText+=')';break;
        case 'e':translatedText+='3';break;
        case 'f':translatedText+="|=";break;
        case 'g':translatedText+='&';break;
        case 'h':translatedText+='#';break;
        case 'i':translatedText+='1';break;
        case 'j':translatedText+=",_|";break;
        case 'k':translatedText+=">|";break;
        case 'l':translatedText+='1';break;
        case 'm':translatedText+="/\\/\\";break;
        case 'n':translatedText+="^/";break;
        case 'o':translatedText+='0';break;
        case 'p':translatedText+="|*";break;
        case 'q':translatedText+="(_,)";break;
        case 'r':translatedText+="I2";break;
        case 's':translatedText+='5';break;
        case 't':translatedText+='7';break;
        case 'u':translatedText+="(_)";break;
        case 'v':translatedText+="\\/";break;
        case 'w':translatedText+="\\/\\/";break;
        case 'x':translatedText+="><";break;
        case 'y':translatedText+='j';break;
        case 'z':translatedText+='2';break;
        case '0':translatedText+='o';break;
        case '1':translatedText+='L';break;
        case '2':translatedText+='R';break;
        case '3':translatedText+='E';break;
        case '4':translatedText+='A';break;
        case '5':translatedText+='S';break;
        case '6':translatedText+='b';break;
        case '7':translatedText+='T';break;
        case '8':translatedText+='B';break;
        case '9':translatedText+='g';break;
        default:translatedText+=text.charAt(i);
      }//switch
    }
    System.out.println(translatedText);
  }//leetTranslator

}//class
