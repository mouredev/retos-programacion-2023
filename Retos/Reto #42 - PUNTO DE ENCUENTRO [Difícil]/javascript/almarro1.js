function crossPoint(initialPosA, initialPosB, speedA, speedB) {
  const [xa, ya] = initialPosA;
  const [xb, yb] = initialPosB;
  const [vxa, vya] = speedA;
  const [vxb, vyb] = speedB;

  console.log(`Computing crossing point for A0=[${xa},${ya}], Va=[${vxa},${vya}], B0=[${xb},${yb}], Vb=[${vxb},${vyb}]`)

  // compute tx,ty based on final coordinates for x and y
  let tx = (xa - xb) / (vxb - vxa);
  let ty = (ya - yb) / (vyb - vya);
  // transform NaN or negative times into Infinity to simplify comparison in next steps
  if (!isFinite(tx) || tx < 0) { tx = Infinity };
  if (!isFinite(ty) || ty < 0) { ty = Infinity };

  // when tx is a number and positive
  if (isFinite(tx)) {
    const x = Math.min(xa + tx * vxa, xb + tx * vxb);
    const y = Math.min(ya + tx * vya, yb + tx * vyb);
    console.log(`Objects will meet at (${x},${y}) after ${tx} seconds`);
  } else if (isFinite(ty)) {
    // when ty is a number and positive
    const x = Math.min(xa + ty * vxa, xb + ty * vxb);
    const y = Math.min(ya + ty * vya, yb + ty * vyb);
    console.log(`Objects will meet at (${x},${y}) after ${tx} seconds`);
  } else {
    // tx and ty are not valid numbers
    console.log('Objects won\'t meet');
  }
}

crossPoint([0, 0], [5, 0], [1, 1], [-1, 1]);

crossPoint([0, 0], [6, 0], [1, 0], [-1, 0]);
crossPoint([0, 0], [6, 0], [1, 0], [1, 0]);
crossPoint([0, 0], [6, 0], [2, 0], [1, 0]);