const maygt = document.querySelector("#maygt");
const ner = document.querySelector("#ner");
const sanal = document.querySelector("#sanal");
const khariu = document.querySelector("#khariu");

maygt.addEventListener("submit", function (e) {
    e.preventDefault;

    console.log("Маягт илгээгдлээ");
    console.log("Нэр:", ner.value);
    console.log("Санал:", sanal.value)

    khariu.textContent = ner.value + ", tanii sanaliig hukeen avlaa. Bayrllaa!";
    khariu.style.color = "green";

    maygt.reset();

});