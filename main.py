from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            if filename.endswith(".pdf") or filename.endswith(".html"):
                folder_destination = r"C:\Users\sebas\OneDrive\Desktop\Downloads_folder\PDF_Folder"
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)
            elif filename.endswith(".png") or filename.endswith(".jpg"):
                folder_destination = r"C:\Users\sebas\OneDrive\Desktop\Downloads_folder\Image_Folder"
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)
            elif filename.endswith(".zip") or filename.endswith(".rar"):
                folder_destination = r"C:\Users\sebas\OneDrive\Desktop\Downloads_folder\Archive_Folder"
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)
            elif filename.endswith(".exe"):
                folder_destination = r"C:\Users\sebas\OneDrive\Desktop\Downloads_folder\Executables_Folder"
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)
            elif filename.endswith(".txt"):
                folder_destination = r"C:\Users\sebas\OneDrive\Desktop\Downloads_folder\TXT_Folder"
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)
            elif filename.endswith(".mp4") or filename.endswith(".wav") or filename.endswith(".mov") or \
                    filename.endswith(".mkv"):
                folder_destination = r"C:\Users\sebas\OneDrive\Desktop\Downloads_folder\MP4_WAV_Folder"
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)
            elif filename.endswith(".xlsx") or filename.endswith(".ods"):
                folder_destination = r"C:\Users\sebas\OneDrive\Desktop\Downloads_folder\Excel_Folder"
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)
            elif filename.endswith(".docx") or filename.endswith(".doc"):
                folder_destination = r"C:\Users\sebas\OneDrive\Desktop\Downloads_folder\Word_Folder"
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)
            else:
                pass


# paths valid when running script from windows terminal
folder_to_track = r"C:\Users\sebas\Downloads"

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
