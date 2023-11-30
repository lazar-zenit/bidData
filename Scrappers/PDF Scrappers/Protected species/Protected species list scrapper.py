import os
import tabula
#list of protected species: https://zzps.rs/podzakonska-akta/

#import pdf
raw_path=r"C:\Users\Lenovo\Documents\Programiranje\bidData\Scrappers\PDF Scrappers\Protected species\Prilog1-Pravilnika-o-proglasenju-i-zastiti-strogo-zasticenih-i-zasticenih-divljih-vrsta-biljaka-zivotinja-i-gljiva.pdf"
os_path=raw_path.replace('\\', '/')
file_path = os.path.abspath(os_path)


#tabula.convert_into(file_path, "prilog1_raw.csv", output_format="csv")

df = tabula.read_pdf(file_path, pages = 'all')

tabula.convert_into(file_path, "prilog1_raw.csv", output_format="csv", pages='all')

print(df)
