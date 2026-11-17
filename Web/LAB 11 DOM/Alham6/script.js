const jims = document.querySelector("#jims");
const nemeh = document.querySelector("#nemeh");
const jagsaalt = document.querySelector("#jagsaalt");

jims.style.height = "60px";
nemeh.addEventListener("click", function() {
    const li = document.createElement("li");
    const v = jims.value
    li.textContent = jims.value;
    if (v.trim() == "") {
        console.log("Hooson bn")
    } else { jagsaalt.append(li) };
    jims.value = "";
    li.addEventListener("click", function() {
    li.remove();
});
});

jims.addEventListener("keydown", function(e) {
    if(e.key === "Enter"){
        const li = document.createElement("li");
        const v = jims.value
        li.textContent = jims.value;
        if (v.trim() == "") {
            console.log("Hooson bn")
        } else { jagsaalt.append(li) };
        jims.value = "";
            li.addEventListener("click", function() {
            li.remove();
        });
    }
});

