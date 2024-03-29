# Projeto Final da Disciplina de Persistência de Dados
Este projeto foi desenvolvido como parte do trabalho final da disciplina de Persistência de Dados. O projeto é uma aplicação web de gerenciamento de vacinação, onde os usuários podem agendar e acompanhar vacinações.

## Pré-requisitos
Certifique-se de ter o Docker instalado

## Como Rodar a Aplicação
Para rodar a aplicação com o Docker, siga as etapas abaixo:

Caso o usuário já tenha o postgres instalado, pare a aplicação em questão utilizando o comando abaixo (linux):

```sudo service postgresql stop```

Ademais:

```git clone https://github.com/gabriel-pcr/vacinacao-persistencia.git```

```cd vacinacao```

```chmod +x entrypoint.sh```

```docker build -t vacinacao .```

```docker-compose up --build```

Após as etapas acima, a aplicação estará disponível em http://localhost:8000

## Autores:
Gabriel Pires de Campos Rezende (Matrícula: 202004752)

Giancarlo Moraes de Sousa (Matrícula: 202004753)
