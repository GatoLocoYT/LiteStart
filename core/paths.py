from pathlib import Path


BASE_DIR = Path(
    __file__
).resolve().parent.parent

ASSETS_DIR = (
    BASE_DIR / "assets"
)

CONFIG_DIR = (
    BASE_DIR / "config"
)

STYLES_DIR = (
    BASE_DIR / "styles"
)