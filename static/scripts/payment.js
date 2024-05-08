document.addEventListener("DOMContentLoaded", function() {
    var doneButton = document.getElementById("done");
    doneButton.addEventListener("click", function() {
        // Проверяем, все ли поля заполнены
        var inputs = document.querySelectorAll('.form__input');
        var allFieldsFilled = true;
        var countrySelect = document.querySelector('.selected-item');
        var country = countrySelect.textContent.trim();

        if (country === '') {
            alert('Please select a country.');
            return; // Прерываем выполнение функции, если страна не выбрана
        }
        inputs.forEach(function(input) {
            if (input.value === '') {
                allFieldsFilled = false;
            }
        });

        if (allFieldsFilled) {
            // Копируем значения из полей ввода
            var firstName = document.querySelector('.form__first').value;
            var lastName = document.querySelector('.form__last').value;
            var street = document.querySelector('.form__street').value;
            var street2 = document.querySelector('.form__street2').value;
            var city = document.querySelector('.form__city').value;
            var state = document.querySelector('.form__state').value;
            var zip = document.querySelector('.form__zip').value;
            var email = document.querySelector('.form__email').value;
            var phone = document.querySelector('.form__phone').value;

            // Вставляем значения в соответствующие элементы формы form__infoTwo
            document.querySelector('.data__first').innerText = firstName;
            document.querySelector('.data__last').innerText = lastName;
            document.querySelector('.data__street').innerText = street;
            document.querySelector('.data__street2').innerText = street2;
            document.querySelector('.data__city').innerText = city;
            document.querySelector('.data__state').innerText = state;
            document.querySelector('.data__zip').innerText = zip;
            document.querySelector('.data__country').innerText = country;
            document.querySelector('.data__email').innerText = email;
            document.querySelector('.data__phone').innerText = phone;

            // Удаляем форму form__info
            var formInfo = document.querySelector('.form__info');
            formInfo.classList.add('hidden');

            // Показываем заполненную форму form__infoTwo
            document.querySelector('.form__infoTwo').classList.remove('hidden');
        } else {
            alert('Please fill in all fields.');
        }
    });

    var changeButton = document.querySelector('.form__change');
    changeButton.addEventListener('click', function() {
        // Показываем форму form__info
        document.querySelector('.form__infoTwo').classList.add('hidden');
        var formInfo = document.querySelector('.form__info');
        formInfo.classList.remove('hidden');

        // Копируем данные из элементов формы form__infoTwo в инпуты формы form__info
        document.querySelector('.form__first').value = document.querySelector('.data__first').innerText;
        document.querySelector('.form__last').value = document.querySelector('.data__last').innerText;
        document.querySelector('.form__street').value = document.querySelector('.data__street').innerText;
        document.querySelector('.form__street2').value = document.querySelector('.data__street2').innerText;
        document.querySelector('.form__city').value = document.querySelector('.data__city').innerText;
        document.querySelector('.form__state').value = document.querySelector('.data__state').innerText;
        document.querySelector('.form__zip').value = document.querySelector('.data__zip').innerText;
        document.querySelector('.form__country').value = document.querySelector('.selected-item').textContent.trim();
        document.querySelector('.form__email').value = document.querySelector('.data__email').innerText;
        document.querySelector('.form__phone').value = document.querySelector('.data__phone').innerText;
    });


 
  
    
});
var formInfo = document.querySelector('.form__infoTwo');
var radioCard = document.getElementById("radioCard");
var orderBtn = document.getElementById("orderBtn");

// Функция для проверки условий и включения/выключения кнопки заказа
function checkConditions() {
    if (radioCard.checked) {
        orderBtn.disabled = false;
        orderBtn.style.backgroundColor = '#3665F3';
    } else {
        orderBtn.disabled = true;
        orderBtn.style.backgroundColor = '#ccc';
    }
}

// Добавляем слушатель события на изменения состояния радиокнопки
radioCard.addEventListener("change", checkConditions);


var orderBtn = document.getElementById("orderBtn");

orderBtn.addEventListener("click", function() {
    window.onbeforeunload = null;

});
window.onbeforeunload = function() {
    return "Data will be lost if you leave the page, are you sure?";
};
function formatPhoneNumber(input) {
    let phoneNumber = input.value.replace(/\D/g, '');

    phoneNumber = phoneNumber.replace(/(\d{1})(\d{3})(\d{3})(\d{4})/, '+$1 ($2) $3-$4');

    input.value = phoneNumber;
}
