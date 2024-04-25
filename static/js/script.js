$(document).ready(function() {
    function carregarImagem() {
        return $('<img>').attr('src', 'https://thispersondoesnotexist.com/image').attr('alt', 'Foto de Perfil');
    }

    $.ajax({
        url: '/users/', // Endpoint para buscar os dados de todos os usuários
        method: 'GET',
        success: function(response) {
            // Limpa o contêiner de dados
            $('#data-container').empty();

            // Itera sobre os dados e os exibe na página
            response.forEach(function(user) {
                // Cria o contêiner de usuário
                var userContainer = $('<div class="user-container"></div>');

                // Cria as informações do usuário
                var userInfo = $('<div class="user-info"></div>');

                // Adiciona a imagem do usuário com sombra
                var userImage = $('<img src="' + user.profile_picture + '" alt="Foto de Perfil">');
                userImage.css('box-shadow', '2px 2px 4px rgba(0, 0, 0, 0.1)');

                // Cria os detalhes do usuário
                var userDetails = $('<div class="user-details"></div>');
                var userName = $('<p><strong>Nome:</strong> ' + user.name + '</p>');
                var userEmail = $('<p><strong>Email:</strong> ' + user.email + '</p>');
                var userProfession = $('<p><strong>Profissão:</strong> ' + user.profession + '</p>');
                var userPhoneNumber = $('<p><strong>Número de Telefone:</strong> ' + user.phone_number + '</p>');

                // Adiciona os elementos à estrutura do DOM
                userDetails.append(userName, userEmail, userProfession, userPhoneNumber);
                userInfo.append(userImage, userDetails);
                userContainer.append(userInfo);

                // Adiciona o contêiner de usuário ao contêiner de dados
                $('#data-container').append(userContainer);
            });
        },
        error: function(xhr, status, error) {
            console.error('Erro ao buscar dados do banco:', error);
        }
    });
});
