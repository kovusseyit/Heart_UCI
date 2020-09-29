import pandas as pd
import os
import zipfile
from urllib.request import urlretrieve

HEART_URL = 'https://www.kaggle.com/ronitf/heart-disease-uci/download'
filename = '33180_43520_bundle_archive.zip'

def get_heart_data(filename=filename, url=HEART_URL, force_download=False):
    """Get the Heart disease UCI data from Kaggle website
    Parameters
    ----------
    filename: string(optional)
        location to save the data
    url: string(optional)
        web location of the data
    force_download: bool(optional)
    if True force redownload of data

    Returns
    -------
    data: pandas.DataFrame
        Heart disease UCI data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
        print('Downloaded')
    
    zf = zipfile.ZipFile('33180_43520_bundle_archive.zip') 
    data = pd.read_csv(zf.open('heart.csv'))
    return data