'use strict';

function meetingPoint(position1, velocity1, position2, velocity2) {
  const vectors = [position1, velocity1, position2, velocity2];
  if (!vectors.every(vector => Array.isArray(vector) && vector.length === 2 && vector.every(Number.isFinite))) {
    throw new Error('Cada posición y velocidad debe ser un vector [x, y]');
  }
  const candidates = [];
  for (let axis = 0; axis < 2; axis++) {
    const distance = position2[axis] - position1[axis];
    const relativeVelocity = velocity1[axis] - velocity2[axis];
    if (relativeVelocity === 0) {
      if (distance !== 0) return null;
    } else {
      candidates.push(distance / relativeVelocity);
    }
  }
  const time = candidates[0] ?? 0;
  if (time < 0 || candidates.some(candidate => Math.abs(candidate - time) > 1e-10)) return null;
  return {
    point: [position1[0] + velocity1[0] * time, position1[1] + velocity1[1] * time],
    time
  };
}

module.exports = { meetingPoint };

if (require.main === module) console.log(meetingPoint([0, 0], [1, 1], [10, 0], [-1, 1]));
