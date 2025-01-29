document.getElementById('registerButton').addEventListener('click', () => {
    const name = document.getElementById('registerName').value;
    const email = document.getElementById('registerEmail').value;
    const password = document.getElementById('registerPassword').value;

    if (name && email && password) {
        alert(`Cadastro realizado com sucesso! Nome: ${name}, E-mail: ${email}`);
    } else {
        alert('Por favor, preencha todos os campos de cadastro!');
    }
});

document.getElementById('loginButton').addEventListener('click', () => {
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;

    if (email && password) {
        alert(`Login realizado com sucesso! E-mail: ${email}`);
    } else {
        alert('Por favor, preencha todos os campos de login!');
    }
});