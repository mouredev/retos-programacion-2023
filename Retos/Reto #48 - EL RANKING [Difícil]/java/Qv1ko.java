import java.io.File;
import java.util.HashMap;

class Qv1ko {

    public static void main(String[] args) {
        list();
    }

    private static void list() {

        File path = new File(".\\Retos");

        HashMap<String, Integer> users = new HashMap<String, Integer>();
        String user = "";
        int totalCorrections = 0, maxCorrections = 0;

        for (File challengeFolder : path.listFiles()) {
            if (challengeFolder.isDirectory()) {

                for (File languageFolder : challengeFolder.listFiles()) {
                    if (languageFolder.isDirectory()) {

                        for (File correction : languageFolder.listFiles()) {
                            if (correction.isFile()) {

                                totalCorrections++;

                                user = correction.getName().split("\\.")[0].toLowerCase();

                                if (users.get(user) == null) {
                                    users.put(user, 1);
                                } else {
                                    users.replace(user, users.get(user) + 1);
                                }

                            }
                            
                        }

                    }
                }

            }
        }

        for (String name : users.keySet()) {
            maxCorrections = (users.get(name) > maxCorrections) ? users.get(name) : maxCorrections;
        }
        
        for (int i = maxCorrections; i > 0; i--) {
            for (String name : users.keySet()) {
                if (users.get(name) == i) {
                    System.out.println(name + " -> " + i);
                }
            }
        }

        System.out.println("\nNumber of participants: " + users.size());
        System.out.println("Corrections sent: " + totalCorrections);

    }

}
