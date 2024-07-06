from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

main_wind = QWidget()
main_wind.resize(600, 500)
main_wind.move(300, 300)
main_wind.setWindowTitle('Memory Card')

#------------------------------------------------------
# Створимо потрібні віджети (Кнопки - таймер - надпис)
#------------------------------------------------------

btn_Menu = QPushButton("Меню")
btn_Sleep = QPushButton("Відпочити")
btn_OK = QPushButton("Відповісти")
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
lb_Question = QLabel("")

#---------------------------------------------------------
# Створюємо панель - із варіантами відповідей - групуємо
#---------------------------------------------------------

RadioGroupBox = QGroupBox ("Варіанти відповідей:") # Рамка для блоку кнопок
RadioGroup = QButtonGroup() # Всі кнопки в віджет

rbtn1 = QRadioButton('')
rbtn2 = QRadioButton('')
rbtn3 = QRadioButton('')
rbtn4 = QRadioButton('')

RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)
                            # Розміщення варіантів відповідей на макет
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout() # Вертикальні в середені горизонтального
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn1) # перші дві відповіді на першому вертикальну лінію
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2) # Привязуємо всі перемикачі до однієї горизонтальної лінії
layout_ans1.addLayout(layout_ans3) 

RadioGroupBox.setLayout(layout_ans1) # додаємо до рамки (лінії з віджетами)
RadioGroupBox.setLayout(layout_ans2)
RadioGroupBox.setLayout(layout_ans3)

#
# Створюємо панель(рамку) із результатом тексту:
#

AnsGroupBox = QGroupBox("Результат тексту:")
lb_Result = QLabel('') # надпис - перекладу - результату
lb_Correct = QLabel('') # вірно чи ні

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res) # додаємо макет до рамки
AnsGroupBox.hide()

# розташуємо всіх віджетів у вікні

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout() 

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel("хвилини"))

layout_line2.addWidget(lb_Question,alignment=(Qt.AlignCenter | Qt.AlignVCenter))

layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK,stretch=2)
layout_line4.addStretch(1)

layout_cards = QVBoxLayout()
layout_cards.addLayout(layout_line1, stretch=1)
layout_cards.addLayout(layout_line2, stretch=2)
layout_cards.addLayout(layout_line3, stretch=8)

layout_cards.addStretch(1)
layout_cards.addLayout(layout_line4, stretch=1)
layout_cards.addStretch(1)
layout_cards.setSpacing(5)

main_wind.setLayout(layout_cards)

main_wind.show()
app.exec_()
