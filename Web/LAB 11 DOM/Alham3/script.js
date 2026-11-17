const garchig = document.querySelector("#garchig");
const tovch = document.querySelector("#tovch");
const t = document.querySelector("#tovch1")

tovch1.addEventListener("mouseover", function() {
    garchig.textContent = "Hello";
    garchig.style.color = "black";
});


tovch.addEventListener("click", function() {
    garchig.textContent = "You clicked it.";
    garchig.style.color = "purple";
});