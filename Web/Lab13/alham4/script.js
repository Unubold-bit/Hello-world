const setgegdel = document.querySelector("#setgegdel");
const toologch = document.querySelector("#toologch");
const urdchilan = document.querySelector("#urdchilan");

setgegdel.addEventListener("input", function () {
    const urt = setgegdel.value.length;
    console.log("Одоогийн урт:", urt);
    toologch.textContent = urt + " / 100";
    urdchilan.textContent = setgegdel.value;
    if (urt >= 90) {
    toologch.style.color = "red";
    } else {
    toologch.style.color = "black";
    }
});