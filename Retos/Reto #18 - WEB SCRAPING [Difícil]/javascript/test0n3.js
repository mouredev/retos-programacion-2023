// JavaScript App that can only be applied through Browser console
// Aplicación en JavaScript que solo se puede aplicar en la consola del navegador

let articles = document.getElementsByClassName("notion-page-content-inner");
let expectedArticle = "";
for (let item of articles) {
  if (item.innerHTML.toLowerCase().match(/(agenda 8 de mayo)/g))
    expectedArticle = item.children;
}

let schedule = [];
for (let item in expectedArticle) {
  if (
    item > 11 &&
    (expectedArticle[item].tagName == "H1" ||
      expectedArticle[item].tagName == "BLOCKQUOTE")
  ) {
    schedule.push(expectedArticle[item].textContent);
    console.log(expectedArticle[item].textContent);
  }
}
