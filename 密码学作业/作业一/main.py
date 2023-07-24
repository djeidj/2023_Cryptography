import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from ui import Ui_Form
import analysis

mapping_table = {}

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.submit_key_button.clicked.connect(self.update_mapping_table)

        self.ui.decode_button.clicked.connect(self.decode_suggestions)

        self.ui.ciphertext.setPlaceholderText("输入密文")
        self.ui.plaintext.setPlaceholderText("输出明文")
        self.ui.mapping_table.setPlaceholderText("这里是所有26个英文字母的映射")
        self.ui.pre_image.setPlaceholderText("密钥-明文")
        self.ui.image.setPlaceholderText("密钥-密文")
        self.ui.suggestions.setPlaceholderText("解密建议")
        self.ui.mapping_table.setText('abcdefghijklmnopqrstuvwxyz')

    def update_mapping_table(self):
        global mapping_table

        pre_image = self.ui.pre_image.text()
        image = self.ui.image.text()
        ciphertext = self.ui.ciphertext.toPlainText()

        try:
            if len(pre_image)!=len(image):
                raise Exception("像与原像长度不一致")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
        
        try:
            if len(set(pre_image))!=len(pre_image) or len(set(image))!=len(image):
                raise Exception("映射有错误")
            elif (not pre_image.isalpha() or not image.isalpha()) and len(pre_image)!=0:
                raise Exception("映射中应该只有英文")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

        mapping_table = analysis.update_part_table(pre_image, image, mapping_table)
        word_list = analysis.get_frequence_word(ciphertext)
        char_dict = analysis.get_frequence_chr(word_list)
        temp_table = analysis.update_all_table(char_dict, mapping_table)

        key=''
        for i in temp_table:
            key+=temp_table[i]
        
        self.ui.mapping_table.setText(key)
        

        

    def decode_suggestions(self):
        global mapping_table
        ciphertext = self.ui.ciphertext.toPlainText()
        key = self.ui.mapping_table.text()

        #  解密
        temp_table = {chr(x) : key[x-ord('a')] for x in range(ord('a'), ord('z')+1)}
        plaintext = analysis.decode(ciphertext, temp_table)
        self.ui.plaintext.setText(plaintext)

        #  给出建议
        word_list = analysis.get_frequence_word(ciphertext)
        char_dict = analysis.get_frequence_chr(word_list)
        twochr_dict = analysis.get_frequence_twochr(word_list)
        thrchr_dict = analysis.get_frequence_thrchr(word_list)

        suggestion = ''
        suggestion += '英文中单个字母频率从大到小排列' + '\n' + str(analysis.frequence_chr_list) +'\n'
        suggestion += '本文中单字母频率从大到小排列' + '\n' + str(list(char_dict.keys())) + '\n'
        suggestion += '英文中双字母组合频率从大到小排列' + '\n' + str(analysis.frequence_twochr_list) +'\n'
        suggestion += '本文中双字母频率从大到小排列' + '\n' + str(list(twochr_dict.keys())) + '\n'
        suggestion += '英文中三字母组合频率从大到小排列' + '\n' + str(analysis.frequence_thrchr_list) +'\n'
        suggestion += '本文中三字母组合频率从大到小排列' + '\n' + str(list(thrchr_dict.keys())) + '\n'

        self.ui.suggestions.setText(suggestion)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())