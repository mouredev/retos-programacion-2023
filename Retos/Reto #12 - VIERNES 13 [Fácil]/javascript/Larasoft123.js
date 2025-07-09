function friday_13({ year, month }) {
  if (typeof year !== "number" || typeof month !== "number") {
    throw new Error("El año y el mes deben ser números");
  }
  return new Date(year, month - 1, 13).getDay() === 5;
}

try {
  const result1 = friday_13({ year: 2023, month: 2 });
  const result2 = friday_13({ year: 2025, month: 6 });

  console.log({result1,result2});
} catch (error) {
  console.log(error.message);
}

