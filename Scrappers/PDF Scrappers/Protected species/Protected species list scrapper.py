import os
import tabula
#list of protected species: https://zzps.rs/podzakonska-akta/

#import pdf
raw_path=r"C:\Users\Lenovo\Zotero\storage\PNDTTR2X\Maja Karaman et al. - 2023 - Biodiversity of fungal species from Tara Mountain .pdf"
os_path=raw_path.replace('\\', '/')
file_path = os.path.abspath(os_path)


#tabula.convert_into(file_path, "prilog1_raw.csv", output_format="csv")

df = tabula.read_pdf(file_path, pages = '3-14')

tabula.convert_into(file_path, "checklist_raw.csv", output_format="csv", pages='3-14')

print(df)
