function getUsuarios() {
    $.ajax({
        type: 'GET',
        url: `/admin/getUsuarios`,
        success: function (response) {
            // Manipular a resposta e popular o HTML
            var usuarios = response.usuarios;
            var tbl_usuarios = $('#tabela-usuarios');
            
            // Limpar o conteúdo atual
            tbl_usuarios.empty();

            usuarios.forEach(function (usuario) {
                var usuarioHTML = `<tr>
                        <td>${usuario.username}</td>
                        <td>${usuario.email}</td>"
                        <td><button class="uk-button uk-button-default uk-button-small" type="button" uk-toggle="target: #modalVerUsuario" onclick="verUsuario(${usuario.id})">Ver <span uk-icon="icon: eye"></span></button></td>
                    </tr>
                `;

                tbl_usuarios.append(usuarioHTML);
            });

        },
        error: function (error) {
            console.error(error);
        }
    });
}

function verUsuario(id) {
    $.ajax({
        type: 'GET',
        url: `/admin/getUsuario/${id}`,
        success: function (response) {
            // Manipular a resposta e popular o HTML
            let usuario = response.usuario;
            let selectSetor = $('#slct-input-setor-visao');
            selectSetor.empty();

            $('#input-username-visao').val(usuario.username);
            $('#input-email-visao').val(usuario.email);
            selectSetor.append(`<option value="${usuario.setor[0]}">${usuario.setor[1]}</option>`)
            $('#slct-input-nivel-acesso-visao').val(usuario.nivel_acesso);

            $('#btnUpdtUsuario').prop('disabled', true);
            $('#btnUpdtUsuario').removeAttr('onclick');
            
            $('#password-visao').on('input', function () {
                // Habilitar ou desabilitar o botão com base na presença de entrada no campo
                $('#btnUpdtUsuario').prop('disabled', $(this).val().trim() === '');
                $('#btnUpdtUsuario').attr('onclick', `updtUsuario(${usuario.id})`);
            });
        },
        error: function (error) {
            console.error(error);
        }
    });
}

function addUsuario(){
    let formData = {
        'username': $('#input-username').val(),
        'email': $('#input-email').val(),
        'setor_id': $('#slct-input-setor').val(),
        'nivel_acesso': $('#slct-input-nivel-acesso').val(),
        'password': $('#input-password').val(),
    }

    let modalInstance = $('#modalAddUsuario');

    $.ajax({
        type: 'POST',
        url: '/admin/addUsuario',
        data: JSON.stringify(formData),  // Converte os dados para JSON
        contentType: 'application/json;charset=UTF-8',  // Define o cabeçalho Content-Type
        success: function (response) {
            // Exibe um SweetAlert de sucesso se a requisição for bem-sucedida
            Swal.fire({
                icon: 'success',
                title: 'Sucesso!',
                text: response.message
            }).then(function () {
                getUsuarios();
                $('#input-username').val(''),
                $('#input-email').val(''),
                $('#slct-input-setor').val(''),
                $('#slct-input-nivel-acesso').val(''),
                $('#input-password').val(''),
                UIkit.modal(modalInstance).hide();
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

function updtUsuario(id) {
    let formData = {
        'username': $('#input-username-visao').val(),
        'email': $('#input-email-visao').val(),
        'setor_id': $('#slct-input-setor-visao').val(),
        'nivel_acesso': $('#slct-input-nivel-acesso-visao').val(),
        'password': $('#password-visao').val(),
    }

    let modalInstance = $('#modalVerUsuario');

    $.ajax({
        type: 'POST',
        url: `/admin/updtUsuario/${id}`,
        data: JSON.stringify(formData),  // Converte os dados para JSON
        contentType: 'application/json;charset=UTF-8',  // Define o cabeçalho Content-Type
        success: function (response) {
            // Exibe um SweetAlert de sucesso se a requisição for bem-sucedida
            Swal.fire({
                icon: 'success',
                title: 'Sucesso!',
                text: response.message
            }).then(function () {
                getUsuarios();
                $('#input-username-visao').val(''),
                $('#input-email-visao').val(''),
                $('#slct-input-setor-visao').val(''),
                $('#slct-input-nivel-acesso-visao').val(''),
                $('#password-visao').val(''),
                UIkit.modal(modalInstance).hide();
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

if (/\/admin\//.test(window.location.href)) {
    getUsuarios();
}