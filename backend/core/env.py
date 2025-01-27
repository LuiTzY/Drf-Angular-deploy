from pathlib import Path
from environ import Env

env =  Env()

#Buildeamos el BASE DIR desde este archivo
BASE_DIR = Path(__file__).resolve().parent.parent

print(f"Este es la ruta base del proyecto {BASE_DIR}")