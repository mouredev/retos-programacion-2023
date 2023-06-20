import java.util.Scanner;

public class Qv1ko {
    
    public static void main(String[] args) {
        guessTheWord("peaked");
    }//main

    private static void guessTheWord(String keyWord) {
        if(keyWord.length()>1) {
            String misteryWord=letterHider(keyWord),attemp="";
            Scanner sc=new Scanner(System.in);
            Boolean guessed=false;
            char[] misteryLetters=misteryWord.toCharArray();
            for(int i=0;i<keyWord.length();i++) {
                System.out.println("The word is \""+misteryWord+"\"");
                System.out.print("Attempt ("+(i+1)+"/"+keyWord.length()+"): ");
                attemp=sc.nextLine();
                if(attemp.length()==keyWord.length()) {
                    if(attemp.equalsIgnoreCase(keyWord)) {
                        guessed=true;
                        break;
                    }
                } else if(attemp.length()==1) {
                    for(int j=0;j<misteryWord.length();j++) {
                        if(keyWord.toCharArray()[j]==attemp.charAt(0)) {
                            misteryLetters[j]=attemp.charAt(0);
                            misteryWord="";
                            for(char letter:misteryLetters) {
                                misteryWord+=letter;
                            }
                        }
                    }
                } else if(attemp.length()!=keyWord.length()&&attemp.length()!=1) {
                    i--;
                    continue;
                }
                if(misteryWord.equalsIgnoreCase(keyWord)) {
                    guessed=true;
                    break;
                }
            }
            System.out.println((guessed)? "\nYou guessed the word\n":"\nYou finished your attempts, the word was "+keyWord+"\n");
            sc.close();
        } else {
            System.out.println("Choose a keyword");
        }
    }//guessTheWord

    private static String letterHider(String word) {
        char[] letters=word.toCharArray();
        String hiddenWord="";
        if(word.length()>2) {
            for(int i=0;i<(int)(word.length()/2);i++) {
                letters[(int)(Math.random()*word.length())]='_';
            }
        } else {
            letters[(int)(Math.random()*word.length())]='_';
        }
        for(char letter:letters) {
            hiddenWord+=letter;
        }
        return hiddenWord;
    }//letterHider

}//class