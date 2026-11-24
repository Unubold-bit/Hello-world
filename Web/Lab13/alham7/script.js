const maygt = document.querySelector("#maygt");
const email = document.querySelector("#email");
const nuuts = document.querySelector("#nuuts");
const davtakh = document.querySelector("#davtakh");

const emailAldaa = document.querySelector("#email_aldaa");
const nuutsAldaa = document.querySelector("#nuuts_aldaa");
const davtakhAldaa = document.querySelector("#davtakh_aldaa");
const amjilt = document.querySelector("#amjilt");


maygt.addEventListener("submit", function (e) {
    e.preventDefault();

    let zov = true;
    emailAldaa.textContent = "";
    nuutsAldaa.textContent = "";
    davtakhAldaa.textContent = "";
    amjilt.textContent = "";

    // 1. Email shalgah

    if (email.value.trim() === "") {
        emailAldaa.textContent = "Emailee bichne uu";
        zov = false;
    } else if (!emailAldaa.value.includes("@")) {
        emailAldaa.textContent = "Email @ temdegt aguulsan baih ystoi";
        zov = false;
    }

    // 2 Nuuts ug shalgah

    if (nuuts.value.length < 6) {
        nuutsAldaa.textContent = "Nuuts ug 6-aas dooshgui temdegtei baih ystoi";
        zov = false;
    }

    // 3. Nuuts ug davhtsaj baigaa eseh
    if (davtakh.value !== nuuts.value) {
        davtakhAldaa.textContent = "Nuuts ug taarahgui baina";
        zov = false;
    }

    console.log("Maygt zov eseh:", zov);

    if (zov) {
        amjilt.textContent = "Amjilt burtguullee!";
        maygt.reset();
    }

});