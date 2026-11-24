const ajil = document.querySelector("#ajil");
const nemeh = document.querySelector("#nemeh");
const jagsaalt = document.querySelector("#jagsaalt");

nemeh.addEventListener("click", function () {
    if (ajil.value.trim() === "") {
    return;
    }

    const li = document.createElement("li");
    li.innerHTML = "<span></span> <button class='ustgakh'>✕</button>";
    li.querySelector("span").textContent = ajil.value;
    jagsaalt.append(li);
    ajil.value = "";
});

jagsaalt.addEventListener("click", function (e) {
    console.log("Дарагдсан элемент:", e.target.tagName);

    if (e.target.classList.contains("ustgakh")) {
        e.target.parentElement.remove();
    } else if (e.target.tagName === "SPAN") {
        e.target.classList.toggle("khiisen");
        if (e.target.classList.contains("khiisen")) {
            e.target.style.textDecoration = "line-through";
            e.target.style.color = "gray";
        } else {
            e.target.style.textDecoration = "none";
            e.target.style.color = "black";
        }
    }
});

