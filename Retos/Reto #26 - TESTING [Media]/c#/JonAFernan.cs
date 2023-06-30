using Xunit;

/*
 * Crea tres test sobre el reto 12: "Viernes 13".
 * - Puedes copiar una solución ya creada por otro usuario en
 *   el lenguaje que estés utilizando.
 * - Debes emplear un mecanismo de ejecución de test que posea
 *   el lenguaje de programación que hayas seleccionado.
 * - Los tres test deben de funcionar y comprobar
 *   diferentes situaciones (a tu elección).
 */

namespace reto26;

public class TestReto13
    {
        [Fact]
        public static void TrueTest()
        {
            Assert.True(IsFriday13(5,2022));
        }

        [Fact]
        public static void FalseTest()
        {
            Assert.False(IsFriday13(7,2022));
        }

        [Fact]
        public static void CorrectFormatMonth()
        {
            int [] months = Enumerable.Range(1,12).ToArray();
            int [] years = Enumerable.Range(1,9999).ToArray();
    

            foreach (int month in months)  Assert.InRange(month, 1 , 12);
            foreach (int year in years) Assert.InRange(year, 1 , 9999);
            
        }


        public static bool IsFriday13(int month, int year)
    {
        DateTime dateToCheck = new DateTime(year, month, 13);

        return dateToCheck.DayOfWeek == DayOfWeek.Friday;
    }
    }