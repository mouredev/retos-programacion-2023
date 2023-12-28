public class Permutations {

    public static void main(String[] args) {
        permute("sol", "");
    }

    public static void permute(String str, String answer){
        if (str.isBlank()) {
            System.out.print(answer + " ");
            return;
        }

        for(int i = 0 ;i < str.length(); i++) {
            char ch = str.charAt(i);
            String leftSubstr = str.substring(0, i);
            String rightSubstr = str.substring(i + 1);
            String rest = leftSubstr + rightSubstr;
            permute(rest, answer + ch);
        }
    }
}
