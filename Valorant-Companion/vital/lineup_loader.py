import os
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtCore import Qt

def load_lineups(agent, map, site, parent):
    path = f"assets/Lineups/{agent}/{map}/{site}/"
    if not os.path.exists(path):
        return None

    lu_list = os.listdir(path)
    scroll_layout = QVBoxLayout()

    for i in range(len(lu_list)//3):
        # Képek betöltése
        pixmapStart = QPixmap(os.path.join(path, f"{agent}-{map}-{site}-{i+1}-Aim.png"))
        pixmapAim = QPixmap(os.path.join(path, f"{agent}-{map}-{site}-{i+1}-Start.png"))
        pixmapFinish = QPixmap(os.path.join(path, f"{agent}-{map}-{site}-{i+1}-Finish.png"))

        # Ellenőrzés
        if pixmapStart.isNull():
            print(f"HIBA: Nem sikerült betölteni a képet: {os.path.join(path, f'{agent}-{map}-{site}-{i+1}-Aim.png')}")
        if pixmapAim.isNull():
            print(f"HIBA: Nem sikerült betölteni a képet: {os.path.join(path, f'{agent}-{map}-{site}-{i+1}-Start.png')}")
        if pixmapFinish.isNull():
            print(f"HIBA: Nem sikerült betölteni a képet: {os.path.join(path, f'{agent}-{map}-{site}-{i+1}-Finish.png')}")


        # Szöveg betöltése
        text = ""
        try:
            with open(os.path.join(path, f"{agent}-{map}-{site}-{i+1}-Text.txt"), encoding="utf-8") as f:
                text = "".join(f.readlines())
        except FileNotFoundError:
            pass

        if not pixmapStart.isNull() and not pixmapAim.isNull() and not pixmapFinish.isNull():
            # 🔹 Képminőség javítása
            pixmapStart = pixmapStart.scaled(1024, 576, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            pixmapAim = pixmapAim.scaled(512, 288, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            pixmapFinish = pixmapFinish.scaled(512, 288, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            # 🔹 QLabel létrehozása a főablakhoz kapcsolva
            aim_label = QLabel(parent)
            aim_label.setPixmap(pixmapStart)

            start_label = QLabel(parent)
            start_label.setPixmap(pixmapAim)

            finish_label = QLabel(parent)
            finish_label.setPixmap(pixmapFinish)

            # 🔹 Szöveg QLabel formázással
            textLabel = QLabel(parent)
            textLabel.setText(text)
            textFont = QFont()
            textFont.setBold(True)
            textFont.setPointSize(26)
            textLabel.setFont(textFont)
            textLabel.setWordWrap(True)  # 🔹 Több soros szöveg megjelenítés
            textLabel.setMaximumWidth(450)

            # Layout létrehozása
            row_layout = QHBoxLayout()
            small_row = QVBoxLayout()

            row_layout.addWidget(aim_label)  # Bal oldalra a nagy kép
            small_row.addWidget(start_label) # Jobb oldalra a két kis kép
            small_row.addWidget(finish_label)
            row_layout.addLayout(small_row)

            row_layout.addWidget(textLabel)  # 🔹 Szöveg hozzáadása

            scroll_layout.addLayout(row_layout)

    # 🔹 Placeholder képek hozzáadása, ha kevesebb mint 4 lineup van
    if len(lu_list) < 5:
        placeholderPixmap = QPixmap("assets/placeholder.png").scaled(1024, 576, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        miniPlaceholder = placeholderPixmap.scaled(512, 288, Qt.KeepAspectRatio, Qt.SmoothTransformation)


        placeholder = QLabel(parent)
        placeholder.setPixmap(placeholderPixmap)

        miniplaceholder1 = QLabel(parent)
        miniplaceholder2 = QLabel(parent)
        miniplaceholder1.setPixmap(miniPlaceholder)
        miniplaceholder2.setPixmap(miniPlaceholder)

        row_layout = QHBoxLayout()
        placeholderLayout = QVBoxLayout()

        row_layout.addWidget(placeholder)  # Bal oldali nagy placeholder
        placeholderLayout.addWidget(miniplaceholder1)
        placeholderLayout.addWidget(miniplaceholder2)
        row_layout.addLayout(placeholderLayout)

        scroll_layout.addLayout(row_layout)
        lu_list.append("placeholder")  # Elkerüljük a végtelen ciklust

    return scroll_layout
