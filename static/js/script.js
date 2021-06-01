console.log("Hello!");


const uzlecosais = document.getElementById('Uzlecosais_logs');
let atsauksmes = [];

window.addEventListener('load', () => {
    atsauksmes= JSON.parse(localStorage.getItem("atsauksmes") || "[]");
    console.log(atsauksmes)
    render();
});

document.getElementById('jaunaAtsauksme').addEventListener('click', () => {
    uzlecosais.style.display = 'block';
})