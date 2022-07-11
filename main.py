import os
from methods import File

list_files = os.listdir()
files = [file for file in list_files if file.endswith(".csv")]
obj = File(files)
abrir_archivo=obj.open_files(files)
files1=obj.process_file(abrir_archivo)
files2=obj.process_seventy(files1)
files3=obj.sorted_files(files2)
print()
print(files3)