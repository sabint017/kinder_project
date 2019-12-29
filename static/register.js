document.addEventListener('DOMContentLoaded', function() {
    var a = document.querySelectorAll('li')

    for (i = 0; i < a.length; i++) {
        a[i].style.display = 'none'
    }

    var b = document.querySelectorAll('span')

    for (i = 0; i < b.length; i++) {
        b[i].textContent = ''
    }

    var labels = document.querySelectorAll('label')

    var boxlength = labels.length * 80 + 'px'

    document.querySelectorAll('div')[1].style.height = boxlength;
})