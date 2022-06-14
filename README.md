# Memewiki

## Environment Setup

```bash
pip install .
```

or, if you have Poetry:

```bash
poetry install
```

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

Se tiver algum problema, provavelmente tem a resolução na [Arch Wiki](https://wiki.archlinux.org/title/PostgreSQL).
