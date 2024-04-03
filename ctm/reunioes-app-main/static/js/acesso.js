function autenticarCredencias() {
    var email = $('#email').val();
    var password = $('#psw').val();

    $('#btnLogin').prop('disabled', true);

    // Envia os dados para o servidor
    $.ajax({
        type: 'POST',
        url: '/autenticacao',  // Rota no backend para lidar com a autenticação
        data: JSON.stringify({ email: email, password: password }),
        contentType: 'application/json;charset=UTF-8',
        success: function (response) {
            // Redireciona para index.html se a autenticação for bem-sucedida
            if (response.success) {
                Swal.fire({
                    icon: "sucess",
                    title: "Ótimo!",
                    text: "Usuário autenticado com sucesso!"
                });
                setTimeout(function () {
                    window.location.href = '/';
                }, 2000);
            } else {
                Swal.fire({
                    icon: "error",
                    title: "Oops...",
                    text: "Autenticação inválida ou não encontrada...",
                });
                $('#btnLogin').prop('disabled', false);

            }
        },
        error: function () {
            alert('Erro ao processar a requisição.');
        }
    });
}