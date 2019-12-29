document.addEventListener('DOMContentLoaded', function () {
    var a = document.querySelectorAll('li')

    for (i = 0; i < a.length; i++) {
        a[i].style.display = 'none'
    }

    var b = document.querySelectorAll('span')

    for (i = 0; i < b.length; i++) {
        b[i].textContent = ''
    }

    var labels = document.querySelectorAll('label')

    for (i = 0; i < labels.length; i++) {
        labels[i].style.display = 'none'
    }

    var inputs = document.querySelectorAll('input')
    var placeholder = ['', 'Enter Your Username', 'Enter Your Occupation', 'Enter Your Age', 'Enter your childs name','Enter your relation to the child','Enter Your Email', 'Enter Your Password', 'Enter Your Password Again']
    for (i = 1; i < inputs.length; i++) {
        inputs[i].placeholder = placeholder[i]
    }
})
