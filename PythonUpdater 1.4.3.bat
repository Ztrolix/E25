@echo off
title Python Updater
cls
:start

set python_ver=36

python ./get-pip.py --user
python get-pip.py --user

cd \
cd \python%python_ver%\Scripts\
py -m pip install --upgrade pip --user
py -m pip install pip --upgrade --user
py -m pip install setuptools -U --user
py -m pip install xlrd --user
py -m pip install XlsxWriter --user
set DISTUTILS_USE_SDK=1 --user
set MSSdk=1 --user
git clone https://github.com/pygame/pygame.git --user
cd pygame --user
py -m pip install setuptools requests wheel numpy -U --user
py -m buildconfig --download --user
python -m buildconfig --download --user
py -m pip install setup.py --user
py -m pip install pyproject.toml --user
py -m pip install pygame.examples.aliens --user
py -m pip install -U wheel --user
py -m pip install wheel --user
py -m pip install -U pygame --user
py -m pip install pygame --user
py -m pip install -U pygame --pre --user
py -m pip install pygame --pre --user
py -m pip install pandas --user
py -m pip install NumPy --user
py -m pip install Matplotlib --user
py -m pip install Seaborn --user
py -m pip install scikit-learn --user
py -m pip install Requests --user
py -m pip install urllib3 --user
py -m pip install NLTK --user
py -m pip install Pillow --user
py -m pip install pytest --user
py -m pip install Pendulum --user
py -m pip install Python Imaging Library --user
py -m pip install MoviePy --user
py -m pip install PyQt --user
py -m pip install Pywin32 --user
py -m pip install tqdm --user
py -m pip install --upgrade pip setuptools wheel --user
py -m pip install --upgrade pip --user
py -m pip install --user --upgrade twine --user
py -m pip install --user --upgrade twine upload --user
py -m pip install --user --upgrade twine upload ZtrolixLib/ --user
py -m pip install ZtrolixLib --user
py -m pip install pgzero --user
py -m pip install adventurelib --user
py -m pip install panda3d --user
py -m pip install arcade --user
py -m pip install --upgrade pip setuptools virtualenv --user
python -m virtualenv kivy_venv --user
py -m virtualenv kivy_venv --user
py -m pip install "kivy[base]" kivy_examples --user
py -m pip install "kivy[base]" kivy_examples --no-binary kivy --user
py -m pip install "kivy[base] @ https://github.com/kivy/kivy/archive/master.zip" --user
py -m pip install --pre "kivy[base]" kivy_examples --user
py -m pip install kivy --pre --no-deps --index-url  https://kivy.org/downloads/simple/ --user
py -m pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple/ --user
git clone git://github.com/kivy/kivy.git --user
cd kivy --user
py -m pip install -e ".[dev,full]" --user
python setup.py build_ext --inplace --user
py setup.py build_ext --inplace --user
py -m pip install pyinstaller --user
py -m pip install PySide2 --user
py -m pip install PySide2 --pre --user
git clone https://code.qt.io/pyside/pyside-setup
cd pyside-setup
git branch --track 5.12 origin/5.12
git checkout 5.12
python setup.py install --qmake=<path/to/qmake/> --parallel=8 --build-tests
7z x .../libclang-release_60-windows-vs2015_64-clazy.7z
SET LLVM_INSTALL_DIR=%CD%\libclang
py -m pip install PySide2 --user
py -m pip install PySide2 --pre --user
py -m pip install PySide6 --user
py -m pip install pyinstaller --user
py -m pip install AppOpener --user
py -m pip install PyQt5 --user
py -m pip install pigar --user
py -m pip install pipreqs --user
py -m pip freeze > requirements.txt --user
@echo -------------
@echo Click enter to close instalation.
@echo -------------
@pause
exit