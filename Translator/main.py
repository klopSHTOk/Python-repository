import sys
import time
from PyQt5.QtWidgets import QApplication  # I've done these imports to add important 
from PyQt5.QtWidgets import QMainWindow   # modules from "PyQt5" library in my program
from PyQt5.QtWidgets import QLineEdit     # 
from PyQt5.QtWidgets import QLabel        # Further, you'll see these things in code
from PyQt5.QtWidgets import QPushButton   #
from PyQt5.QtWidgets import QMessageBox   # This import's used to make an error window
from PyQt5 import QtGui                   # And that import's used to add an icon in my GUI
import pyttsx3                            # 
import textblob                           # Module 'pyttsx3' is used to make a word's pronunciation. 
from textblob import TextBlob             # 'textblob' is very helpful with translating, he works on the Google API  


# ----------------------------------------------------
class MainWindow(QMainWindow):             # Here I've made a class of the program main window
    def __init__(self):
        super(MainWindow, self).__init__() 

        self.setWindowTitle('Translator')     # Here I've written a title of the window
        self.setGeometry(1620, 900, 482, 482) # In this string I've set geometry of *my* window, 
                                              # but you'd correct it for yourself according to the screen resolution

        self.in_put = QLineEdit(self)            # 
        self.in_put.move(147, 170)               # By using this class I've made line edit
        self.in_put.setFixedWidth(195)           # in which you can write needed words to translate
        self.in_put.setFixedHeight(40)           #

        self.button_to_tran = QPushButton(self)                #
        self.button_to_tran.setText('Перевести\n(произнести)') # Here I've made just a button
        self.button_to_tran.move(187, 215)                     # which you need to push after writing words to translate
        self.button_to_tran.adjustSize()                       #

        self.button_to_tran.clicked.connect(self.translation)         # It's just a method working for upper button

        self.see_res = QLabel(self)     # 
        self.see_res.move(147, 137)     # This's a label with the result of translating    
        self.see_res.setFixedWidth(240) #

        self.clean = QPushButton(self)  #
        self.clean.setText('Очистить')  # That button we can use to clean our line edit
        self.clean.move(187, 267)       # For correct work of this button I've written a special method, which is presented below
        self.clean.adjustSize()         #

        self.clean.clicked.connect(self.in_put.clear) # Here it's!

# --------------------------------------------------------------------------------------------------------------------------
    def translation(self): 

        #___________________________________________________________________________________________________________________
        try:                                         # This's main 'try' block 
            self.blob = TextBlob(self.in_put.text()) # In this string I import TextBlob method from 'textblob' class
            self.deteced = self.blob.detect_language()   

            if self.deteced == 'ru' or 'uk':             # Translation from Russian language to English language
                try:
                    self.translated = self.blob.translate(to='en')
                    self.see_res.setText(f'{self.translated}')

                    self.en_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
                    self.engine = pyttsx3.init()
                    self.engine.setProperty('voice', self.en_voice_id)
                    self.engine.say(self.translated)

                    time.sleep(1)
                    self.engine.runAndWait()

                except textblob.exceptions.NotTranslated:
                    self.see_res.setText('Перевод невозможен!')

            if self.deteced == 'en':                    # Translation from English to Russian
                try:
                    self.translated = self.blob.translate(to='ru')
                    self.see_res.setText(f'{self.translated}')

                    self.ru_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'
                    self.engine = pyttsx3.init()
                    self.engine.setProperty('voice', self.ru_voice_id)
                    self.engine.say(self.translated)

                    time.sleep(1)
                    self.engine.runAndWait()

                except textblob.exceptions.NotTranslated:
                    self.see_res.setText('Перевод невозможен!')

            else:                                                   # This's error window which appears when you write                                                                       
                not_def = QMessageBox()                             # words from other languages (default: Russian/English)
                not_def.setWindowTitle('Неидентифицированный язык') # Actually, it doesn't always work...
                not_def.setText('Данного языка нет в базе данных!')
                not_def.move(1640, 1000)
                not_def.setIcon(QMessageBox.Warning)
                not_def.setWindowIcon(QtGui.QIcon('error.png'))
                not_def.setStandardButtons(QMessageBox.Ok)
        #_________________________________________________________________________________________________________________    
        except textblob.exceptions.TranslatorError:   # This main 'exception' block contain error window which appears
            error = QMessageBox()                     # when you click on the button "Перевести" before writing any words in the line edit 
            error.setWindowTitle('Пустое поле ввода')
            error.setText('Прежде чем нажимать кнопку перевода,\nпровертье заполненность поля.')
            error.move(1640, 1000)
            error.setIcon(QMessageBox.Warning)
            error.setWindowIcon(QtGui.QIcon('error.png'))
            error.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)

            error.exec_()

        self.clean.clicked.connect(self.see_res.clear)             # That method works after pushing a button named "Очистить"

        #_________________________________________________________________________________________________________________

# --------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':                          # This construction's very important,
    app = QApplication(sys.argv)                    # because we can run a program only with it
    app.setWindowIcon(QtGui.QIcon('translate.png'))
    window = MainWindow()

    window.show()
    sys.exit(app.exec())