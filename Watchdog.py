import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src.Excel_Reader import Excel_Functions
from src.modbus_server import Server_Functions


# Specify the folder to monitor
folder_to_monitor = "C:/Users/Jose/OneDrive - The Automation Clinic Ltd/Desktop/Projects/Watchdog_Script/Test_Folder"
# Specify the columns format of the document
columns_to_check = ["name", "ID"]
data_to_send = columns_to_check[1]


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        file_path = event.src_path
        file_extension = os.path.splitext(file_path)[1]
        print(file_extension)
        # Ignore temporary files created by Microsoft Excel
        if file_path.startswith("~$"):
            return
        else:
            if file_extension.lower() == ".xlsx":
                print(f"A new Excel file has been created! File Name: {file_path}")
                verify = Excel_Functions.verified_doc(file_path, columns_to_check)
                if verify:
                    data = Excel_Functions.organize_data(file_path, data_to_send)
                    server = Server_Functions.run_server_sent_data(data)
                    print(server)
                else:
                    print('Error with data')
            else:
                print(f"A new file has been created! File Name: {file_path}")

def monitor_folder(folder_path):
    # Create an event handler instance
    event_handler = MyHandler()

    # Create an observer instance
    observer = Observer()

    # Schedule the event handler to monitor the specified folder path for created files
    observer.schedule(event_handler, path=folder_path, recursive=False)

    # Start the observer to begin monitoring
    observer.start()

    try:
        # Keep the script running and checking for events until interrupted by the user
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # If the user presses Ctrl+C, stop the observer
        observer.stop()

    # Wait for the observer to complete before exiting
    observer.join()

if __name__ == "__main__":
    while True:
        # Start monitoring the folder for new files
        monitor_folder(folder_to_monitor)
