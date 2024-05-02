// Функция открытия табов
function openTab(tabName) {
    var i;
    var tabcontent = document.getElementsByClassName("tabcontent");
    var tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("active");
    }
    document.getElementById(tabName).style.display = "block";
    event.currentTarget.classList.add("active");
}

// Открыть первый таб по умолчанию
document.getElementById("active").style.display = "block";
document.getElementsByClassName("tablink")[0].classList.add("active");
document.addEventListener("DOMContentLoaded", function() {
    setRandomHighBid();
});
function setRandomHighBid() {
    var highBidElements = document.querySelectorAll('.product__highBid');

        // Генерируем случайное число от 100 до 1000
        // Вставляем случайное число в элемент
        highBidElements.forEach(el => {
            var randomBid = Math.floor(Math.random() * (1000 - 100 + 1)) + 100;

            el.innerHTML = "Highest bid: - " + randomBid + " €";

        });
    
}

// setTimeout(() => setRandomHighBid(), 3000);


