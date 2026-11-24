const khool = document.querySelector("#khool");
const tsai = document.querySelector("#tsai");
const salat = document.querySelector("#salat");
const avakhSongoltuud = document.querySelectorAll('input[name="avakh"]');
const niit = document.querySelector("#niit");


function niitBodokh() {
    let une = Number(khool.value);

    if (tsai.checked) {
        une = une + Number(tsai.value);
    }
    if (salat.checked) {
        une = une + Number(salat.value);
    }

    const avakh = document.querySelector('input[name="avakh"]:checked');
    une = une + Number(avakh.value);

    console.log("Нийт үнэ:", une);
    niit.textContent = "Нийт: " + une + "₮";
}

khool.addEventListener("change", niitBodokh);
tsai.addEventListener("change", niitBodokh);
salat.addEventListener("change", niitBodokh);

avakhSongoltuud.forEach(function (radio) {
 radio.addEventListener("change", niitBodokh);
});
