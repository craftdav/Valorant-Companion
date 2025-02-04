from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea
from PySide6.QtGui import QPixmap, QGuiApplication, QFont
from PySide6.QtCore import Qt
import os
from lineup_ui import Ui_MainWindow
from lineup_loader import load_lineups
from actions import setup_agent_action

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Qt template használata
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Görgethető terület
        self.scroll_area = self.ui.scrollArea
        self.scroll_area.hide()

        # Logo létrehozása és elhelyezése
        self.logoPixmap = QPixmap("assets/VC-Logo.png").scaled(261, 261, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_label = QLabel(self)
        self.logo_label.setPixmap(self.logoPixmap)
        self.logo_label.setScaledContents(False)
        self.logo_label.resize(self.logoPixmap.size())
        self.logo_label.move(0, 21)

        # Menü gombok action beállítások
        self.setup_actions()

        # Home menüben home gomb lenyomásakor 
        self.ui.actionHome.triggered.connect(lambda: self.returnHome())
        
        # Indításkor
        self.returnHome()

    # FÜGGVÉNYEK

    def showLineups(self, agent, map, site):

        self.scroll_area.show()
        self.scroll_widget = QWidget()
        
        scroll_layout = load_lineups(agent, map, site, self)
        if scroll_layout:
            self.scroll_widget.setLayout(scroll_layout)
        else:
            self.scroll_widget.setLayout(QVBoxLayout())  # Üres ha nincs lineup
        
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setWidgetResizable(True)
        self.setCentralWidget(self.scroll_area)
        self.logo_label.hide()


    def returnHome(self):
        self.scroll_area.hide()
        self.logo_label.show()
    
    def setup_actions(self):
        setup_agent_action(self.ui, self.showLineups)

# App execution
app = QApplication([])
screen_geometry = QGuiApplication.primaryScreen().geometry()  # 🔹 Képernyő mérete
window = MyApp()
window.setGeometry(screen_geometry)  # 🔹 Beállítja a méretet
window.showMaximized()
app.exec()