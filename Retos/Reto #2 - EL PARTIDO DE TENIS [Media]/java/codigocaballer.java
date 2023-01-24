package java;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class codigocaballer {
    static class Score {
        int points = 0, adv = 0, numPlayer;
        boolean winner = false;

        Score(int numPlayer) {
            this.numPlayer = numPlayer;
        }

        public <T> T getScoreOrDefault(T value, T defaultValue) {
            return value.equals(new Integer(0)) ? defaultValue : value;
        }

        public void sumAndShow(Score s2) {
            if (points < 40) {
                points += (points < 30 ? 15 : 10);
                System.out.println(points == 40 && points == s2.points
                        ? "Deuce"
                        : (numPlayer == 1
                                ? getScoreOrDefault(points, "Love")
                                        + " - " + getScoreOrDefault(s2.points, "Love")
                                : getScoreOrDefault(s2.points, "Love")
                                        + " - " + getScoreOrDefault(points, "Love")));
            } else {
                adv += 1;
                if (points == s2.points && s2.adv == adv)
                    System.out.println("Deuce");
                else if (points == s2.points && adv - s2.adv == 1)
                    System.out.println("Advance P" + numPlayer);
                else {
                    winner = true;
                    System.out.println("P" + numPlayer + " has won");
                }
            }
        }
    }

    public static void main(String[] args) throws IOException, InterruptedException {
        System.out.println(new String(new char[22])
                .replace("\0", "-")
                .concat(new String("\n------TENNIS GAME-----\n"))
                .concat(new String(new char[22])
                        .replace("\0", "-")));

        char[] msg = "Please enter the results table (one point every time with format P[player_number] and press enter):\n"
                .concat("ex:\nP1\n")
                .toCharArray();

        for (char c : msg) {
            System.out.print(c);
            Thread.sleep(10);
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputText = "";
        Score p1 = new Score(1), p2 = new Score(2);

        String pattern = "^[pP]([1|2])$";
        Pattern inputRegex = Pattern.compile(pattern);

        do {
            inputText = br.readLine();
            Matcher m = inputRegex.matcher(inputText);
            if (m.find()) {
                String pNumber = m.group(1);

                if (pNumber.equals("1"))
                    p1.sumAndShow(p2);
                else
                    p2.sumAndShow(p1);
            }

            else
                System.err.println("ERROR: wrong input, try again");
        } while (!p1.winner && !p2.winner);
    }
}