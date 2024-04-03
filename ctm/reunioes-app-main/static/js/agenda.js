function addAgendamento(){
    let formData = {
        'id_sala': $('#input-sala-id').val(),
        'id_usuario':  $('#input-usuario').val(),
        'hora_inicio': $('#input-inicio').val(), 
        'hora_fim': $('#input-fim').val(),
        'data': $('#input-data').val(),
    };

    $('#btnAgendarN').prop('disabled', true);

    $.ajax({
        type: 'POST',
        url: '/agenda/agendar',
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
            $('#btnAgendarN').prop('disabled', false);
            //console.log(error.responseJSON.message);
        }
    });
}   

function addAgendamentoExp(){
    let formatoHora = { hour: '2-digit', minute: '2-digit', second: '2-digit' };

    let inicio = $('#slct-hora-inicio').val();
    let fim = new Date(`2000-01-01 ${inicio}`);
    inicio = new Date(`2000-01-01 ${inicio}`);
    fim.setMinutes(fim.getMinutes() + 10);

    $('#btnAgendarExp').prop('disabled', true);

    console.log(fim.toLocaleTimeString([], formatoHora));
    let formData = {
        'id_sala': $('#input-sala-id').val(),
        'id_usuario':  $('#input-usuario').val(),
        'hora_inicio': $('#slct-hora-inicio').val(), 
        'hora_fim': fim.toLocaleTimeString([], formatoHora),
        'data': $('#dt_pretendida').val(),
    };

    $.ajax({
        type: 'POST',
        url: '/agenda/agendar',
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

            $('#btnAgendarExp').prop('disabled', false);
            //console.log(error.responseJSON.message);
        }
    });
}  

function confirmarCancelamento(reuniaoId) {
    Swal.fire({
        title: "Tem certeza?",
        text: "Você realmente deseja cancelar esta reunião?",
        icon: "warning",
        showDenyButton: true,
        showCancelButton: true,
        confirmButtonText: "Confirmar",
        denyButtonText: "Cancelar",
        dangerMode: true,
    }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
            cancelarReuniao(reuniaoId);
        } else if (result.isDenied) {
          Swal.fire("Nada aconteceu...", "", "info");
        }
      });
}

function cancelarReuniao(reuniaoId) {
    // Envie uma solicitação ao backend para cancelar a reunião
    $.ajax({
        type: 'POST',
        url: '/agenda/cancelar_reuniao/'+ reuniaoId,
        success: function (response) {
            // Lógica adicional após o cancelamento (se necessário)
            if (response.success) {
                // Exibir uma mensagem de sucesso, recarregar a página ou realizar outras ações necessárias
                Swal.fire({
                    icon: 'success',
                    title: 'Sucesso!',
                    text: response.message
                }).then(function () {
                    location.reload();
                });
            } else {
                // Exibir uma mensagem de erro, se aplicável
                swal("Erro ao cancelar a reunião!", { icon: "error" });
            }
        },
        error: function () {
            // Exibir uma mensagem de erro em caso de falha na solicitação AJAX
            swal("Erro de comunicação com o servidor!", { icon: "error" });
        }
    });
}

