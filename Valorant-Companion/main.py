from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QScrollArea
from PySide6.QtGui import QPixmap, QGuiApplication
from PySide6.QtCore import Qt
import os
from vital.lineup_ui import Ui_MainWindow
from vital.lineup_loader import load_lineups
from vital.actions import setup_agent_action

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scroll_area = self.ui.scrollArea
        self.scroll_area.hide()

        self.logoPixmap = QPixmap("assets/VC-Logo.png")
        self.logo_label = QLabel(self)
        self.logo_label.setPixmap(self.logoPixmap)
        self.logo_label.move(0, 21)

        self.setup_actions()
        self.ui.actionHome.triggered.connect(self.returnHome)
        self.returnHome()

    def showLineups(self, agent, map, site):
        try:
            if self.scroll_area is None or not self.scroll_area.isVisible():
                self.scroll_area = QScrollArea(self)
                self.scroll_area.setWidgetResizable(True)
                self.ui.scrollArea = self.scroll_area
                self.scroll_area.hide()
        except:
            self.scroll_area = QScrollArea(self)
            self.scroll_area.setWidgetResizable(True)
            self.ui.scrollArea = self.scroll_area
            self.scroll_area.hide()

        self.scroll_area.show()
        self.scroll_widget = QWidget()
        
        scroll_layout = load_lineups(agent, map, site, self)
        self.scroll_widget.setLayout(scroll_layout if scroll_layout else QVBoxLayout())
        
        self.scroll_area.setWidget(self.scroll_widget)
        self.setCentralWidget(self.scroll_area)
        self.logo_label.hide()

    def returnHome(self):
        self.scroll_area.hide()
        self.logo_label.show()
        self.setCentralWidget(self.logo_label)
    
    def setup_actions(self):
        setup_agent_action(self.ui, self.showLineups)
    
    def resizeEvent(self, event):
        new_size = min(self.width(), self.height()) * 0.5
        scaled_pixmap = self.logoPixmap.scaled(new_size, new_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        
        self.logo_label.setPixmap(scaled_pixmap)
        self.logo_label.resize(scaled_pixmap.size())
        self.logo_label.move((self.width() - self.logo_label.width()) // 2, 
                             (self.height() - self.logo_label.height()) // 2)
        
        super().resizeEvent(event)

app = QApplication([])
screen_geometry = QGuiApplication.primaryScreen().geometry()
window = MyApp()
window.setGeometry(screen_geometry)
window.showMaximized()
app.exec()
