const counter = document.querySelector("#counter");
const count = document.querySelector("#count");
const decrease = document.querySelector("#decrease");
const reset = document.querySelector("#reset");
const increase = document.querySelector("#increase");
const box = document.querySelector("#box")
let num = 0;



increase.addEventListener("click", function(){
    num++;
    count.textContent = num;
    colorChanger(num);
})

decrease.addEventListener("click", function(){
    num--;
    count.textContent = num;
    colorChanger(num);
})

reset.addEventListener("click", function(){
    num = 0;
    count.textContent = num;
    colorChanger(num);
})

function colorChanger(num){
    if (num < 0 ){
        count.style.color = "red";
    } else if (num > 0) {
        count.style.color = "green";
    } else {
        count.style.color = "black";
    }
}
