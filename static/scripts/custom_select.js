function formatPhoneNumber(input) {
    let phoneNumber = input.value.replace(/\D/g, '');
    input.value = "+" + phoneNumber;
}
var currentLanguage = document.getElementById("lang").value
document.addEventListener('DOMContentLoaded', function () {
    let select = document.getElementById('pet-select');

    let container = document.createElement('div');
    container.setAttribute('class', 'custom-select');

    let selectedItem = document.createElement('div');
    selectedItem.setAttribute('class', 'selected-item');
    if (currentLanguage == "en"){
        selectedItem.innerHTML = 'Country or region'
    } else if (currentLanguage == "el"){
        selectedItem.innerHTML = 'Χώρα ή περιοχή'
    } else if (currentLanguage == "de"){
        selectedItem.innerHTML = 'Land oder Region'
    } else if (currentLanguage == "fr"){
        selectedItem.innerHTML = 'Pays ou région'
    } else if (currentLanguage == "pt"){
        selectedItem.innerHTML = 'País ou região'
    } else if (currentLanguage == "nl"){
        selectedItem.innerHTML = 'Land of regio'
    } else if (currentLanguage == "sk"){
        selectedItem.innerHTML = 'Krajina alebo región'
    }  else if (currentLanguage == "lb"){
        selectedItem.innerHTML = 'Land oder Regioun'
    }

    let itemsContainer = document.createElement('div');
    itemsContainer.setAttribute('class', 'select-items');

    // Создаем копии всех option
    for (let option of select.options) {
        let item = document.createElement('div');
        item.innerHTML = option.innerHTML;
        item.addEventListener('click', function() {
            selectedItem.innerHTML = option.innerHTML;
            select.value = option.value;
            selectedItem.click();
        });
        itemsContainer.appendChild(item);
    }

    container.appendChild(selectedItem);
    container.appendChild(itemsContainer);
    select.parentNode.insertBefore(container, select.nextSibling);

    selectedItem.addEventListener('click', function () {
        this.nextSibling.classList.toggle('show');
    });

    // Закрываем окно выбора при клике вне него
    window.addEventListener('click', function (e) {
        if (!e.target.matches('.selected-item')) {
            let items = document.getElementsByClassName('select-items');
            for (let item of items) {
                if (item.classList.contains('show')) {
                    item.classList.remove('show');
                }
            }
        }
    });
});