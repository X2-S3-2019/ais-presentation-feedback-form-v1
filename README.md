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

use auto-py-to-exe: 

pyinstaller -y -F -w --add-data "C:/projects/ais-presentation-feedback-form-v1/template/Template.docx";"template" --add-data "C:/Users/Admin/scoop/apps/python27/current/Lib/site-packages/eel/eel.js";"eel" --add-data "C:/projects/ais-presentation-feedback-form-v1/web";"web/" --hidden-import bottle_websocket  "C:/projects/ais-presentation-feedback-form-v1/accessment.py"



pyinstaller -y -F -w 
--add-data "C:/projects/ais-presentation-feedback-form-v1/template/Template.docx";"template"
--add-data "C:/Users/Admin/scoop/apps/python27/current/Lib/site-packages/eel/eel.js";"eel" 
--add-data "C:/projects/ais-presentation-feedback-form-v1/web";"web/" 
--hidden-import bottle_websocket  
"C:/projects/ais-presentation-feedback-form-v1/accessment.py"

