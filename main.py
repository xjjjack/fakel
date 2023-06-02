from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
import deepl
import keyboard


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FakeL")

        self.label = QLabel("Double 'Ctrl+C' to copy and translate")
        self.setCentralWidget(self.label)

        keyboard.add_hotkey('ctrl+c', self.on_ctrl_c_pressed)
        
        with open('auth_key.txt', 'r') as f:
            self.auth_key = f.read()
        self.translator = deepl.Translator(self.auth_key)

    def on_ctrl_c_pressed(self):
        clipboard_text = QApplication.clipboard().text()
        translated_text = self.translator.translate_text(clipboard_text, target_lang='ZH') # replace with your translation function
        self.label.setText(translated_text.text)


app = QApplication([])
window = MainWindow()
window.show()

app.exec()
