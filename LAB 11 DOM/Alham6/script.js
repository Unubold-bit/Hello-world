const jims = document.querySelector("#jims");
const nemeh = document.querySelector("#nemeh");
const jagsaalt = document.querySelector("#jagsaalt");

nemeh.addEventListener("click", function() {
    const li = document.createElement("li");
    li.textContent = jims.value;
    jagsaalt.append(li);
    jims.value = "";
})