# Gerador de Senhas Python

Este repositório tem como intuito gerar senhas "criptografadas" em **Python** que, caso não tenha a chave para visualizar as senhas, perde o acesso a elas. Você pode utilizar tanto o python3 quanto outra versão, mas deve seguir as especificações das bibliotecas.

Criada no ambiente de desenvolvimento do Windows 10, porém funcionando em outros SOs que atendam as especificações da linguagem **Python**.

**Como usar:**
- Inicie o arquivo **generate_key.py** para conseguir gerar a sua chave que deve ser guardada preciosamente. Após iniciar e salvar a chave gerada, inicie o arquivo **passwords.py** para começar a utilizar o seu gerador e visualizador das senhas geradas.

## Arquivos

- ***generate_key.py:*** Usado para gerar a chave utilizada para visualizar as senhas que estão criptografadas.
- ***passwords.json:*** Usado para guardar quais senhas estão geradas, criptografadas corretamente.
- ***passwords.py:*** Usado para gerar as senhas, visualizar e verificar se uma senha já foi gerada.

## Bibliotecas Utilizadas (+ relevantes)

- *Fernet (cryptography.fernet)*
- *secrets*

Para instalar a biblioteca *Fernet*, você deverá iniciar em seu terminal:

   > Python3 
   ```bash
   pip3 install cryptography
   ```

   > Python
   ```bash
   pip install cryptography
   ```
## Clonar o projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/lucasFR2/password_generator.git
   
Caso queira utilizar o código, fique a vontade. Peço que dê os créditos a mim caso for utilizar
