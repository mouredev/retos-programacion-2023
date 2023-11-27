type Vector = { x: number; y: number };
type Particle = {
  position: Vector;
  speed: Vector;
};
type LinearCoefficients = [number, number];
type Path = { x: LinearCoefficients; y: LinearCoefficients };

const findTimeToMeet = (
  equationCoefficients1: LinearCoefficients,
  equationCoefficients2: LinearCoefficients,
): number => {
  const ec2Inverted = equationCoefficients2.map(
    (coefficient) => coefficient * -1,
  );
  const coefficientSum: LinearCoefficients = [
    equationCoefficients1[0] + ec2Inverted[0],
    equationCoefficients1[1] + ec2Inverted[1],
  ];

  return Math.abs(coefficientSum[1] / coefficientSum[0]);
};

const evaluatePath = (path: Path, time: number): Vector => {
  const x = path.x[0] * time + path.x[1];
  const y = path.y[0] * time + path.y[1];
  return { x, y };
};

const findMeetingPoint = (p1: Particle, p2: Particle): string => {
  const pathCoefficients1: Path = {
    x: [p1.speed.x, p1.position.x],
    y: [p1.speed.y, p1.position.y],
  };

  const pathCoefficients2: Path = {
    x: [p2.speed.x, p2.position.x],
    y: [p2.speed.y, p2.position.y],
  };

  const timeToMeetX = findTimeToMeet(pathCoefficients1.x, pathCoefficients2.x);
  const timeToMeetY = findTimeToMeet(pathCoefficients1.y, pathCoefficients2.y);

  if (timeToMeetX !== timeToMeetY) return "The particles will not meet";

  const meetingPoint = evaluatePath(pathCoefficients1, timeToMeetX);
  return `The particles will meet at x: ${meetingPoint.x} and y: ${meetingPoint.y} in ${timeToMeetX} seconds`;
};

console.log(
  findMeetingPoint(
    { position: { x: -8, y: 2 }, speed: { x: 3, y: -1 } },
    { position: { x: -2, y: -7 }, speed: { x: 1, y: 2 } },
  ),
);

console.log(
  findMeetingPoint(
    { position: { x: 6, y: 4 }, speed: { x: -2, y: -2 } },
    { position: { x: 3, y: -4 }, speed: { x: -1, y: 2 } },
  ),
);
