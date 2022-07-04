# Memewiki

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
