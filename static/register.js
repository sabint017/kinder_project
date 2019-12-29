document.addEventListener('DOMContentLoaded', function() {
    var list = document.querySelectorAll('div')[0].querySelectorAll('li')

    for (i = 0; i < list.length; i++) {
        list[i].style.display = 'none'
    }

    var sp = document.querySelectorAll('div')[0].querySelectorAll('span')

    for (i = 0; i < sp.length; i++) {
        sp[i].textContent = ''
    }

    var labels = document.querySelectorAll('label')

    var boxlength = labels.length * 80 + 'px'

    document.querySelectorAll('div')[1].style.height = boxlength;
})