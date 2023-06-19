# Sistema de Gestão de Propostas de Empréstimo Pessoal

Este projeto utiliza a seguinte stack:

- Django
- Celery
- React
- Postgres

A aplicação Django permite a criação dos **Campos** que devem ser preenchidos na proposta, bem como a visualização das **Propostas** submetidas pelos clientes através da UI desenvolvida em React.

Uma task em Celery é responsável por receber as propostas e atribuir um status Aprovada ou Negada, aleatoriamente.

## Como executar

Todos os componentes da arquitetura são servidos em containers definidos no arquivo `docker-compose.yml`. 

Para subir os containers, execute o seguinte comando:

```
docker compose up --build -d
```

Em seguida, execute o script `setup.sh` que é responsável por executar as migrations e criar um superuser com as seguintes credenciais:

```
Usuário: admin
Senha: admin
```

A plataforma em Django estará exposta na porta `8000` e a UI estará disponível na porta `5173`.