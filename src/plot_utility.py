import pandas as pd
import glob
import numpy as np

from src.parser import get_iso_results
from src.parser import create_abs_path


def create_matrix(string):
    """
    careful! you don't know the order of the MG! The OG are sorted by name.
    :param string: (relative) path of dictionary
    :return: Matrix with 0 and 1
    """
    M = []
    path = create_abs_path(string)
    list_of_files = glob.glob(path + "/*.txt")  # abs path of all txt files in the folder

    # sort files by class
    list_of_files = sorted(list_of_files, key=last_27chars)

    for file in list_of_files:
        value = get_iso_results(file)
        M.append(value)
    M = np.array(M)  # row: OG, columns: MG
    M = M.transpose()  # row: MG, columns: OG
    return M


def last_27chars(string):
    return string[-27:]
