def generate_pseudo_random(seed, a, c, m, num_values):
  pseudo_random_numbers = []
  x_n = seed

  for _ in range(num_values):
    x_n = (a * x_n + c) % m
    pseudo_random_numbers.append(x_n % 100 + 1)  # Ajustar el rango a 1-5

  return pseudo_random_numbers


seed = 3
a = 332423423423423
c = 232234234
m = 51234234
num_values = 10

random_sequence = generate_pseudo_random(seed, a, c, m, num_values)
print(random_sequence)
