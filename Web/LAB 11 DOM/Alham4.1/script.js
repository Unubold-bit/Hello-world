const too = document.querySelector("#too");
const nemeh = document.querySelector("#nemeh");
const hasah = document.querySelector("#hasah");
const teg = document.querySelector("#teg");

let count = 0;


nemeh.addEventListener("click", function (){
    count = count + 1;
    too.textContent = count;
    nnn(count);
});

hasah.addEventListener("click", function() {
    count--;
    too.textContent = count;
    nnn(count);

});

teg.addEventListener("click", function() {
    count = 0;
    too.textContent = count;
    nnn(count);
});

function nnn(count) {
    if (count > 0) {
        too.style.color = "green";
    } else if (count < 0) {
        too.style.color = "red";
    } else {
        too.style.color = "black";
    };
};