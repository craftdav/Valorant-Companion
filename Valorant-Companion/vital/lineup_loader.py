import os
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtCore import Qt

def load_lineups(agent, map, site, monitor_size, parent):
    path = f"assets/Lineups/{agent}/{map}/{site}/"
    if not os.path.exists(path):
        return None
    trap_list=[]
    if os.path.exists(os.path.join(path,"Trap")):
        trap_path=os.path.join(path,"Trap")
        path=os.path.join(path,"Lineup")
    
        trap_list = os.listdir(trap_path)
        trap_list.sort(key=len)
        trap_notes=0
        for i in range(len(trap_list)):
            if trap_list[i].lower().endswith(".txt"):
                trap_notes+=1

    lu_list = os.listdir(path)
    loaded_pics=[]
    loaded_pixmaps=[]
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
            pixmapStart = pixmapStart.scaled(monitor_size[0]//2, monitor_size[1]//2, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            pixmapAim = pixmapAim.scaled(monitor_size[0]//4, monitor_size[1]//4, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            pixmapFinish = pixmapFinish.scaled(monitor_size[0]//4, monitor_size[1]//4, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            # 🔹 QLabel létrehozása a főablakhoz kapcsolva
            aim_label = QLabel(parent)
            aim_label.setPixmap(pixmapStart)
            loaded_pics.append(aim_label)
            loaded_pixmaps.append(pixmapAim)

            start_label = QLabel(parent)
            start_label.setPixmap(pixmapAim)
            loaded_pics.append(start_label)
            loaded_pixmaps.append(pixmapStart)

            finish_label = QLabel(parent)
            finish_label.setPixmap(pixmapFinish)
            loaded_pics.append(finish_label)
            loaded_pixmaps.append(pixmapFinish)

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

    for i in range(len(trap_list)-trap_notes):
        pixmapTrap = QPixmap(os.path.join(trap_path, f"{agent}-{map}-{site}-{i+1}-Trap.png"))

        if pixmapTrap.isNull():
            print(f"HIBA: Nem sikerült betölteni a képet: {os.path.join(trap_path, f'{agent}-{map}-{site}-{i+1}-Trap.png')}")
        
        text = ""
        try:
            with open(os.path.join(trap_path, f"{agent}-{map}-{site}-{i+1}-TrapText.txt"), encoding="utf-8") as f:
                text = "".join(f.readlines())
        except FileNotFoundError:
            pass

        if not pixmapTrap.isNull():
            # 🔹 Képminőség javítása
            pixmapTrap = pixmapTrap.scaled(monitor_size[0], monitor_size[1], Qt.KeepAspectRatio, Qt.SmoothTransformation)


            # 🔹 QLabel létrehozása a főablakhoz kapcsolva
            trap_label = QLabel(parent)
            trap_label.setPixmap(pixmapTrap)
            loaded_pics.append(trap_label)
            loaded_pixmaps.append(pixmapTrap)


            # 🔹 Szöveg QLabel formázással
            textLabel = QLabel(parent)
            textLabel.setText(text)
            textFont = QFont()
            textFont.setBold(True)
            textFont.setPointSize(26)
            textLabel.setFont(textFont)
            textLabel.setWordWrap(True)  # 🔹 Több soros szöveg megjelenítés
            textLabel.setMaximumWidth(450)

            row_layout = QHBoxLayout()
            row_layout.addWidget(trap_label)
            row_layout.addWidget(textLabel)

            scroll_layout.addLayout(row_layout) 

    # 🔹 Placeholder képek hozzáadása, ha kevesebb mint 4 lineup van
    if len(lu_list) < 5 and len(trap_list)==0:
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

    return [scroll_layout,loaded_pics,loaded_pixmaps]

def lineupCounter():
    # Ez a path pontosan ugyanaz, mint a load_lineups()-ban
    lineups_path = "assets/Lineups"

    if not os.path.exists(lineups_path):
        print(f"Nem található a Lineups mappa: {os.path.abspath(lineups_path)}")
        return 0

    counted = 0
    agents = os.listdir(lineups_path)
    
    for agent in agents:
        agent_path = os.path.join(lineups_path, agent)
        if not os.path.isdir(agent_path):
            continue
        places = os.listdir(agent_path)

        for place in places:
            place_path = os.path.join(agent_path, place)
            if not os.path.isdir(place_path):
                continue
            sites = os.listdir(place_path)

            for site in sites:
                site_path = os.path.join(place_path, site)
                if not os.path.isdir(site_path):
                    continue
                if "Trap" in os.listdir(site_path):
                    types= os.listdir(site_path)
                    for type in types:
                        type_path=os.path.join(site_path,type)
                        pics = os.listdir(type_path)
                        for pic in pics:
                            if pic.lower().endswith("p.png"):
                                counted += 3
                            elif pic.lower().endswith(".png"):
                                counted +=  1

                else:
                    pics = os.listdir(site_path)
                    

                    for pic in pics:
                        if pic.lower().endswith("p.png"):
                            counted += 3
                        elif pic.lower().endswith(".png"):
                            counted +=  1

    return counted // 3