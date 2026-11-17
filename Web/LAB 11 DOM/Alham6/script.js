const jims = document.querySelector("#jims");
const nemeh = document.querySelector("#nemeh");
const jagsaalt = document.querySelector("#jagsaalt");

nemeh.addEventListener("click", function() {
    const li = document.createElement("li");
    const v = jims.value
    li.textContent = jims.value;
    if (v.trim() == "") {
        console.log("Hooson bn")
    } else { jagsaalt.append(li) };
    jims.value = "";
})