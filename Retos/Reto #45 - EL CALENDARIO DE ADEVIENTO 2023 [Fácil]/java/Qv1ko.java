import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

class Qv1ko {

    public static void main(String[] args) {
        calendar();
    }

    private static void calendar() {

        ArrayList<String> participants = new ArrayList<String>();
        String participant = "";
        int position = 0;
        boolean on = true, exit = false;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (!exit) {
            
            System.out.print("\n1) Add participant | 2) Show participants | 3) Delete participant | 4) Carry out the draw | 5) Exit\nSelect one option: ");

            try {
                switch(br.readLine()) {

                    case "1":

                        System.out.println("\nAdd participant\n");

                        System.out.print("Name: ");
                        participant = br.readLine();

                        for (String p : participants) {
                            if (participant.equalsIgnoreCase(p)) {
                                System.out.println("\nThe participant already exists\n");
                                on = false;
                                break;
                            }
                        }

                        if (on) {
                            participants.add(participant);
                        }

                        break;

                    case "2":

                        System.out.println("\nList of participants\n");

                        for (int i = 0; i < participants.size(); i++) {
                            System.out.println("- " + participants.get(i));
                        }

                        break;

                    case "3":

                        if (participants.size() > 0) {

                            System.out.println("\nDelete participant\n");

                            System.out.print("Name: ");
                            participant = br.readLine();

                            for (int i = 0; i < participants.size(); i++) {
                                if (participant.equalsIgnoreCase(participants.get(i))) {
                                    participants.remove(i);
                                    on = false;
                                    break;
                                }
                            }
                            
                            if (on) {
                                System.out.println("\nParticipant does not exist");
                            } else {
                                System.out.println("\nThe participant has been eliminated");
                            }

                        } else {
                            System.out.println("\nNo participants");
                        }

                        break;

                    case "4":

                        if (participants.size() > 0) {

                            position = (int)(Math.random() * participants.size());
                            System.out.println("\nThe winner is " + participants.get(position));
    
                            participants.remove(position);
                            
                        } else {
                            System.out.println("\nNo participants");
                        }
                        
                        break;

                    case "5":
                        
                        System.out.println("\nLeaving...\n");
                        exit = true;
                        break;

                    default:
                        System.out.println("\nSelect a number");
                    
                }

                on = true;

            } catch (IOException exc) {
                System.out.println("\nInput error\n");
            }

        }

    }

}
