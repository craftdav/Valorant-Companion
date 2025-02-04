import os
import sys

def get_resource_path(relative_path):
    """ Visszaadja az adatfájlok helyes elérési útját PyInstaller környezetben """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # PyInstaller ideiglenes mappa
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Példa a helyes elérési út használatára
path = get_resource_path("Valorant-Companion/")

"""
rmdir /s /q build
rmdir /s /q dist
del main.spec
pyinstaller --onefile --distpath app --workpath app/temp main.py
"""
