document.addEventListener('DOMContentLoaded', function() {
    var list = document.querySelectorAll('div')[0].querySelectorAll('li')

    for (i = 0; i < list.length - 1; i++) {
        list[i].style.display = 'none'
    }

    var sp = document.querySelectorAll('div')[0].querySelectorAll('span')

    for (i = 0; i < sp.length; i++) {
        sp[i].textContent = ''
    }

    var labels = document.querySelectorAll('label')
    for (i = 0; i < labels.length; i++) {
        labels[i].style.display = 'none'
    }

    var input = document.querySelectorAll('input')
    for (i = 1; i < input.length; i++) {
        input[i].placeholder = labels[i - 1].textContent
    }
    var boxlength;
    if (labels.length > 10) {
        boxlength = labels.length * 67 + 'px'
    } else {
        boxlength = labels.length * 75 + 'px'
    }

    document.querySelectorAll('div')[1].style.height = boxlength;
})