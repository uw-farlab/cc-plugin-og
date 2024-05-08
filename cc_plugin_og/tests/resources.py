"""
cc_plugin_og/tests/resources.py
"""
import importlib
import subprocess


def get_filename(path):
    """
    Returns the path to a valid dataset
    """
    filename = importlib.resources.files("cc_plugin_og") / path
    nc_path = filename.with_suffix(".nc")
    if not nc_path.exists():
        generate_dataset(filename, nc_path)
    return str(nc_path)


def generate_dataset(cdl_path, nc_path):
    subprocess.call(["ncgen", "-o", nc_path, cdl_path])


STATIC_FILES = {
    "good_dataset": get_filename("tests/data/good_dataset.cdl"),
    "bad_variable": get_filename("tests/data/bad_variable.cdl"),
    "bad_attribute": get_filename("tests/data/bad_attribute.cdl"),
}
