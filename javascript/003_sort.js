

var list = new Array(1, 2, 3);

console.log("List: " + list);
console.log("Länge der List: " + list.length);
console.log("Zufallszahl : " + random(0,100));
console.log("****Neue Zufallszahlen zur Liste hinzufügen****")
list.push(random(0,100));
list.push(random(0,100));
list.push(random(0,100));
list.push(random(0,100));
list.push(random(0,100));
list.push(random(0,100));
list.push(random(0,100));
console.log("List: " + list);
console.log("Länge der List: " + list.length);
console.log("Zufallszahl : " + random(0,100));



function random (min, max) {
    return  Math.round(Math.random() * (max - min) + min);
}