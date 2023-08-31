import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Qv1ko {

    public static void main(String[] args) {

        System.out.println("Hello World!");

        String myString = "";
        int myInt = 0;
        double myDouble = 0.35;
        boolean myBool = true;

        final int MYCONST = 35;

        if (myInt == 35) {
            System.out.println("if");
        } else if (myBool) {
            System.out.println("else if");
        } else {
            System.out.println("else");
        }

        String[] myArray = new String[] { "a", "r", "r", "a", "y" };
        ArrayList<String> myList = new ArrayList<String>();
        Object[] myTuple = { "t", "u", 42, true };
        Set<String> mySet = new HashSet<>();
        Map<String, Integer> myMap = new HashMap<String, Integer>();

        for (int i = 0; i < myArray.length; i++) {
            myList.add(myArray[i]);
            myTuple[0] = myArray[i];
            mySet.add(myArray[i]);
            myMap.put(myArray[i], i);
        }
        for (String setValue : mySet) {
            System.out.print(setValue);
        }
        while (myBool) {
            if (((int)(Math.random() * 11)) % 2 == 0) {
                myBool = false;
            }
            System.out.println("\nmyBool: " + myBool);
        }

        System.out.println(myFunction());
        myFunction(myString, myDouble, MYCONST);

        MyClass myClass = new MyClass(35);
        myClass.printValues();
    
        try {
            myInt = Integer.parseInt(myString);   
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }

    public static String myFunction() {

        return "myFunction";

    }

    private static void myFunction(String myString, double myDouble, int MYCONST) {

        System.out.println(myString + "\n" + myDouble + "\n" + MYCONST);

    }

}

class MyClass {
    
    private int myInt;

    public MyClass(int intValue) {
        myInt = intValue;
    }

    public void printValues() {
        System.out.println("myInt: " + myInt);
    }

}
