$(document).ready(function () {
    // Função para fazer a solicitação AJAX
    function obterSlotsSala(id_sala, data, regiao) {
        $.ajax({
            type: 'GET',
            url: `/agenda/slots_sala/${data}/${id_sala}`,
            success: function (response) {
                // Manipular a resposta e popular o HTML
                var slots = response.slots;
                var marcacaoSlotsDiv = $(regiao);

                $('#input-inicio').val('');
                $('#input-fim').val('');

                // Limpar o conteúdo atual
                marcacaoSlotsDiv.empty();

                slots.forEach(function (slot) {
                    var { disponibilidade, ocupante } = slot;
                    var slotHTML = `
                    <div>
                        <div class="uk-card uk-card-default uk-card-small uk-card-body uk-card-hover slot-card" data-disponibilidade="${disponibilidade}">
                            <h3 class="uk-card-title">${slot.slot}</h3>
                            <p>${disponibilidade}</p>
                    `;

                    if (disponibilidade === "Indisponivel") {
                        slotHTML += `<p>${ocupante ? ocupante.username : ''}</p></div>`;
                    } else {
                        slotHTML += `</div>`;
                    }

                    slotHTML += `</div>`;

                    marcacaoSlotsDiv.append(slotHTML);
                });

                // Adicionar listener de evento de clique aos cards
                $('.slot-card[data-disponibilidade="Disponivel"]').on('click', function () {
                    $(this).toggleClass('uk-card-primary');
                    atualizarNotificacao();
                });

                $('.slot-card[data-disponibilidade="Indisponivel"]').toggleClass('uk-card-secondary');

                atualizarSelectHoraInicio(slots);
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        });
    }

    function obterSlotsSalaView(id_sala, data, regiao) {
        $.ajax({
            type: 'GET',
            url: `/agenda/slots_sala/${data}/${id_sala}`,
            success: function (response) {
                // Manipular a resposta e popular o HTML
                var slots = response.slots;
                var marcacaoSlotsDiv = $(regiao);

                // Limpar o conteúdo atual
                marcacaoSlotsDiv.empty();

                slots.forEach(function (slot) {
                    var { disponibilidade, ocupante } = slot;
                    var slotHTML = `
                    <div>
                        <div class="uk-card uk-card-default uk-card-small uk-card-body uk-card-hover slot-card" vw-data-disponibilidade="${disponibilidade}">
                            <h3 class="uk-card-title">${slot.slot}</h3>
                            <p>${disponibilidade}</p>
                    `;

                    if (disponibilidade === "Indisponivel") {
                        slotHTML += `<p>${ocupante ? ocupante.username : ''}</p></div>`;
                    } else {
                        slotHTML += `</div>`;
                    }

                    slotHTML += `</div>`;

                    marcacaoSlotsDiv.append(slotHTML);
                });


                $('.slot-card[vw-data-disponibilidade="Indisponivel"]').toggleClass('uk-card-secondary');

            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        });
    }

    // Função para atualizar o select com os slots disponíveis
    function atualizarSelectHoraInicio(slots) {
        var selectHoraInicio = $('#slct-hora-inicio');
        selectHoraInicio.empty();

        // Adicionar opções ao select
        slots.forEach(function (slot) {
            if (slot.disponibilidade === "Disponivel") {
                var option = $('<option>', { value: slot.slot, text: slot.slot });
                selectHoraInicio.append(option);
            }
        });

        // Exibir o select
        selectHoraInicio.css('display', 'block');
    }

    //Roda instruções apenas se 'agenda' estiver na url
    if (/\/agenda\//.test(window.location.href)) {
        // Adicionar listener de evento de alteração à data
        $('#dt_pretendida').on('change', function () {
            var dataEscolhida = $(this).val();
            var idSala = $('#input-sala-id').val();  // Substitua pelo ID da sala desejada
            obterSlotsSala(idSala, dataEscolhida, '#marcacao-slots');
            $('#input-data').val(dataEscolhida);
        });

        // Chamar a função inicialmente para definir o estado inicial com a data atual
        var idSalaInicial = $('#input-sala-id').val();
        var dataAtual = new Date().toISOString().split('T')[0];
        $('#dt_pretendida').val(dataAtual); // Definir a data atual
        $('#input-data').val(dataAtual)
        obterSlotsSala(idSalaInicial, dataAtual, '#marcacao-slots');
        obterSlotsSalaView(idSalaInicial, dataAtual, '#marcacao-slots-hoje');

        // Obtenha o elemento com o ID uk-accordion-1
        var accordionElement = document.getElementById("uk-accordion-1");

        // Obtenha o elemento com o ID resumo-agendamento
        var resumoAgendamentoElement = document.getElementById("resumo-agendamento");

        // Adicione um ouvinte de eventos para a mudança de estado
        accordionElement.addEventListener("click", function () {
            // Obtenha o valor atual de aria-expanded
            var expandedValue = accordionElement.getAttribute("aria-expanded");

            // Verifique se aria-expanded é "true" e mostre ou oculte o elemento resumo-agendamento
            if (expandedValue === "false") {
                resumoAgendamentoElement.style.display = "block";
            } else {
                resumoAgendamentoElement.style.display = "none";
            }
        });
    }

});

// Função para mostrar o popup
function mostrarPopup() {
    UIkit.modal.dialog(`
        <div class="uk-modal-body">
            <h2>Resumo da Reunião</h2>
            <p>Início: <span id="hora-inicio">--:--</span></p>
            <p>Fim: <span id="hora-fim">--:--</span></p>
            <p>Duração: <span id="duracao">--</span> minutos</p>
        </div>
    `).show();
}

// Função para atualizar a notificação com base nos slots marcados
function atualizarNotificacao() {
    let slotsSelecionados = $('.slot-card.uk-card-primary');
    let inicio = '--:--';
    let fim = '--:--';
    let duracao = 0;
    let formatoHora = { hour: '2-digit', minute: '2-digit', second: '2-digit' };

    if (slotsSelecionados.length > 0) {
        // Calcular a hora de início e fim com base nos slots selecionados
        var horarios = Array.from(slotsSelecionados).map(function (slot) {
            return $(slot).find('.uk-card-title').text();
        });

        inicio = horarios[0];
        inicio = new Date(`2000-01-01 ${inicio}`)
        fim = horarios[horarios.length - 1];
        fim = new Date(`2000-01-01 ${fim}`);
        fim.setMinutes(fim.getMinutes() + 15);

        // Calcular a duração em minutos
        duracao = (fim - inicio) / (1000 * 60);

    }

    // Atualizar o conteúdo do popup
    $('#hora-inicio').text(inicio);
    $('#hora-fim').text(fim);
    $('#duracao').text(duracao);

    //Popula Resumo
    $('#input-inicio').val(inicio.toLocaleTimeString([], formatoHora));
    $('#input-fim').val(fim.toLocaleTimeString([], formatoHora));
    $('#input-duracao').val(duracao);

    // Exibir notificação
    UIkit.notification({ message: `Sua reunião começará às <b>${inicio.toLocaleTimeString([], formatoHora)}</b> e irá até as <b>${fim.toLocaleTimeString([], formatoHora)}</b> com duração de <b>${duracao}</b> minutos.`, pos: 'top-right', status: 'warning' });
}

