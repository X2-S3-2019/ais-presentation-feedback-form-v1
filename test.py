import os
import tkinter as tk
from tkinter import filedialog

def setFolder():
	application_window = tk.Tk()
	try:
		application_window.withdraw()
		application_window.update()
		file_path = filedialog.askdirectory(
						parent=application_window,
						initialdir=os.getcwd(),
						title="Please select a folder:")
		application_window.quit()
		print(file_path)
	except Exception as e:
		print(e)
		return False
	return True


setFolder()