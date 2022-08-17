import pyttsx3
import smtplib
import const
import os
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio


def exact_process():    
    os.chdir('h://Programmes//SCRIPTS//Python//Projects//Main//TLReader//log//') # путь до текстового файла
    with open('to_read.txt', 'w', encoding='utf-8') as w:
        w.write(const.DATA[0])
    w.close()

    with open('to_read.txt', 'r', encoding='utf-8') as r:
        data = r.read()
    os.chdir('h://Programmes//SCRIPTS//Python//Projects//Main//TLReader//') # текущая директория

    tts = pyttsx3.init()
    ru_vocie_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_ruRU_PavelM" # голос из реестра
    tts.setProperty('voice', ru_vocie_id)
    tts.setProperty('rate', 250)
    tts.setProperty('volume', 1)
    tts.save_to_file(data, "audio.mp3")
    tts.runAndWait()

    r.close()

    def send_email():
        msg = MIMEMultipart()
        msg['From'] = const.EMAIL
        msg['To'] = const.EMAIL
        msg['Subject'] = 'Озвученный текст'

        filename = os.path.basename(const.PATH)
        with open(const.PATH, 'rb') as fp:
            file = MIMEAudio(fp.read())
            file.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(file)
        fp.close()

        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        #server.starttls()
        server.login(const.EMAIL, const.PASSWORD)
        server.send_message(msg)
        server.quit()   
    send_email()
