const code_konami = [
  "Up",
  "Up",
  "Down",
  "Down",
  "Left",
  "Right",
  "Left",
  "Right",
  "B",
  "A",
];
const keys_entered_user = [];

document.addEventListener("keydown", (e) => {
  if (e.key === code_konami[keys_entered_user.length]) {
    keys_entered_user.push(e.key);

    if (code_konami.length === keys_entered_user.length) {
      console.log("Código Konami");
    } else {
      console.log(keys_entered_user);
    }
  } else {
    keys_entered_user.length = 0;
  }
});
