# Firebase PUCPR

Firebase PUCPR é um programa de autenticação em dois fatores dentro do firebase realizado em grupo para a Atividade Somativa correspondente ao Grupo 22, com os seguintes participantes:

* Bruno
* Josiane
* Roger
* Thatiane

## Instalação

Clone esse repositório do github e altere o `.env.example` para `.env` com as suas credenciais dentro do Firebase e do SMTP do Google correspondentes.

Assim

```bash
git clone https://github.com/er-jpg/firebase_auth
cd firebase_auth
vim .env.example
```

Depois instale os pacotes requeridos para a realização da atividade

```bash
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

Assim você pode realizar as ações da aplicação.
