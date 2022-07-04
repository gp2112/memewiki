# Memewiki

Este é um projeto inicialmente implementado para um trabalho da disciplina de Base de Dados, do ICMC/USP.

A ideia da Memewiki é ser uma plataforma brasileira que sirva como um "hub" de memes, com foco maior em memes nacionais, aos moldes de uma wikipedia, knowyoourmeme, rottentomatos, chans e reddit. Algumas das funcionalidades são a criação de uma página tipo "wiki" sobre um meme - por hora chamado de "meme base", que serve como uma "base" para outros memes derivados. Memes derivados, ou "normais", podem ser derivados de memes base, sendo praticamentte imagens comuns, sem muita informação, em que qualquer usuário possa criar de formma fácil e rápida.

O objetivo da plataforma, além de ser uma "wiki" e um "hub" de memes, é também permitir com que novos memes sejam criados, tal como são feitos no chans, mas sem a parte do descontrole e anomia que permeiam nesses ambientes. Pra isso a Memewiki também possui um Image Board, onde qualquer usuário pode criar uma thread e comentar com texto e imagens.

![image](https://user-images.githubusercontent.com/26512375/177132413-e6e4add4-7c7f-47d0-b755-23450257c9f4.png)

![image](https://user-images.githubusercontent.com/26512375/177127314-b7dbe062-c051-4d66-b762-b260073cd984.png)

![image](https://user-images.githubusercontent.com/26512375/177131557-1dfac7f0-5113-4e06-bbc4-fdd2d8616453.png)

Obviamente, ele está em faze de protótipo, com um layout improvisado (ninguém do grupo curtia front end ...) :v

## Requisitos:

- python 3
- postgresql

## Instalação e Execução:

    git clone https://github.com/gp2112/memewiki
    cd memewiki
    pip install .

execute:

    memewiki

ou, caso possua o poetry:

    cd memewiki
    poetry install
    poetry run memewiki



## PostgreSQL Install

Manuel Ultra rápido e pragmático LINUX:

Basicamente, quando instalar, ele cria um user postgres. Ele vai ser usado pra acessar o client por sockets.
Assim que instalar:

1. Entra no user: sudo -iu postgres

2. Inicia DB Cluster: initdb -D /var/lib/postgres/data

3. Volta pro user normal: dá um CTRL+D ou executa exit

4. Inicia o serviço do postgresql (o backend): sudo systemctl start postgresql.
    1. (opicional) - Se quiser que ele inicie sempre que o sistema iniciar, tb execute: sudo systemctl enable postgresql

Pronto, já tá rodando. Agora no cliente:

Se quiser entrar no client: 

1. Entra no user: sudo -iu postgres
2. Execute: psql

Para criar um DB:

1. Entra no user: sudo -iu postgres
2. createdb [NOME_DB]

OBS: Crie um banco dados chamado memewiki para execução deste projeto.

Se tiver algum problema, provavelmente tem a resolução na [Arch Wiki](https://wiki.archlinux.org/title/PostgreSQL).


## Funcionamento da aplicação

É importante para leitura do código entender as camadas e como elas interagem entre si.

```
    app -> [ routes <-> controller <-> services <-> models ]
          <-- VIEW ---    
```

O arquivo app.py define, através do Framework Flask, onde estão as rotas da aplicação. Os arquivos de rota mapeam funções do controller, que por sua vez chamam serviços, que por sua vez acessam models.

É na camada de models que está o código que faz comunicação com o banco de dados, usando a biblioteca [psycopg2](https://www.psycopg.org/). É essa biblioteca que lida com a comunicação com o driver do PostgreSQL e com proteção a SQL injection.

Ao voltar da cadeia de chamadas à funções de camadas cada vez mais internas, a rota retorna uma view com as informações requisitadas, utilizando HTML e CSS.

## Créditos

- [Guilherme Paixão](https://github.com/gp2112)
    - Modelagem Relacional da Base de Dados
    - Aplicação: backend, frontend, Implementação no PostgreSQL
    - Documentação da Aplicação
    
- [Lucas Almeida](https://github.com/lalmeida32)
    - Modelagem Entidade-Relacionamento da Base de Dados
    - Modelagem Relacional da Base de Dados
    - Documentação do Modelo e Planejamento da Base de Dados
    - Documentação da Aplicação
    
- [Ádrio Oliveira](https://github.com/adriooa)
    - Modelagem Entidade-Relacionamento da Base de Dados
    - Modelagem Relacional da Base de Dados
    - Documentação do Modelo e Planejamento da Base de Dados

- [Eduardo Rossi](https://github.com/RossiEduardo)
    - Modelagem Entidade-Relacionamento da Base de Dados
    - Modelagem Relacional da Base de Dados
    - Documentação do Modelo e Planejamento da Base de Dados
  
- [Breno Pejon](https://github.com/BPejon)
    - Implementação do Modelo Relacional em SQL
    - Projeto da Aplicaç
