from pathlib import Path
from .common_data_elements_schema import *

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "common_data_elements_schema.yaml"
