import urllib.request
from datetime import datetime, timedelta
import time
import threading
import signal

exit_event = threading.Event()

def signal_handler(signum, frame):
    exit_event.set()
    print("Script terminated \n", 
          "Please close command prompt")

def download_images():
    # Image URLs
    rs_comp_url = "https://www.hidmet.gov.rs/data/satelitska_slika/Srbija_com_1.png"
    eu_comp_url = "https://www.hidmet.gov.rs/data/satelitska_slika/Evropa_com_1.png"
    while not exit_event.is_set():
        # Current_datetime
        current_datetime = datetime.now()
        
        # Turn datetime into string
        dt_string = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        dt_left = datetime.now() + timedelta(hours=1)
        dt_left_string = dt_left.strftime("%H:%M:%S")
        
        # Download images
        urllib.request.urlretrieve(rs_comp_url, f"rs_satellite_comp_{dt_string}.png")
        urllib.request.urlretrieve(eu_comp_url, f"eu_satellite_comp_{dt_string}.png")
        print(f"Images downloaded successfully. Next image will be taken at {dt_left_string}")
        time.sleep(3600)
        if exit_event.is_set():
            break
        
    
def loading_animation():
    # Defining animation characters
    animation_chars = ['|', '/', '-', '\\']
    
    # Infinite loop
    while not exit_event.is_set():
        for char in animation_chars:
            print("Waiting..." + char, end = '\r')
            time.sleep(0.1)  # Adjust the delay for desired animation speed
        # Break the loop when exit_event is set (KeyboardInterrupt)
        if exit_event.is_set():
            break
        

# Wait for the signal
signal.signal(signal.SIGINT, signal_handler)
    
# Define threads
download_thread = threading.Thread(target=download_images)
animation_thread = threading.Thread(target=loading_animation)

# Define daemons
download_thread.daemon = True
animation_thread.daemon = True


# Start thread
download_thread.start()
animation_thread.start()

# Thread waits for a bit    
while True:
    pass

# Wait for function to finnish before it quits
download_thread.join()
animation_thread.join()