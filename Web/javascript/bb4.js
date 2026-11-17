const sek = 98;
const min = 60;
let minut = sek/60;
let sekund = sek%60;   
let m = Math.trunc(minut);
console.log(m, sekund);
