document.addEventListener('DOMContentLoaded', function () {
    var list = document.querySelectorAll('li')

    for (i = 3; i < list.length; i++) {
        list[i].style.display = 'none'
    }


})