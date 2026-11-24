const khairtsag = document.querySelector("#khairtsag");
const medeelel = document.querySelector("#medeelel");
console.log("script.js ачаалагдлаа");

khairtsag.addEventListener("click", function () {
    console.log("click");
    khairtsag.style.backgroundColor = "lightblue";
    medeelel.textContent = "Нэг удаа дарлаа (click)";
});
khairtsag.addEventListener("dblclick", function () {
    console.log("dblclick");
    khairtsag.style.backgroundColor = "orange";
    medeelel.textContent = "Хоёр удаа хурдан дарлаа (dblclick)";
});
khairtsag.addEventListener("mouseover", function () {
    console.log("mouseover");
    khairtsag.style.border = "4px solid green";
    medeelel.textContent = "Хулгана дээр ирлээ (mouseover)";
});
khairtsag.addEventListener("mouseout", function () {
    console.log("mouseout");
    khairtsag.style.border = "none";
    medeelel.textContent = "Хулгана гарлаа (mouseout)";
});