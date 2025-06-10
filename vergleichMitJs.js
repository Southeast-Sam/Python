let passwort = "geheim";
let anzahl = 0;
for (let i = 0; i <= 3; i++) {
  let eingabe = prompt("Bitte Passwort eingeben:");
  if (eingabe === passwort) {
    alert("Zugang gewährt");
    break;
  } else {
    anzahl++;
    if (anzahl === 3) {
      alert("Zugang verweigert");
      break;
    } else {
      alert("Falsches Passwort, bitte erneut versuchen.");
    }
  }
}
