import os
import sys
import base64



def get_resource_path(relative_path):
    """ Visszaadja az adatfájlok helyes elérési útját PyInstaller környezetben """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # PyInstaller ideiglenes mappa
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Példa a helyes elérési út használatára
path = get_resource_path("")
ipath = os.path.join(path, "assets", "Lineups")
encoded_path = os.path.join(path,"assets", "encoded")

# Végigmegyünk az assets/Lineups teljes fájlszerkezetén
for root, dirs, files in os.walk(ipath):
    # Az eredeti struktúra megtartásához kinyerjük a relatív elérési utat
    relative_root = os.path.relpath(root, ipath)
    encoded_dir = os.path.join(encoded_path, relative_root)

    # Létrehozzuk a megfelelő mappát az encoded könyvtárban
    os.makedirs(encoded_dir, exist_ok=True)

    # Végigmegyünk az összes fájlon a mappán belül
    for file in files:
        source_file = os.path.join(root, file)
        encoded_file = os.path.join(encoded_dir, file + ".txt")

        # Base64 kódolás és mentés
        with open(source_file, "rb") as img, open(encoded_file, "w") as f:
            encoded_data = base64.b64encode(img.read()).decode("utf-8")
            f.write(encoded_data)
            f.close()
print("Minden fájl sikeresen átkonvertálva és mentve az encoded mappába!")




