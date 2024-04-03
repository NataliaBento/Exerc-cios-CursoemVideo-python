function getPerfil() {
    $.ajax({
        type: 'GET',
        url: `/usuario/getPerfil`,
        success: function (response) {
            // Manipular a resposta e popular o HTML
            let usuario = response.usuario;

            $('#input-perfil-usuario').val(usuario.username);

            $('#btnUpdtPerfil').prop('disabled', true);
            $('#btnUpdtPerfil').removeAttr('onclick');

            $('#input-perfil-password').on('input', function () {
                // Habilitar ou desabilitar o botão com base na presença de entrada no campo
                $('#btnUpdtPerfil').prop('disabled', $(this).val().trim() === '');
                $('#btnUpdtPerfil').attr('onclick', `updtCheckPerfil()`);
            });
        },
        error: function (error) {
            console.error(error);
        }
    });
}

function updtCheckPerfil() {
    Swal.fire({
        title: "Tem certeza?",
        text: "Você realmente deseja atualizar as informações?",
        icon: "warning",
        showDenyButton: true,
        showCancelButton: true,
        confirmButtonText: "Confirmar",
        denyButtonText: "Cancelar",
        dangerMode: true,
    }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
            uptdPerfil();
        } else if (result.isDenied) {
          Swal.fire("Nada aconteceu...", "", "info");
        }
      });
}

function uptdPerfil(){
    let formData = {
        'username': $('#input-perfil-usuario').val(),
        'password': $('#input-perfil-password').val()
    };

    $.ajax({
        type: 'POST',
        url: '/usuario/uptdPerfil',
        data: JSON.stringify(formData),  // Converte os dados para JSON
        contentType: 'application/json;charset=UTF-8',  // Define o cabeçalho Content-Type
        success: function (response) {
            // Exibe um SweetAlert de sucesso se a requisição for bem-sucedida
            Swal.fire({
                icon: 'success',
                title: 'Sucesso!',
                text: response.message
            }).then(function () {
                // Recarregar a página após clicar em "OK"
                location.reload();
            });

        },
        error: function (error) {
            // Exibe um SweetAlert de erro se a requisição falhar
            Swal.fire({
                icon: 'error',
                title: 'Erro!',
                text: error.responseJSON.message
            });

            //console.log(error.responseJSON.message);
        }
    });
}

getPerfil();