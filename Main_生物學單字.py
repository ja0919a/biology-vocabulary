from PySide6.QtWidgets import QApplication,QWidget
from Ui_生物學單字 import Ui_Form
import json

class MyWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.js=json.load(open('temp.json','r'))
        
        self.chapters=[i[:-1] for i in self.js.keys()]
        self.chapters.insert(0,'全部')
        
        self.voc={}
        for i in self.js.values():
            for j in i.items():
                self.voc[j[0]]=j[1]
        
        self.vocs=[i for i in self.js.values()]
        self.vocs.insert(0,self.voc)
        
        self.voc_index=0
        self.radio_state=1
        self.push_state=0
        
        self.comboBox.addItems(self.chapters)
        self.comboBox.setCurrentIndex(0)
        
        self.lineEdit.setText('1')
        
        self.plainTextEdit_1.setPlainText(list(self.vocs[self.comboBox.currentIndex()].keys())[self.voc_index])
        self.plainTextEdit_2.setPlainText(list(self.vocs[self.comboBox.currentIndex()].values())[self.voc_index])
        self.bind()
        
    def bind(self):
        self.comboBox.currentIndexChanged.connect(self.chapter_change)
        self.radioButton_1.clicked.connect(self.radio)
        self.radioButton_2.clicked.connect(self.radio)
        self.radioButton_3.clicked.connect(self.radio)
        self.lineEdit.textEdited.connect(self.line)
        self.pushButton.clicked.connect(self.push)

    def display(self):
        self.words_label.setText('單字總數 : '+str(len(self.vocs[self.comboBox.currentIndex()])))
        self.words_label_2.setText(' / '+str(len(self.vocs[self.comboBox.currentIndex()])))
        self.lineEdit.setText(str(self.voc_index+1))
        if self.radio_state==1:
            self.plainTextEdit_1.setPlainText(list(self.vocs[self.comboBox.currentIndex()].keys())[self.voc_index])
            self.plainTextEdit_2.setPlainText(list(self.vocs[self.comboBox.currentIndex()].values())[self.voc_index])
        elif self.radio_state==2:
            if self.push_state%2==0:
                self.plainTextEdit_2.setPlainText(list(self.vocs[self.comboBox.currentIndex()].values())[self.voc_index])
                self.plainTextEdit_1.setPlainText('')
            else:
                self.plainTextEdit_1.setPlainText(list(self.vocs[self.comboBox.currentIndex()].keys())[self.voc_index])
                
        elif self.radio_state==3:
            if self.push_state%2==0:
                self.plainTextEdit_1.setPlainText(list(self.vocs[self.comboBox.currentIndex()].keys())[self.voc_index])
                self.plainTextEdit_2.setPlainText('')
            else:
                self.plainTextEdit_2.setPlainText(list(self.vocs[self.comboBox.currentIndex()].values())[self.voc_index])
    def push(self):
        if self.radio_state==1:
            self.voc_index+=1
            self.display()
        elif self.radio_state==2:
            if self.push_state==0:
                self.push_state+=1
            else:
                self.push_state=0
                self.voc_index+=1
            self.display()
        elif self.radio_state==3:
            if self.push_state==0:
                self.push_state+=1
            else:
                self.push_state=0
                self.voc_index+=1
            self.display()
        
                
            
        
    def line(self):
        self.push_state=0
        self.voc_index=int(self.lineEdit.text())-1
        self.display()

    def chapter_change(self):
        self.voc_index=0
        self.radioButton_1.setChecked(1)
        self.radio_state=1
        self.push_state=0
        self.display()
    
    def radio(self):
        self.push_state=0
        if self.radioButton_1.isChecked():
            self.radio_state=1
        elif self.radioButton_2.isChecked():
            self.radio_state=2
        elif self.radioButton_3.isChecked():
            self.radio_state=3
        self.display()

if __name__=='__main__':
    app=QApplication([])
    window=MyWindow()
    window.show()
    app.exec()