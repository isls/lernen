var list = [1, 2, 3];

console.log('List: ' + list);
console.log('Länge der List: ' + list.length);
console.log('Zufallszahl : ' + calcRandomInt(0, 100));
console.log('****Neue Zufallszahlen zur Liste hinzufügen****');
list.push(calcRandomInt(0, 100));
list.push(calcRandomInt(0, 100));
list.push(calcRandomInt(0, 100));
list.push(calcRandomInt(0, 100));
list.push(calcRandomInt(0, 100));
list.push(calcRandomInt(0, 100));
list.push(calcRandomInt(0, 100));

console.log('List: ' + list);
console.log('Länge der List: ' + list.length);
console.log('Zufallszahl : ' + calcRandomInt(0, 100));

function calcRandomInt (min, max) {
  return Math.round(Math.random() * (max - min) + min);
}
