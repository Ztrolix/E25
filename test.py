from zipfile import ZipFile

with ZipFile('ZtroLib.zip', 'r') as f:
    f.extractall()