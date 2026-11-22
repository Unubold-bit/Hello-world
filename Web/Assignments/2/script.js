const reviews = [
    {
        id: 0,
        name: "Isagi Yoichi",
        job: "Striker",
        img: "isagi.png",
        about: "Yoichi Isagi is the main protagonist of the Japanese manga and anime series Blue Lock, a high school striker who enters a ruthless training program to become the world's best forward."
    },
    {
        id: 1,
        name: "Bachira",
        job: "Dribler",
        img: "bachira.png",
        about: "Meguru Bachira is a fictional soccer player and a major character in the Blue Lock manga and anime series. He is a 17-year-old forward known for his cheerful, eccentric personality and unpredictable, instinct-driven style of play"
    },
    {
        id: 2,
        name: "Itoshi Sae",
        job: "Mid-fielder",
        img: "sae.png",
        about: "Sae Itoshi (also written Itoshi Sae; Japanese: 糸師 冴) is a fictional soccer prodigy and key character from the manga and anime series Blue Lock"
    },
    {
        id: 3,
        name: "Itoshi Rin",
        job: "Striker",
        img: "rin.png",
        about: "Rin Itoshi is a fictional 16-year-old striker from the soccer manga and anime series Blue Lock, known for his elite shooting, analytical game IQ, and rivalry with his older brother, Sae Itoshi"
    }
];

const img = document.getElementById("zurag");
const job = document.getElementById("job");
const authorName = document.getElementById("name");
const about = document.getElementById("about");

const prevBtn = document.querySelector(".prev-btn");
const nextBtn = document.querySelector(".next-btn");
const randomBtn = document.querySelector(".random-btn")
// set starting item

let currentItem = 0;

// Load initial item

window.addEventListener('DOMContentLoaded', function () {
    showPerson();
})

// show person based on item

function showPerson() {
    const item = reviews[currentItem];
    img.src = item.img;
    authorName.textContent = item.name;
    job.textContent = item.job;
    about.textContent = item.about;
}

// show next person

nextBtn.addEventListener("click", function() {
    currentItem++;
    if (currentItem > reviews.length - 1) {
        currentItem = 0;
    }
    showPerson();
});

// show previous erson
prevBtn.addEventListener("click", function() {
    currentItem--;
    if (currentItem < 0) {
        currentItem = reviews.length - 1;
    }
    showPerson();
});

// show random person

randomBtn.addEventListener("click", function () {
    let nextIndex = Math.floor(Math.random() * reviews.length);
    if (reviews.length > 1 && nextIndex === currentItem) {
        nextIndex = (currentItem + 1) % reviews.length;
    }
    currentItem = nextIndex;
    showPerson();
});