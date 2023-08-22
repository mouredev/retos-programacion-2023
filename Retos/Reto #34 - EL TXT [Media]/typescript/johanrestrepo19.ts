import { createInterface } from "node:readline/promises";
import { existsSync } from "node:fs";
import { join } from "node:path";
import { open } from "node:fs/promises";
import { stdin, stdout } from "node:process";

const FILE_PATH = join(".", "text.txt");
const RL = createInterface({ input: stdin, output: stdout, terminal: false });

const main = async () => {
  const isWriting = true;
  const fileExists = existsSync(FILE_PATH);

  const wishToDeleteContent = fileExists
    ? await RL.question(
        "El fichero ya existe, desea borrar el contenido? y/n: "
      )
    : null;

  const fd =
    fileExists && wishToDeleteContent === "n"
      ? await open(FILE_PATH, "a+")
      : await open(FILE_PATH, "w+");

  if (fileExists && wishToDeleteContent === "n") {
    stdout.write("\nContenido del fichero: \n");
    stdout.write(await fd.readFile({ encoding: "utf8" }));
    stdout.write("\n");
  }

  while (isWriting) {
    const userInput = await RL.question("Input: ");
    if (userInput === ":q") break;
    await fd.writeFile(`${userInput}\n`);
  }

  await fd.close();
  RL.close();
};

main();
