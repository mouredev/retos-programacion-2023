import { describe, expect, it } from "vitest";

const reto12 = (month, year) => new Date(`${month} 13, ${year}`).getDay() === 5;

describe("reto12", () => {
	it("should return true", () => {
		expect(reto12("January", 2023)).toBe(true);
	});

	it("should return false", () => {
		expect(reto12("May", 2022)).toBe(true);
	});

	it("should return false", () => {
		expect(reto12("July", 2023)).toBe(false);
	});
});
