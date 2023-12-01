function hexToRgb(hex: string): { r: number; g: number; b: number } | null {
    const match = hex.toLowerCase().match(/^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i);
    if (!match) return null;

    const [, r, g, b] = match.map((x) => parseInt(x, 16));
    return { r, g, b };
}

function rgbToHex(rgb: number[]): string | null {
    const regex: RegExp = /^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
    const valid = rgb.every(c => regex.test(c.toString()));

    if (!valid) return null;

    const srgb = rgb.map(c => c.toString(16));

    return `#${srgb.join('').toLowerCase()}`;
}


const hex = "#FF5733";
const rgb = [255, 87, 51];

console.log(rgbToHex(rgb));
console.log(hexToRgb(hex));