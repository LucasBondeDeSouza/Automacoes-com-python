import requests
import smtplib
import email.message

# Pegar a informação que você quer
requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
requisicao_dicionario = requisicao.json()
cotacao = float(requisicao_dicionario['USDBRL']['bid'])
print(cotacao)

# Enviar um aviso - email
def enviar_email(cotacao):
    corpo_email = f"""
    <p>Dólar esta abaixo de R$5.20. Cotação atual: R${cotacao}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = 'Dólar está hoje abaixo de R$5.20'
    msg['From'] = 'bondelucas77@gmail.com'
    msg['To'] = 'bondelucas77@gmail.com'
    password = 'xkajodwpmkjcbcaz'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login credentials for sending the email
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


if cotacao < 5.20:
    enviar_email(cotacao)

# deploy - heroku