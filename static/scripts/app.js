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
