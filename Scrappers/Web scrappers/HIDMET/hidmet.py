import urllib.request
from datetime import datetime, timedelta
import time
import threading
import sys
import os

# Variable for stopping infinite loop
run = True

def download_images():
    global run
    
    # Image URLs
    rs_comp_url = "https://www.hidmet.gov.rs/data/satelitska_slika/Srbija_com_1.png"
    eu_comp_url = "https://www.hidmet.gov.rs/data/satelitska_slika/Evropa_com_1.png"
    
    while run:
        try:
            # Current_datetime
            current_datetime = datetime.now()
            # Turn datetime into string
            dt_string = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
            dt_left = datetime.now() + timedelta(hours=1)
            dt_left_string = dt_left.strftime("%H:%M:%S")
            # Download images
            urllib.request.urlretrieve(rs_comp_url, 
                                   f"rs_satellite_comp_{dt_string}.png")
            urllib.request.urlretrieve(eu_comp_url, 
                                   f"eu_satellite_comp_{dt_string}.png")

            print(f"Images downloaded successfully. Next image will be taken at {dt_left_string}")
            time.sleep(3600)
    
        except KeyboardInterrupt:
            print('KeyboardInterrupt: Script terminated')
            run = False
            break
            
    
def loading_animation():
    # Defining animation characters
    animation_chars = ['|', '/', '-', '\\']
    # Infinite loop
    try:
        while True:
            for char in animation_chars:
                print("Waiting..." + char, end = '\r')
                time.sleep(0.1)  # Adjust the delay for desired animation speed
    except KeyboardInterrupt:
        pass


try:
    # Start thread for animation
    animation_thread = threading.Thread(target=loading_animation)
    animation_thread.start()
    
    # Define and start thread for downloading
    download_thread = threading.Thread(target=download_images)
    download_thread.start()

    download_thread.join()

except KeyboardInterrupt:
    run = False
    print('KeyboardInterrupt: Script terminated')

finally:
    run = False
    animation_thread.join()
