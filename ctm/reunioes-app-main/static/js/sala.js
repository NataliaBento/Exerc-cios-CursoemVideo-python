function getSalas() {
    $.ajax({
        type: 'GET',
        url: `/admin/getSalas`,
        success: function (response) {
            // Manipular a resposta e popular o HTML
            let salas = response.salas;
            let tbl_salas = $('#tabela-salas');
            let nm_tipo;
            
            // Limpar o conteúdo atual
            tbl_salas.empty();

            salas.forEach(function (sala) {

                if (sala.tipo === 0){
                    nm_tipo = 'Normal';
                } else {
                    nm_tipo = 'Expressa';
                }

                var salaHTML = `<tr>
                        <td>${sala.id}</td>
                        <td>${sala.sala}</td>"
                        <td>${nm_tipo}</td>"
                        <td><button class="uk-button uk-button-default uk-button-small" type="button" uk-toggle="target: #modalVerSala" onclick="verSala(${sala.id})">Ver <span uk-icon="icon: eye"></span></button></td>
                    </tr>
                `;

                tbl_salas.append(salaHTML);
            });

        },
        error: function (error) {
            console.error(error);
        }
    });
}

function verSala(id) {
    $.ajax({
        type: 'GET',
        url: `/admin/getSala/${id}`,
        success: function (response) {
            // Manipular a resposta e popular o HTML
            let sala = response.sala;
            let selectTipo = $('#slct-input-tipo-visao');
            selectTipo.empty();

            let nm_tipo 

            if (sala.tipo === 0){
                selectTipo.append(`<option value="${sala.tipo}">Normal</option>`)
                selectTipo.append(`<option value="1">Expressa</option>`)
            } else {
                selectTipo.append(`<option value="${sala.tipo}">Expressa</option>`)
                selectTipo.append(`<option value="0">Normal</option>`)
            }

            $('#input-sala-visao').val(sala.sala);
            

            $('#btnUpdtSala').attr('onclick', `updtSala(${sala.id})`);
            
        },
        error: function (error) {
            console.error(error);
        }
    });
}

function addSala(){
    let formData = {
        'sala': $('#input-sala').val(),
        'tipo': $('#slct-input-tipo').val(),
    }

    let modalInstance = $('#modalAddSala');

    $.ajax({
        type: 'POST',
        url: '/admin/addSala',
        data: JSON.stringify(formData),  // Converte os dados para JSON
        contentType: 'application/json;charset=UTF-8',  // Define o cabeçalho Content-Type
        success: function (response) {
            // Exibe um SweetAlert de sucesso se a requisição for bem-sucedida
            Swal.fire({
                icon: 'success',
                title: 'Sucesso!',
                text: response.message
            }).then(function () {
                getSalas();
                $('#input-sala').val(''),
                $('#slct-input-tipo').val(''),
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

function updtSala(id) {
    let formData = {
        'sala': $('#input-sala-visao').val(),
        'tipo': $('#slct-input-tipo-visao').val(),
    }

    let modalInstance = $('#modalVerSala');

    $.ajax({
        type: 'POST',
        url: `/admin/updtSala/${id}`,
        data: JSON.stringify(formData),  // Converte os dados para JSON
        contentType: 'application/json;charset=UTF-8',  // Define o cabeçalho Content-Type
        success: function (response) {
            // Exibe um SweetAlert de sucesso se a requisição for bem-sucedida
            Swal.fire({
                icon: 'success',
                title: 'Sucesso!',
                text: response.message
            }).then(function () {
                getSalas();
                $('#input-sala').val('');
                $('#slct-input-tipo').val('');
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
    getSalas();
}