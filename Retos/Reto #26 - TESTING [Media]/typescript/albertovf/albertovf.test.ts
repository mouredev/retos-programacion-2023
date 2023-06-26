import { reto } from './albertovf';

describe('Test reto#12', () => {
	test('Comprobar meses que tienen Viernes 13', () => {
		expect(reto(2023, 1)).toBe(true);
		expect(reto(2023, 10)).toBe(true);
	});
	test('Comprobar meses que no tienen Viernes 13', () => {
		expect(reto(2023, 2)).toBe(false);
		expect(reto(2023, 6)).toBe(false);
	});
	test('Comprobar meses erroneos', () => {
		expect(reto(2023, 0)).toBe(false);
		expect(reto(2023, 16)).toBe(false);
		expect(reto(-50, 1)).toBe(false);
	});
});