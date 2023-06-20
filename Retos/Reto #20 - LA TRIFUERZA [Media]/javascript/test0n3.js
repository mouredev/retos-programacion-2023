function Triforce(input) {
  let nroRows = input;
  let elementWidth = 2 * nroRows - 1;
  let maxLength = elementWidth * 2 + 1;
  let externalPadding = Math.floor(maxLength / 2);
  let triforceText = drawTriforce();

  function printHead() {
    let element = "";
    for (let i = 0; i < nroRows; i++) {
      element += `${createPadding(externalPadding)}${createStars(i)}\n`;
      externalPadding -= 1;
    }
    return element;
  }

  function printBase() {
    let element = "";
    for (let i = 0; i < nroRows; i++) {
      element += `${createPadding(externalPadding)}${createStars(
        i
      )}${createPadding(elementWidth)}${createStars(i)}\n`;
      externalPadding -= 1;
      elementWidth -= 2;
    }
    return element;
  }

  function createPadding(padding) {
    let temp = "";
    for (let i = 0; i < padding; i++) {
      temp += " ";
    }
    return temp;
  }

  function createStars(row) {
    let temp = "";
    for (let i = 0; i < row * 2 + 1; i++) {
      temp += "*";
    }
    return temp;
  }

  function drawTriforce() {
    return printHead() + printBase();
  }

  Object.defineProperties(this, {
    triforce: {
      get: function () {
        return triforceText;
      },
    },
    nroRows: {
      get: function () {
        return nroRows;
      },
    },
  });
}

// [1, 2, 5].forEach((i) => console.log(new Triforce(i).triforce));

// console.log(new Triforce(10).nroRows);
