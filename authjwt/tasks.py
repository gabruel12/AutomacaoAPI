
from celery import shared_task
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings

@shared_task
def email_verificacao(username, email, code):
    send_mail(
        subject="Código de verificação - TechBird",
        message=f"Olá {username},\n\nSeu código é: {code}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )

@shared_task
def email_boas_vindas(username, email):
    subject       = 'Bem-Vindo!!'
    from_email    = settings.EMAIL_HOST_USER
    to            = [email]
    fail_silently = False
    text_content  = f"""
Olá {username},

Sua conta foi criada com sucesso!

Agora você já pode acessar a plataforma e aproveitar todos os recursos.

Se precisar de ajuda, estamos à disposição.

Equipe TechBird 🚀
""",
    html_content   = f"""
        <html>
            <body style="font-family: Arial, sans-serif;">
                <h2 style="color:#2E86C1;">Olá {username}, seja muito bem-vindo! 🎉</h2>
            
                <p>
                    Sua conta foi criada com <strong>sucesso</strong> e agora você já pode
                    acessar nossa plataforma.
                </p>

                <p>
                    Estamos muito felizes por ter você conosco. Nossa missão é oferecer
                    a melhor experiência possível para que você possa ter uma experiência agradável.
                </p>

                <a href="https://github.com/gabruel12"
                   style="
                       background-color:#2E86C1;
                       color:white;
                       padding:10px 20px;
                       text-decoration:none;
                       border-radius:5px;
                       display:inline-block;
                   ">
                   Acessar minha conta
                </a>

                <p style="margin-top:20px;">
                    Se tiver qualquer dúvida, basta responder este email.
                </p>

                <p>
                    Atenciosamente,<br>
                    <strong>Equipe TechBird 🚀</strong>
                </p>
            </body>
        </html>
""",
    
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    