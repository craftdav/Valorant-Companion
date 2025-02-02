from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea
from PySide6.QtGui import QPixmap, QGuiApplication
from PySide6.QtCore import Qt
import os
from lineup_ui import Ui_MainWindow

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
        self.logoPixmap = QPixmap("Valorant-Companion/VC-Logo.png").scaled(261, 261, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_label = QLabel(self)
        self.logo_label.setPixmap(self.logoPixmap)
        self.logo_label.setScaledContents(False)
        self.logo_label.resize(self.logoPixmap.size())
        self.logo_label.move(0, 21)


        # Yoru menüben x gomb lenyomásakor
        self.ui.actionYoruAbyssA.triggered.connect(lambda: self.showLineups("Abyss","A"))
        self.ui.actionYoruAbyssB.triggered.connect(lambda: self.showLineups("Abyss","B"))
        self.ui.actionYoruAscentA.triggered.connect(lambda: self.showLineups("Ascent","A"))
        self.ui.actionYoruAscentB.triggered.connect(lambda: self.showLineups("Ascent","B"))
        self.ui.actionYoruBindA.triggered.connect(lambda: self.showLineups("Bind", "A"))
        self.ui.actionYoruBindB.triggered.connect(lambda: self.showLineups("Bind", "B"))
        self.ui.actionYoruBreezeA.triggered.connect(lambda: self.showLineups("Breeze","A"))
        self.ui.actionYoruBreezeA.triggered.connect(lambda: self.showLineups("Breeze","B"))
        self.ui.actionYoruFractureA.triggered.connect(lambda: self.showLineups("Fracture","A"))
        self.ui.actionYoruFractureB.triggered.connect(lambda: self.showLineups("Fracture","B"))
        #self.ui.actionYoruHaven.triggered.connect(lambda: self.showLineups("Heaven"))
        #self.ui.actionYoruPearl.triggered.connect(lambda: self.showLineups("Pearl"))

        # Home menüben home gomb lenyomásakor 
        self.ui.actionHome.triggered.connect(lambda: self.returnHome())
        
        # Indításkor
        self.returnHome()









    # FÜGGVÉNYEK

    def showLineups(self, map, site):

        # Scroll area reset
        self.scroll_area.show()
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)  
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setWidgetResizable(True)
        self.setCentralWidget(self.scroll_area)
        
        # Előző oldalak eltűntetése
        self.logo_label.hide()

        path = "Valorant-Companion/Lineups/Yoru/" + map + "/" + site + "/"
        lu_list = os.listdir(path) # line-up lista

        for i in range(0,len(lu_list),3):
            # Kép betöltése
            pixmapStart = QPixmap(os.path.join(path, lu_list[i]))
            pixmapAim = QPixmap(os.path.join(path, lu_list[i+1]))
            pixmapFinish = QPixmap(os.path.join(path, lu_list[i+2]))
            if not pixmapStart.isNull() and not pixmapAim.isNull() and not pixmapFinish.isNull():
                pixmapStart = pixmapStart.scaled(1024, 576, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                pixmapAim = pixmapAim.scaled(512, 288, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                pixmapFinish = pixmapFinish.scaled(512, 288, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                
                # Nagy QLabel a képhez
                aim_label = QLabel(self)
                aim_label.setPixmap(pixmapStart)
                aim_label.setScaledContents(False)
                aim_label.resize(pixmapStart.size())



                # Kis QLabel a start és finish-hez
                start_label = QLabel(self)
                start_label.setPixmap(pixmapAim)
                finish_label = QLabel(self)
                finish_label.setPixmap(pixmapFinish)
                # Sorba rendezés (QHBoxLayout)
                row_layout = QHBoxLayout()
                small_row =QVBoxLayout()

                row_layout.addWidget(aim_label)  # Bal oldalon

                small_row.addWidget(start_label)# Jobb oldalon
                small_row.addWidget(finish_label)

                row_layout.addLayout(small_row)


                # Hozzáadjuk a fő vertikális layout-hoz
                self.scroll_layout.addLayout(row_layout)
                
                # if len(lu_list)<4:
                #     placeholder=QLabel(self)
                #     placeholderPixmap = QPixmap("PySideLearn/Valorant-Companion/placeholder.png")
                #     placeholderPixmap = placeholderPixmap.scaled(1024, 576, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                #     placeholder.setPixmap(placeholderPixmap)
                #     row_layout.addWidget(placeholder)

                #     miniplaceholder = QLabel(self)
                #     placeholderLayout=QVBoxLayout()
                #     placeholderPixmap = placeholderPixmap.scaled(512, 288, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                #     miniplaceholder.setPixmap(placeholderPixmap)
                #     placeholderLayout.addWidget(miniplaceholder)
                #     placeholderLayout.addWidget(miniplaceholder)
                    
                #     row_layout.addLayout(placeholderLayout)
                #     self.scroll_layout.addWidget(row_layout)

    def returnHome(self):
        self.scroll_area.hide()
        self.logo_label.show()

        




# App execution
app = QApplication([])
screen_geometry = QGuiApplication.primaryScreen().geometry()  # 🔹 Képernyő mérete
window = MyApp()
window.setGeometry(screen_geometry)  # 🔹 Beállítja a méretet
window.showMaximized()
app.exec()

