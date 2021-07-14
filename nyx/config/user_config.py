import os 
import yaml
from Ipython import get_ipython
from nyx.util import _make_dir

pkg_directory = os.path.dirname(__file__)

with open(
    os.path.join(os.path.expanduser("~"), ".nyx", "config.yml"), "r"
) as ymlfile:
    cfg = yaml.safe_load(ymlfile)

shell = get_ipython().__class__.__name__


def _make_image_dir():

    if not cfg["images"]["dir"]:
        image_dir = DEFAULT_IMAGE_DIR
    else:
        image_dir = cfg["images"]["dir"]

    _make_dir(image_dir)

    return image_dir

    