/*
 * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
 * en dos dimensiones.
 * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
 *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
 * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
 * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarn en lograrlo.
 * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.   
 */

type PointLocation = {
  x: number;
  y: number;
}

type Velocity = PointLocation;

interface Point {
  loc: PointLocation,
  vel: Velocity,
}

const meetingPoint = (pointA: Point, pointB: Point): number | null => {
  // Resolviendo la ecuación para el eje x
  const tX = (pointB.loc.x - pointA.loc.x) / (pointA.vel.x - pointB.vel.x);
  
  // Resolviendo la ecuación para el eje y
  const tY = (pointB.loc.y - pointA.loc.y) / (pointA.vel.y - pointB.vel.y);
  
  // Si tX y tY son iguales, entonces se encontrarán en ese momento t
  if (tX === tY) {
    return tX;
  }
  return null;
}

const meetingPointWrapper = (pointA: Point, pointB: Point) => {
  const response = meetingPoint(pointA, pointB);

  if (response === null) {
    console.log('Los puntos no se encontrarán! 😢');
  } else {
    console.log(`Los puntos se encontrarán en ${response} segundos!!! 🎉`);
  }
}

// Ejemplos
// NO SE ENCUENTRAN

const pointA1: Point = {
  loc: { x: 0, y: 0 },
  vel: { x: 1, y: 0 },
};

const pointB1: Point = {
  loc: { x: 0, y: 1 },
  vel: { x: 1, y: 0 },
};
meetingPointWrapper(pointA1, pointB1);


const pointA2: Point = {
  loc: { x: 0, y: 0 },
  vel: { x: 1, y: 0 },
};

const pointB2: Point = {
  loc: { x: 1, y: 0 },
  vel: { x: -1, y: 0 },
};
meetingPointWrapper(pointA2, pointB2);

const pointA3: Point = {
  loc: { x: 0, y: 0 },
  vel: { x: 0, y: 1 },
};

const pointB3: Point = {
  loc: { x: 2, y: 0 },
  vel: { x: 1, y: 0 },
};
meetingPointWrapper(pointA3, pointB3);

// SE ENCUENTRAN!
const pointA4: Point = {
  loc: { x: 0, y: 0 },
  vel: { x: 1, y: 1 }
};

const pointB4: Point = {
  loc: { x: 2, y: 2 },
  vel: { x: 0, y: 0 }
};
meetingPointWrapper(pointA4, pointB4);
