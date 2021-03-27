from PySide2 import QtWidgets
from PySide2.QtCore import QEvent
from PySide2.QtGui import QPixmap, Qt, QIcon
from PySide2.QtWebSockets import QWebSocket

from resources.resources import DataMgr
from src.qt.com.qtimg import QtImgMgr
from src.util import Log
from ui.chatrootmsg import Ui_ChatRoomMsg


class QtChatRoomMsg(QtWidgets.QWidget, Ui_ChatRoomMsg):
    def __init__(self):
        super(self.__class__, self).__init__()
        Ui_ChatRoomMsg.__init__(self)
        self.setupUi(self)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setWindowFlag(Qt.Dialog)
        self.resize(400, 100)

        p = QPixmap()
        p.loadFromData(DataMgr().GetData("placeholder_avatar"))
        self.commentLabel.installEventFilter(self)
        self.picLabel.installEventFilter(self)
        self.label.installEventFilter(self)
        self.label.setText("")
        self.data = None
        self.picData = None
        self.audioData = None
        self.picLabel.setPixmap(p)
        self.picLabel.setCursor(Qt.PointingHandCursor)
        self.picLabel.setScaledContents(True)
        self.picLabel.setAttribute(Qt.WA_TranslucentBackground)
        self.commentLabel.setWordWrap(True)
        # self.setStyleSheet("""
        #     background:transparent;
        #     border:2px solid red;
        # """)
        self.widget.setStyleSheet(""".QWidget{
            border-image:url(resources/skin_aio_friend_bubble_pressed.9.png) 50;
            border-top-width: 10px;
            border-right-width: 10px;
            border-bottom-width: 10px;
            border-left-width: 10px;
            }
            """)
        self.replayLabel.setWordWrap(True)
        self.replayLabel.setStyleSheet("""
            border-image:url(resources/skin_aio_friend_bubble_pressed.9.png) 50;
            border-top-width: 20px;
            border-right-width: 20px;
            border-bottom-width: 10px;
            border-left-width: 20px;
            """)
        # self.commentLabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
        # self.name.setTextInteractionFlags(Qt.TextSelectableByMouse)
        p = QPixmap()
        p.loadFromData(DataMgr().GetData("audio"))
        self.toolButton.setIcon(QIcon(p))

    def SetPicture(self, data):
        pic = QPixmap()
        pic.loadFromData(data)
        self.picData = data
        self.picLabel.setPixmap(pic)

    def SetHeadPicture(self, data):
        pic = QPixmap()
        pic.loadFromData(data)
        self.label.setCursor(Qt.PointingHandCursor)
        self.label.setScaledContents(True)
        self.label.setAttribute(Qt.WA_TranslucentBackground)
        self.label.setPixmap(pic)

    def SetPictureComment(self, data):
        pic = QPixmap()
        pic.loadFromData(data)
        self.data = data
        newPic = pic.scaled(200, 300, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.commentLabel.setCursor(Qt.PointingHandCursor)
        self.commentLabel.setScaledContents(True)
        self.commentLabel.setAttribute(Qt.WA_TranslucentBackground)
        self.commentLabel.setPixmap(newPic)
        self.commentLabel.setMinimumSize(newPic.width(), newPic.height())

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.LeftButton:
                if self.picData and (obj == self.label or obj == self.picLabel):
                    QtImgMgr().ShowImg(self.picData)
                elif self.data and obj == self.commentLabel:
                    QtImgMgr().ShowImg(self.data)
                return True
            else:
                return False
        else:
            return super(self.__class__, self).eventFilter(obj, event)