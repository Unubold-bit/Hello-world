const tovchuud = document.querySelectorAll(".songolt")
const urDun = document.querySelector("#ur_dun")

tovchuud.forEach(function (tovch){
    tovch.addEventListener("click", function (e) {
        console.log(e);
        console.log("Event-ийн төрөл:", e.type);
        console.log("Дарагдсан элемент:", e.target);

        const songoson = e.target.textContent;
        urDun.textContent = "Та " + songoson + " сонголоо";
    });
});