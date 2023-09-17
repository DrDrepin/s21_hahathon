from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QListView
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon, QPixmap
from PyQt6.QtCore import Qt

from os import path


class ItemModel(QStandardItemModel):
    def __init__(self, currPath="/"):
        super(ItemModel, self).__init__()

        self.currentPath = currPath

        self.__folderIcon = QIcon(path.join('icons', 'folder.png'))
        self.__fileIcon = QIcon(path.join('icons', 'file.png'))
        self.__offset = 0
        self.__step = 15

        #self.json = None

    def addElement(self, filePath: str, img: bytes = None, imgPath: str = None):
        fileName = self.__getFileName(filePath)

        it = QStandardItem(fileName)
        
      

        icon = None
        if img:
            qp = QPixmap()
            qp.loadFromData(img)
            icon = QIcon(qp)
        else:
            icon = self.__determineStdIcon(fileName)

            

        # it.setData(QtGui.QIcon(os.path.join('images', 'bao{}.png'.format(i))),        # +++
        #                            QtCore.Qt.DecorationRole)
        
        it.setIcon(icon)
        self.appendRow(it)
        #it.setData(icon, Qt.ItemDataRole.DecorationRole) 
        
        
        
    #private
    def __determineStdIcon(self, file: str):
        if '.' in file:
            return self.__fileIcon
        else: 
            return self.__folderIcon

    def __getFileName(self, filepath: str):
        tmp = filepath.split("/")
        l = len(tmp)

        return tmp[l - 1]
    
    def setOffset(self, offset: int):
        self.__offset = offset
    