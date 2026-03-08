# Projeto de Automação
## Projeto destinado à automações de email's para novos usuários com Celery + Redis.
Diariamente pequenos sites se perguntam:

**Clientes entram mas após um tempo... Não voltam. Como poderiamos resolver isso?**

E a resposta é mais simples do que parece. Embora podemos achar que receber email's chatos mais podem nos irritar do que nos fazer pensar "Vou voltar para este site.", devíamos olhar por outro lado, email's não servem para anúncios, quando percebemos que é um "anúncio" automáticamente não olhamos e possívelmente iríamos parar como spam. De fato, email's como **anúncio** são um saco, porém, não consigo ignorar um email do **meu banco**. Bancos tem email's como aviso, até mesmo para anúnciar algo utilizam do aviso, e nunca ignoramos um email de nosso banco, até porquê nossa renda está lá. Email's bem utilizados podem ser uma **arma crucial** na jogada de marketing de um site, se utilizados da maneira certa.

## Sistema de email's automático

Propus um sistema em que logo que o usuário se cadastra recebe um código de confirmação de email, e após o cadastro recebe um email de boas vindas. A parte boa? Você pode colocar seus emails estratégicos para serem enviados diretamente para seu cliente logo após uma ação! Utilizando Redis + Celery o sistema de filas pode enviar **automáticamente** um email para seu cliente sem que você precise se preocupar com isso! Automatizando uma tarefa super chata mas que, usada estratégicamente pode ser *um benefício incrível* para seu site **trazendo resultados significantes**!

## Tecnologias Utilizadas

+ Python 3.12
+ Docker
+ PostgreSQL
+ Redis
+ Celery
+ Testes automáticos com Pytest
+ CI com GitHub Actions
+ Django REST
+ Authenticação com Json Web Token

<hr style="width: 400px;">

Sistema já conta com um building com **Docker Compose** junto com o arquivo **requirements.txt** para instalar dependências.

**O arquivo .env não está no repositório, insira seus dados de email para que os emails possam ser enviados.**

<hr>