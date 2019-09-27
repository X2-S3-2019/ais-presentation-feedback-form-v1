# ais-presentation-feedback-form-v1
Version 1 of Feedback Form for presentations of AIS students. This project was developed for SOFT808 (Software User Experience).


#### install python 2.7
#### install pip

#### python packages 
##### pip install eel
##### pip install docx-mailmerge
##### pip install PyInstaller




###### for developer : python accessment.py 
###### for package:
1. windows: pyinstaller .\accessment.py --onefile --noconsole --hidden-import bottle_websocket --add-data C:\Users\Admin\scoop\apps\python27\current\lib\site-packages\eel\eel.js;eel --add-data .\web\;.\web\
2. mac/unix: pyinstaller accessment.py --onefile --noconsole --hidden-import bottle_websocket --add-data /usr/local/lib/python2.7/site-packages/eel/eel.js:eel --add-data web:web 



