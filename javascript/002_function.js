var x = 10;
console.log("Ergebnis für x=" + x + " = " + addMultiple(10));

function addMultiple(x) {
    var ergebnis = 0;
    for (let zahl = 0; zahl < x; zahl++) {
        ergebnis = ergebnis + zahl;
    }
    return ergebnis;
} 