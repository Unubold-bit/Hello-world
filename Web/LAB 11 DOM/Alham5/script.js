const ner = document.querySelector("#ner")
const tovch = document.querySelector("#tovch"); 
const mendchilgee = document.querySelector("#mendchilgee");

tovch.addEventListener("click", function() {
    mendchilgee.textContent = "Hello " + ner.value + "!";
});