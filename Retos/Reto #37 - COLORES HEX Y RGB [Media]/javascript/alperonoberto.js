// transform rgb to hex:
// r: 0, g: 0, b: 0 -> #000000
//
// transform hex to rgb:
// #000000 -> r: 0, g: 0, b: 0

export function RGBToHex(RGBCode) {
    let hexString = "#";
  
    for (const val of Object.values(RGBCode)) {
      let hexVal = val;
      let result = "";
  
      while (hexVal > 16) {
        let operation = Math.floor(hexVal / 16);
        let resto = hexVal % 16;
        hexVal = operation;
  
        switch (operation) {
          case 10:
            result += "A";
            break;
          case 11:
            result += "B";
            break;
          case 12:
            result += "C";
            break;
          case 13:
            result += "D";
            break;
          case 14:
            result += "E";
            break;
          case 15:
            result += "F";
            break;
          default:
            result += operation;
            break;
        }
  
        switch (resto) {
          case 10:
            resto = "A";
            break;
          case 11:
            resto = "B";
            break;
          case 12:
            resto = "C";
            break;
          case 13:
            resto = "D";
            break;
          case 14:
            resto = "E";
            break;
          case 15:
            resto = "F";
            break;
        }
  
        result += resto;
      }
  
      hexString += result;
    }
    return hexString;
  }
  
  export function HexToRGB(hexCode) {
    let hexArr = hexCode.split("");
    hexArr.shift();
    let newHexArr = [];
  
    for (let i = 0; i < hexArr.length; i += 2) {
      newHexArr.push([hexArr[i], hexArr[i + 1]]);
    }
  
    const rgbTranslation = {
      r: newHexArr[0],
      g: newHexArr[1],
      b: newHexArr[2],
    };
  
    for (const [key, val] of Object.entries(rgbTranslation)) {
      if (isNaN(val[0])) {
        val[0] = val[0].toUpperCase();
      } else if (isNaN(val[1])) {
        val[1] = val[1].toUpperCase();
      }
      rgbTranslation[key] = hexValueToDecimal(val[0], 0) + hexValueToDecimal(val[1], 1);
    }
  
    return rgbTranslation;
  }
  
  function hexValueToDecimal(value, pos) {
    switch (value) {
      case "A":
        return pos === 0 ? 10 * 16 : 10;
      case "B":
        return pos === 0 ? 11 * 16 : 11;
      case "C":
        return pos === 0 ? 12 * 16 : 12;
      case "D":
        return pos === 0 ? 13 * 16 : 13;
      case "E":
        return pos === 0 ? 14 * 16 : 14;
      case "F":
        return pos === 0 ? 15 * 16: 15;
      default:
        return pos === 0 ? Number(value) * 16 : Number(value);
    }
  }
  
  const rgbColor = {
    r: 25,
    g: 86,
    b: 200,
  };
  
  const hexColor = "#2b0b17";
  
  console.log(RGBToHex(rgbColor));
  console.log(HexToRGB(hexColor));