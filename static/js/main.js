const POP_UP = document.getElementById('popUp');
let reviews = [];

window.addEventListener('load', () => {
    reviews = JSON.parse(localStorage.getItem("reviews") || "[]");
    console.log(reviews)
    render();
});

document.getElementById('newReview').addEventListener('click', () => {
    POP_UP.style.display = 'block';

})

document.getElementById('addReview').addEventListener('click', () => {
    POP_UP.style.display = 'none';

    let review = {Car: rented-car.value, Person: person-name.value, Review: persons-review.value};

    rented-car.value == "";
    person-name.value == "";
    persons-review.value == "";

    reviews.push(review);

    render();
})

function render() {
    let webReviews = document.getElementById('webReviews');
    webReviews.innerHTML = "";

    for(let i = 0; i < reviews.length; i++) {
        let review = `
        <div class="review">
            <h3>rented-car: ${reviews[i].rented-car}</h3>
            <h4>person-name: ${reviews[i].person-name}</h4>
            <h5>persons-review: ${reviews[i].persons-review}</h5>
            <button onclick='removeReview("${reviews[i].rented-car}")'>Delete</button>
        </div>`;

        webReviews.innerHTML += review;
    }

    localStorage.setItem("reviews", JSON.stringify(reviews))
}


function removeReview(review){
    for(let i = 0; i < reviews.length; i++) {
        if(review === reviews[i].rented-car){
            delete reviews[i];
            break;
        }
    }

    reviews = reviews.filter(function (e) {return e != null;});

    localStorage.setItem("reviews", JSON.stringify(reviews))
    render();
}
