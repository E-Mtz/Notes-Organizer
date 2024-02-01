import os
from os import listdir
from shutil import move
from fnmatch import fnmatch
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

downloads = "C:/Users/Esteban/Downloads"

class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        files = listdir(downloads)
        Exam1 = ["A.2", "A.3", "1.1", "1.3", "A.6", "A.4", "2.4", "A.5", "1.4", "1.6", "1.7", "1.5"]
        Exam2 = ["2.1", "2.2", "2.3", "2.5", "2.7", "1.8", "1.9", "3.1", "3.2", "3.3", "3.4", "3.5"]
        Exam3 = ["4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7", "5.1", "5.3", "5.4", "5.5"]
        FinalExam = ["6.1", "6.2", "6.3", "6.4", "7.1", "7.2"]

        for file in files:
            if fnmatch(file, "Section*.pdf"):
                section = ".".join(x for x in file if x.isdigit() or x == 'A')
                if section in Exam1:
                    destination = "E:/School/College/YR1S1/MATH 150/Notes/Exam 1"
                    move(file, destination)
                elif section in Exam2:
                    destination = "E:/School/College/YR1S1/MATH 150/Notes/Exam 2"
                    move(file, destination)
                elif section in Exam3:
                    destination = "E:/School/College/YR1S1/MATH 150/Notes/Exam 3"
                    move(file, destination)
                elif section in FinalExam:
                    destination = "E:/School/College/YR1S1/MATH 150/Notes/Final Exam"
                    move(file, destination)
                else:
                    continue


if __name__ == "__main__":
    path = downloads
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()