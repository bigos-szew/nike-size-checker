from dotenv import dotenv_values
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from discordwebhook import Discord
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

config = dotenv_values(".env")
logger = logging.getLogger(__name__)


def send_mail(subject, body, to):
    logger.info('sending email')
    try:
        msg = MIMEMultipart()
        msg['From'] = config['MAIL_LOGIN']
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP_SSL(
            config['MAIL_SERVER_IP'], config['MAIL_SERVER_PORT'])
        server.ehlo()
        server.login(config['MAIL_LOGIN'], config['MAIL_PASSWORD'])
        server.send_message(msg)
        server.quit()
    except Exception as e:
        logger.error(f'error occurred: {e}')


def send_discord_message(message):
    logger.info('sending email')
    try:
        discord = Discord(url=config["DISCORD_WEBHOOK"])
        discord.post(content=message)
    except Exception as e:
        logger.error(f'error occurred: {e}')
