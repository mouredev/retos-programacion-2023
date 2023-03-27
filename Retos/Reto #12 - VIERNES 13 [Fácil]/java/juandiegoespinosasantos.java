public class Friday13thChallenge {

    public static boolean hasFriday13th(final int year, final int month) {
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.YEAR, year);
        calendar.set(Calendar.MONTH, month - 1);

        return calendar.get(Calendar.DAY_OF_WEEK) == Calendar.FRIDAY;
    }
}
