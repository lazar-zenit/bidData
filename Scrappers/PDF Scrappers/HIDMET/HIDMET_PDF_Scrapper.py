import os
import time
import tabula
import pandas as pd

#start the timer
start=time.time()

file_path=os.path.abspath(
    "Z:/Programiranje/PDF_scrapper/HIDMET_source/Meteoroloski godisnjak 1 - klimatoloski podaci - 2022.pdf")

tabula.convert_into(file_path, "output.csv", output_format="csv", pages='138')

end=time.time()
print('Time elapsed (minutes):', round((end-start)/60, 2), '\n', 'Time elapsed (seconds):', round(end-start, 2))
