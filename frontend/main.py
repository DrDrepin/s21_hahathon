
from JSONData import JSONData
#import ItemModel
from ItemModel import ItemModel
from UI.UI import Ui_MainWindow


from PyQt6.QtWidgets import QApplication, QMainWindow, QListView
from PyQt6.QtCore import Qt, QModelIndex
from PyQt6.QtGui import QPixmap


import sys
from functools import partial 

def showImgUpper(w: Ui_MainWindow, data: JSONData):
    #a = l
    def showImgInner(item: QModelIndex):
        nonlocal w
        nonlocal data

        #w.outImage.setText("ADASDASDASD")
        img = data.getElem(item.row())["data"]
        if img:
        #w.outImage.setPixmap(item.data(Qt.ItemDataRole.DecorationRole).pixmap(200, 200))
            qp = QPixmap()
            qp.loadFromData(img)
            w.outImage.setPixmap(qp)
        else:
            qp = QPixmap()
            w.outImage.setPixmap(qp)



    return showImgInner

def getUpPageUpper(w: Ui_MainWindow, data: JSONData):
    #a = l
    def showImgInner(item: QModelIndex):
        nonlocal w
        nonlocal data

        #w.outImage.setText("ADASDASDASD")
        img = data.getElem(item.row())["data"]
        if img:
        #w.outImage.setPixmap(item.data(Qt.ItemDataRole.DecorationRole).pixmap(200, 200))
            qp = QPixmap()
            qp.loadFromData(img)
            w.outImage.setPixmap(qp)
        else:
            qp = QPixmap()
            w.outImage.setPixmap(qp)



    return showImgInner




def tesst(s: str, item: QModelIndex):
    print(str, item)


f = open("icons/images.jpeg", "rb")
t = f.read()
f.close()

json = [
    {"path": "/asda/file.txt", "data": None},
    {"path": "/asda/fil", "data": None     },
    {"path": "/asda/filaaa", "data": None  },
    {"path": "/asda/imposter.png", "data": t},
    {"path": "/asda/morozilka.tar", "data": None}  
]

if __name__ == "__main__":
    print(type(t))
    app = QApplication(sys.argv)
    model = ItemModel()
    data = JSONData()

    data.set_data(json)
    data.processAllData(model.addElement)





    main = QMainWindow()
    window = Ui_MainWindow()
    window.setupUi(main)
    window.listFiles.setModel(model)
#    window.listFiles.clicked.connect()
#    model.takeRow()
    showImg = showImgUpper(window, data)
    window.listFiles.clicked.connect(showImg)
    #window.upButton.clicked.connect(partial(tesst, s="Ppaapa"))
    
   # print("SHHHTOOOO")
   # main.show()
    main.show()

    app.exec()