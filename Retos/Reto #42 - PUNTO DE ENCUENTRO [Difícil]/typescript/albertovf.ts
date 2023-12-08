class Point {
	x: number; y: number;

	constructor(x, y) {
		this.x = x;
		this.y = y;
	}

	distance = (z: Point) => {
		return Math.sqrt(
			(z.x - this.x) ** 2 +
			(z.y - this.y) ** 2
		)
	}
}

class Vector {
	x: number;
	y: number;
	vx: number;
	vy: number;

	constructor(o: Point, v: Point) {
		this.x = o.x;
		this.y = o.y;
		this.vx = v.x;
		this.vy = v.y;
	}

	origin() {
		return new Point(this.x, this.y);
	}

	desplazamiento(t: number) {
		return new Point(this.x + this.vx * t, this.y + this.vy * t);
	}
}

const colision = (A: Vector, B: Vector) => {
	let t = 1;
	let previousDistance = A.origin().distance(B.origin());
	let actualDistance = A.desplazamiento(t).distance(B.desplazamiento(t));

	while (true) {
		t++
		let Ax2 = A.desplazamiento(t).x;
		let Ay2 = A.desplazamiento(t).y;
		let Bx2 = B.desplazamiento(t).x;
		let By2 = B.desplazamiento(t).y;
		if (actualDistance >= previousDistance) {
			return 'Los puntos no se encuentran';
		}
		else if (Ax2 === Bx2 && Ay2 === By2) {
			return `Se han encontrado en (${Ax2}, ${Ay2}) en t=${t}`;
		}
		else {
			previousDistance = actualDistance;
			actualDistance = A.desplazamiento(t).distance(B.desplazamiento(t));
		}
	}
}

const reto = (v1: Vector, v2: Vector) => {
	console.log(colision(v1, v2));
}

reto(new Vector(new Point(0, 0), new Point(1, 1)), new Vector(new Point(5, 0), new Point(0, 1)));// Se cruzan
reto(new Vector(new Point(2, 0), new Point(0, 1)), new Vector(new Point(4, 0), new Point(0, 1)));// Objetos con vectores paralelos que nunca se encuentran.
reto(new Vector(new Point(2, 2), new Point(1, 1)), new Vector(new Point(4, 0), new Point(0, 1)));// Objetos que se cruzan pero no en el mismo instante
