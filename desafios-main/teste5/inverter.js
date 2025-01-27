function inverterString(s) {
    let invertida = "";
    for (let i = s.length - 1; i >= 0; i--) {
        invertida += s[i];
    }
    return invertida;
}

let string = prompt("Digite uma string para inverter:");
console.log(`String invertida: ${inverterString(string)}`);
