const ajil = document.querySelector("#ajil");
const tovchMedeelel = document.querySelector("#tovch_medeelel");
const jagsaalt = document.querySelector("#jagsaalt");

ajil.addEventListener("keydown", function (e) {
    console.log("Daragdsan tovch:", e.key);
    tovchMedeelel.textContent = "Daragdsan tovch: " + e.key;

    if (e.key === "Enter") {
        const li = document.createElement("li");
        li.textContent = ajil.value;
        jagsaalt.append(li);
        ajil.value = "";
    }
});