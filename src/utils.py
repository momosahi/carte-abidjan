import geopandas as gpd
import yaml
import logging


def import_config(path: str) -> dict:
    try:
        with open(path, "r") as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        logging.error(f"File {path} not found")
    return config


def import_data(path: str) -> gpd.GeoDataFrame:
    try:
        data = gpd.read_file(path)
    except FileNotFoundError:
        logging.error(f"File {path} not found")
    return data
