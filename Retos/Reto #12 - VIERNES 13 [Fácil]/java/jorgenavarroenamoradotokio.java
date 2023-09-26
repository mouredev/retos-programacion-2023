package com.retos.ej12;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.Calendar;

public class jorgenavarroenamoradotokio {

	public static void main(String[] args) {
		System.out.println(existeViernesTreceCalendar(Calendar.JANUARY, 2023));
		System.out.println(existeViernesTreceLocalDate(1, 2023));
	}

	private static boolean existeViernesTreceCalendar(int mes, int anio) {
		Calendar c = Calendar.getInstance();
		c.set(Calendar.DAY_OF_MONTH, 13);
		c.set(Calendar.MONTH, mes);
		c.set(Calendar.YEAR, anio);
		return c.get(Calendar.DAY_OF_WEEK) == Calendar.FRIDAY;
	}

	private static boolean existeViernesTreceLocalDate(int mes, int anio) {
		LocalDate localDate = LocalDate.of(anio, mes, 13);
		return localDate.getDayOfWeek() == DayOfWeek.FRIDAY;
	}

}
