class Qv1ko {

    public static void main(String[] args) {
        meetingPoint(new int[]{randomNumber(5), randomNumber(5)}, new int[]{randomNumber(5), randomNumber(5)}, new int[]{randomVector(2), randomVector(2)}, new int[]{randomVector(2), randomVector(2)});
    }

    private static void meetingPoint(int[] obj1, int[] obj2, int[] vectorObj1, int[] vectorObj2) {

        int time = 0;

        if (!parallel(vectorObj1, vectorObj2)) {

            while((obj1[0] != obj2[0] || obj1[1] != obj2[1]) && time < 180) {
                obj1[0] += vectorObj1[0];
                obj1[1] += vectorObj1[1];
                obj2[0] += vectorObj2[0];
                obj2[1] += vectorObj2[1];
                time++;
            }
    
            System.out.println((time == 180)? "Will not be found" : "Meets at " + obj1[0]+ "," + obj1[1] + " after " + time + " seconds");

        } else {
            System.out.println("Will not be found");
        }

    }

    private static boolean parallel(int[] vectorObj1, int[] vectorObj2) {
        return (vectorObj1[0] * vectorObj2[1] == vectorObj1[1] * vectorObj2[0]);
    }

    private static int randomNumber(int index) {
        return (int)(Math.random() * (index + 1));
    }

    private static int randomVector(int index) {
        return (int)(Math.random() * index) + 1;
    }

}
