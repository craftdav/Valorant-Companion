from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QScrollArea
from PySide6.QtGui import QPixmap, QGuiApplication, QFont
from PySide6.QtCore import Qt
from vital.lineup_ui import Ui_MainWindow
from vital.lineup_loader import load_lineups
from vital.actions import setup_agent_action
from vital.lineup_loader import lineupCounter
import os
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        screen = QGuiApplication.primaryScreen()  # az elsődleges képernyő
        geometry = screen.geometry()              # QRect objektum: x, y, width, height

        self.width = geometry.width()
        self.height = geometry.height()

        self.showedPics = []
        self.showedPixmaps = []

        self.scroll_area = self.ui.scrollArea
        self.scroll_area.hide()

        current_file_path = os.path.abspath(__file__)
        per=len(current_file_path)-1
        while True:
            if current_file_path[per] !="\\":
                per-=1
            else:
                break
        current_file_path=current_file_path[0:per]

        logo_path = "assets/VC-Logo.png"
        self.logoPixmap = QPixmap(logo_path)
        self.logo_label = QLabel(self)
        self.logo_label.setPixmap(self.logoPixmap)
        self.logo_label.move(0, 21)

        self.countLabel = QLabel(self)
        self.counted_lineups=lineupCounter()
        self.countLabel.setText(str(self.counted_lineups))
        self.countLabel.move(0,21)
        self.countFont = QFont()
        self.countFont.setBold(True)
        self.countFont.setPointSize(100)
        self.countLabel.setFont(self.countFont)
        self.countLabel.setFixedSize(150,150)

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
        
        loaded = load_lineups(agent, map, site, [self.width,self.height], self)
        scroll_layout = loaded[0]
        self.showedPics = loaded[1]
        self.showedPixmaps = loaded[2]

        self.scroll_widget.setLayout(scroll_layout if scroll_layout else QVBoxLayout())
        
        self.scroll_area.setWidget(self.scroll_widget)
        self.setCentralWidget(self.scroll_area)
        self.logo_label.hide()
        self.countLabel.show()

    def returnHome(self):
        self.scroll_area.hide()
        self.logo_label.show()
        self.countLabel.show()
        self.setCentralWidget(self.logo_label)
    
    def setup_actions(self):
        setup_agent_action(self.ui, self.showLineups)
    
app = QApplication([])
screen_geometry = QGuiApplication.primaryScreen().geometry()
window = MyApp()
window.setGeometry(screen_geometry)
window.showMaximized()
app.exec()
