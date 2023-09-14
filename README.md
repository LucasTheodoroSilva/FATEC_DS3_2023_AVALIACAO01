# GitHub User Information
- Este é um script Python simples que permite aos usuários obter informações sobre um usuário do GitHub usando a API do GitHub.

# Pré-requisitos
- Antes de usar este script, você precisa ter o Python instalado no seu sistema. Além disso, certifique-se de ter a biblioteca requests instalada. Você pode instalá-la usando o seguinte comando:

  ´´´ pip install requests ´´´

# Uso
Clone o repositório ou copie o código para o seu ambiente de desenvolvimento.

# Execute o script:
  ´´´ python github_user_info.py ´´´

Você será solicitado a inserir o nome de usuário do GitHub que deseja consultar.
O script enviará uma solicitação à API do GitHub e exibirá as informações do usuário, se encontrado.

# Exemplo de Saída
Se o usuário for encontrado, a saída será semelhante a:

***** Usuários do GitHub *****
- Qual é o nome do usuário? <digite o nome de usuário>
<username>
Nome completo: <Nome Completo>
Localização: <Localização>
Seguidores: <Número de Seguidores>
Seguindo: <Número de Seguindo>
Biografia: <Biografia>

Status da execução: 200

- Se o usuário não for encontrado, a saída será:

***** Usuários do GitHub *****
Qual é o nome do usuário? <digite o nome de usuário>
<username>
Usuário não encontrado

Status da execução: 404

- Se ocorrer algum outro erro, a saída será:

***** Usuários do GitHub *****
Qual é o nome do usuário? <digite o nome de usuário>
<username>
Não é possível encontrar o usuário

Status da execução: <Código de Status da Resposta>

- Certifique-se de fornecer um nome de usuário válido do GitHub para obter informações do usuário.
