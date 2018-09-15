var readline = require('readline-sync');

console.log('Bitte Passwort eingeben:');
var password = 9632;
var input = readline.questionInt();
if (password === input) {
  console.log('Passwort korrekt.');
} else {
  console.log('Passwort leider falsch.');
}
