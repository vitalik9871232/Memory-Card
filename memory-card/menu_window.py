from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

menu_wind = QWidget() # створюємо вікно
menu_wind.resize(400, 300) 
menu_wind.setWindowTitle('Меню')

# ------------------------------------------------------------------------------
# створюємо поле для запитання, поле для відповіді, поля для невірних відповідей
# ------------------------------------------------------------------------------

txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')

# ---------------
# створюємо форму
# ---------------

layout_form = QFormLayout()
layout_form.addRow('Питання',txt_Question)
layout_form.addRow('Вірна відповідь',txt_Answer)
layout_form.addRow('Невірна відповідь 1',txt_Wrong1)
layout_form.addRow('Невірна відповідь 2',txt_Wrong2)
layout_form.addRow('Невірна відповідь 3',txt_Wrong3)

# ----------------
# створюємо кнопки
# ----------------

btn_back = QPushButton('Назад') # повернутися
btn_clear = QPushButton('Очистити') # очищення
btn_add_q = QPushButton('Додати запитання') # додавання запитання

# ----------------------------------------
# додаємо кнопки до горизонтального макету
# ----------------------------------------

horizontal_btn_l = QHBoxLayout()
horizontal_btn_l.addWidget(btn_back)
horizontal_btn_l.addWidget(btn_clear)
horizontal_btn_l.addWidget(btn_add_q)

# ----------------------------------------------------
# додаємо горизонтальний макет до вертикального макету
# ----------------------------------------------------

vline = QVBoxLayout()
vline.addLayout(layout_form)
vline.addLayout(horizontal_btn_l)

menu_wind.setLayout(vline)