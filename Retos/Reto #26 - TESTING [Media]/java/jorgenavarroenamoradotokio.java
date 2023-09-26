package com.retos.ej26;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.time.DayOfWeek;
import java.time.LocalDate;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class jorgenavarroenamoradotokio {

	@Test
	void whenDiaNoEsViernes() {
		assertFalse(existeViernesTreceLocalDate(9, 2023));
	}

	@Test
	void whenDiaEsViernes() {
		assertTrue(existeViernesTreceLocalDate(1, 2023));
	}

	@Test
	void whenDiaEsCero() {
		Exception thrown = Assertions.assertThrows(Exception.class, () -> {
			existeViernesTreceLocalDate(0, 2023);
		}, "Exception was expected");

		Assertions.assertEquals("Invalid value for MonthOfYear (valid values 1 - 12): 0", thrown.getMessage());
	}

	private boolean existeViernesTreceLocalDate(int mes, int anio) {
		LocalDate localDate = LocalDate.of(anio, mes, 13);
		return localDate.getDayOfWeek() == DayOfWeek.FRIDAY;
	}

}
