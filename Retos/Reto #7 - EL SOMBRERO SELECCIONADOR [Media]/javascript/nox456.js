const readline = require("node:readline/promises");

const prompt = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

async function selectorHat() {
    const questions_answers = {
        "¿Cuál crees que es tu valor más importante?": [
            "Bondad",
            "Lealtad",
            "Sabiduría",
            "Astucia",
        ],
        "¿Cúal casa pertenece a tu tradición familiar?": [
            "Gryffindor",
            "Hufflepuff",
            "Ravenclaw",
            "Slytherin",
        ],
        "¿Cuál crees que es tu rasgo más importante?": [
            "Valiente",
            "Honesto",
            "Inteligente",
            "Ambicioso",
        ],
        "¿Cuál es tu color favorito?": ["Rojo", "Amarillo", "Azul", "Verde"],
        "¿Cuál de estos animales te gusta más?": [
            "León",
            "Tejón",
            "Águila",
            "Serpiente",
        ],
    };
    const questions = Object.keys(questions_answers);
    const answers = Object.values(questions_answers);

    const houses_points = {
        Gryffindor: 0,
        Hufflepuff: 0,
        Ravenclaw: 0,
        Slytherin: 0,
    };

    for (const question of questions) {
        const index = questions.indexOf(question);

        let question_prompt = `${question}: \n`;
        answers[index].forEach((answer, i) => {
            question_prompt = question_prompt.concat(`${answer} (${i + 1})\n`);
        });
        const prompt_value = await prompt.question(`${question_prompt}\n> `);
        const value_index = parseInt(prompt_value) - 1;

        houses_points[Object.keys(houses_points)[value_index]]++;
    }
    const max_house_points = Object.values(houses_points).sort(
        (a, b) => b - a
    )[0];
    const house_name =
        Object.keys(houses_points)[
            Object.values(houses_points).indexOf(max_house_points)
        ];
    console.log(`Felicidades!! Has entrado a ${house_name}`);
    prompt.close();
}

(async () => {
    await selectorHat();
})();
