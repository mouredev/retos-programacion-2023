import static facil.reto12.Friday13.check;
import org.junit.Test;
import static junit.framework.TestCase.assertTrue;
import static junit.framework.TestCase.assertFalse;

public class Friday13Test {

    @Test
    public void friday13Exists(){
        assertTrue(check(2023, 1));
    }

    @Test
    public void friday13DoesNotExists(){
        assertFalse(check(2023, 2));
        assertFalse(check(2023, 11));
    }

    @Test
    public void multipleFriday13(){
        assertTrue(check(2017, 1));
        assertTrue(check(2017, 10));
        assertTrue(check(2018, 7));
        assertTrue(check(2019, 12));
        assertTrue(check(2020, 3));
        assertTrue(check(2021, 8));
        assertTrue(check(2022, 5));
    }

}
