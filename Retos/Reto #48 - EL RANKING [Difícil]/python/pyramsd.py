import os

directorio = os.path.dirname(__file__)
directorio = os.path.abspath(os.path.join(directorio, os.pardir, os.pardir))

usuarios = {}
ejercicios = 0

for _, _, files in os.walk(directorio):

    for file in files:
        if file.lower() not in ["ejercicio.md", "language_stats.py", ".ds_store", ".gitignore"]:
            user = os.path.splitext(file.lower())[0]
            usuarios[user] = usuarios.get(user, 0) + 1
            ejercicios += 1

sorted_usuarios = sorted(usuarios.items(), key=lambda item: item[1], reverse=True)

print(f"Número de usuarios únicos: {len(usuarios)}")
print(f"Número de correcciones enviadas: {ejercicios}")
print("Ranking de usuarios y correcciones:")
for index, user in enumerate(sorted_usuarios):
    print(f"{index + 1} {user[0]} ({user[1]})")
