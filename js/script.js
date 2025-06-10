// Обработчик формы авторизации
document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    if(username || password) {
        console.log('Попытка входа:', { username, password });
        alert('Добро пожаловать, ' + (username || 'гость') + '!');
    } else {
        guestLogin();
    }
});

// Обработчик кнопки "Войти как гость"
document.getElementById('guestLogin').addEventListener('click', guestLogin);

// Функция входа как гостя
function guestLogin() {
    console.log('Вход как гость');
    alert('Добро пожаловать в систему! Вы вошли как гость.');
    // window.location.href = 'dashboard.html'; // Перенаправление после входа
}

// Дополнительные функции
document.querySelector('.forgot-password').addEventListener('click', function(e) {
    e.preventDefault();
    alert('Функция восстановления пароля будет реализована позже.');
});

 document.getElementById('loginForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            
            if(username || password) {
                alert('Добро пожаловать, ' + (username || 'пользователь') + '!');
                // Здесь можно добавить реальную логику авторизации
            } else {
                alert('Пожалуйста, введите логин или пароль');
            }
        });

        // Обработка "Забыли пароль?"
        document.querySelector('.forgot-password').addEventListener('click', function(e) {
            e.preventDefault();
            alert('Функция восстановления пароля будет реализована позже');
        });

        // Обработка "Зарегистрироваться"
        document.querySelector('.register-link').addEventListener('click', function(e) {
            e.preventDefault();
            alert('Функция регистрации будет доступна позже');
              });