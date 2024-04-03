// Função para atualizar a exibição do relógio na página
function updateTime() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();

    // Formata as horas, minutos e segundos com zero à esquerda, se necessário
    hours = hours < 10 ? '0' + hours : hours;
    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;

    // Constrói a string de tempo no formato HH:mm:ss
    var timeString = hours + ':' + minutes + ':' + seconds;

    // Atualiza o conteúdo do elemento HTML com o ID 'time'
    document.getElementById('relogio').textContent = timeString;
}

// Atualiza o relógio a cada segundo
setInterval(updateTime, 1000);