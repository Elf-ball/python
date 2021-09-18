# -*- coding: utf-8 -*-

from windowpyqt5.untitled import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import json
# from mylog import LogAssistant


class QueryWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # init函数，每次调用query_window类时，会自动调用此函数
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.query_formula)
        # 给button 的 点击动作绑定一个事件处理函数

    def query_formula(self):
        # 获取下拉列表当前选中的值
        hj = self.ui.comboBox.currentText()
        plug = self.ui.comboBox_2.currentText()
        print("您选择的插件为：", plug)
        path = "E:\\插件安装包\\{file_path}\\1.1.0\\install.json"
        f = open(path.format(file_path=plug), 'r')
        info = f.read()
        json_data = json.loads(info)
        version = json_data["version"]
        f.close()
        # 将读取到的version，填充到plainTextEdit中
        self.ui.plainTextEdit.setPlainText(version)
        # 最后一句不为pyqt5中的方法时，执行完程序就会自动关闭弹框（原因未知）
        QtWidgets.QMessageBox.information(self, "提示", "您选择的环境为:" + hj)


# 使用以下代码才能成功调用界面函数
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QueryWindow()
    window.show()
    sys.exit(app.exec_())
