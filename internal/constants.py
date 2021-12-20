from pathlib import Path

INTERNAL_DIR ="/root/web/internal"
MAP_INFO_DIR = "/root/web/data/addmap_data/map_data.json"
ADDMAP_DATA_DIR ="/root/web/data/addmap_data"
CARTDATA_DIR = "/root/web/internal/static/cartdata"

CART_WEB_DIR_LOCAL = Path('.').absolute().as_posix() + "/cartogram-web"
INTERNAL_DIR_LOCAL = CART_WEB_DIR_LOCAL + "/internal"
ADDMAP_DATA_DIR_LOCAL = CART_WEB_DIR_LOCAL +  "/data/addmap_data"
MAP_INFO_DIR_LOCAL = ADDMAP_DATA_DIR_LOCAL + "/map_data.json"