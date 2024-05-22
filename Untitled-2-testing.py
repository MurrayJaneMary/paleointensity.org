
import os
file_path = 'C:/Users/murray98/Documents/Paleointensity/MD_phenom_mod/Phenom_mod_ZIP/modres_customT19_lambda001_parallel_B1.th'
if not os.path.isfile(file_path):
    raise FileNotFoundError(f"File not found: {file_path}")
