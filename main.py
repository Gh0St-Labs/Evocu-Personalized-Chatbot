import threading

from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
from backend import TheChatBot
from threading import Thread


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Evocu. Your Friendly Neighbourhood ChatBot!')

        self.chatbot = TheChatBot()

        self.setMinimumSize(700, 500)

        # Chat Text Area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 680, 320)

        # Add the Input Section
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText(
            'What is the Quote Of The Day?')
        self.input_field.setGeometry(10, 340, 520, 35)

        # Add the 'Send' Button
        self.send_button = QPushButton('Send', self)
        self.send_button.setGeometry(550, 339, 143, 36)
        self.send_button.clicked.connect(self.send_response)

        self.show()

    def send_response(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append('+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ QUERY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+')
        self.chat_area.append(f"Me: {user_input}")
        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_query):
        response = self.chatbot.get_response(user_query)
        self.chat_area.append('*************************************************************')
        self.chat_area.append(f"Evocu: {response}")
        self.chat_area.append('+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ RESULT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+')

app = QApplication(sys.argv)
cbw = ChatBotWindow()
sys.exit(app.exec())