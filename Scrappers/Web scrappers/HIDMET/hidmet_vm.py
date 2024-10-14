import urllib.request
from datetime import datetime

def download_images():
    # Image URLs
    rs_comp_url = "https://www.hidmet.gov.rs/data/satelitska_slika/Srbija_com_1.png"
    eu_comp_url = "https://www.hidmet.gov.rs/data/satelitska_slika/Evropa_com_1.png"
    
    # Current_datetime
    current_datetime = datetime.now()
        
    # Turn datetime into string
    dt_string = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    
    # Download images
    urllib.request.urlretrieve(rs_comp_url, f"rs_satellite_comp_{dt_string}.png")
    urllib.request.urlretrieve(eu_comp_url, f"eu_satellite_comp_{dt_string}.png")
    
download_images()