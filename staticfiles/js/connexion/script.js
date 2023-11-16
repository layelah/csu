// Code JavaScript pour masquer le message d'erreur après 1 secondes
setTimeout(function() {
    var errorMessage = document.getElementById('error-message');
    if (errorMessage) {
        errorMessage.style.display = 'none';
        }
}, 2000); // 1000 millisecondes = 1 secondes



document.addEventListener('DOMContentLoaded', function () {
    const passwordInput = document.getElementById('password');
    const passwordToggleIcon = document.getElementById('password-toggle');

    passwordToggleIcon.addEventListener('click', function () {
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            passwordToggleIcon.innerHTML = '<ion-icon name="eye-outline"></ion-icon>';
        } else {
            passwordInput.type = 'password';
            passwordToggleIcon.innerHTML = '<ion-icon name="eye-off-outline"></ion-icon>';
        }
    });
});

