const sheltersBtn = document.getElementById('sheltersBtn');
sheltersBtn.addEventListener('click', function (e) {
    e.preventDefault();
    navigator.geolocation.getCurrentPosition((position) => {
        window.location = sheltersBtn.getAttribute('data-url') + `?latitude=${position.coords.latitude}&longitude=${position.coords.longitude}`
    })
    return false;
})

document.querySelector('.navbar-toggler').addEventListener('click', (e) => {
    document.querySelector('.navbar-collapse').classList.toggle('show');
})
document.querySelector('.navbar-placeholder').addEventListener('click', (e) => {
    document.querySelector('.navbar-collapse').classList.toggle('show');
})
