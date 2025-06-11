// Preise halbieren
const preise = {
  Apfel: 1.2,
  Banane: 0.8,
  Kirsche: 2.5,
};

const preiseHalbiert = Object.fromEntries(
  Object.entries(preise).map(([obst, preis]) => [obst, preis / 2])
);
console.log(preiseHalbiert);
