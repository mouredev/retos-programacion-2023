import net.datafaker.Faker;
import java.util.*;

public class AdevientoCalendar {

    public static void main(String[] args) {
        AdevientoCalendar dev = new AdevientoCalendar();
        dev.play();
    }

    private List<String> users;
    private final Random r;
    private Scanner sc;
    public AdevientoCalendar() {
        this.users = new LinkedList<>();
        this.r = new Random();
        this.sc = new Scanner(System.in);
        loadRandomUsers(10);
    }

    public void addUser(String user){
        if (this.users.contains(user)) System.out.println("User already exists");
        else this.users.add(user);
    }

    public void showUsers(){
        for (String user : this.users) System.out.println(user);
    }

    public void deleteUser(String user){
        if (this.users.contains(user)) {
            this.users.remove(user);
            System.out.println("User deleted");
        } else {
            System.out.println("User doesn't exist");
        }
    }

    public void play(){
        displayMenu();
        processUserInput();
    }

    private void startGiveaway(){
        if (this.users.isEmpty()) {
            System.out.println("No users!");
            return;
        }

        int index = this.r.nextInt(this.users.size());
        String winner = this.users.get(index);
        System.out.println("The winner is " + winner + " Congratulations!");
        deleteUser(winner);
    }

    public void exit(){
        System.out.println("Exit...");
        System.exit(0);
    }

    private void displayMenu(){
        System.out.println("aDEViento Calendar");
        System.out.println("Options:\n1- Add user\n2- Delete user\n3- Show users\n4- Start giveaway\n5- Get number of users\n6- Exit");
        System.out.println("Please select one by entering the number");
    }

    private void processUserInput(){
        String input = "";

        while (!input.equals("6")) {
            input = sc.nextLine();
            switch (input) {
                case "1": {
                    System.out.println("Enter the user: ");
                    String user = sc.nextLine();
                    addUser(user);
                    break;
                }
                case "2": {
                    System.out.println("Enter the user to delete: ");
                    String user = sc.nextLine();
                    deleteUser(user);
                    break;
                }
                case "3": {
                    showUsers();
                    break;
                }
                case "4": {
                    startGiveaway();
                    break;
                }
                case "5": {
                    getNumberOfUsers();
                    break;
                }
                case "6": {
                    exit();
                }
                default: System.out.println("Invalid input. Please enter a valid number.");
            }
        }
    }

    public void getNumberOfUsers(){
        System.out.println("Number of users: " + this.users.size());
    }

    private void loadRandomUsers(int n){
        Faker faker = new Faker();
        for (int i = 0; i < n; i++) addUser(faker.name().firstName());
    }
}
