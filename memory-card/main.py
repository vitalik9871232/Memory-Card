from main_window import *
from menu import *

def switch_screen():
    if btn_OK.text() == 'Відповісти':
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Наступне запитання')
    else:
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_OK.setText('Відповісти')
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

main_wind.show()
app.exec_()