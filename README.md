# spartans-timesheet
Passo a Passo para configuração do projeto

1) fazer o clone do projeto
2) criar virtual env (FORA DA PASTA DO PROJETO PARA NÃO SUBIR NO GIT. QUEM FIZER DENTRO DA PASTA VAI TOMAR UMA VOADORA)
3) ativar o virtualenv
4) instalar requirements (pip install -r requirements.pip)
5) instalar o mysql server
---------------------------------
Divisão de Apps:

contas = [usuario, perfil, login]
squad = [squad, membros_squad]
core = [lançamento_horas, cliente, projeto, categoria]
