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



document.getElementById('promo').addEventListener('click', function() {
    var promoValue = document.querySelector('.promoInput').value.trim(); // Получаем значение из инпута и удаляем пробелы в начале и конце строки
    if (promoValue == "MAY2" || promoValue == "may2") {
      document.getElementById('modal').style.display = 'block'; // Показываем модальное окно об успешном применении промокода
    } else {
      document.getElementById('incorrectModal').style.display = 'block'; // Показываем модальное окно с сообщением об ошибке
    }
  });

  document.getElementById('useBtn').addEventListener('click', function() {
    document.getElementById('modal').style.display = 'none';
  });

  document.getElementById('useBtnIncorrect').addEventListener('click', function() {
    document.getElementById('incorrectModal').style.display = 'none';
  });