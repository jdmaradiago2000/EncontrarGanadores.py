from base import Process
import csv
from collections import OrderedDict
from operator import getitem

final_list = {}
porcentajes =[]

class File(Process):
    def __init__(self, files):
        self.files = files
      
    def open_files(self, files):
        """Este método requiere por parametros la lista de archivos
        Args:
            files(list): listas de quiz realizados
        Returns:
            list[dict]: informacion agrupada de archivos .csv
        """
        list_join = []
        for i in self.files:
            with open(i, encoding="utf-8") as csv_file:
                file_to_process = csv.DictReader(csv_file)
                for i in file_to_process:
                    name = i["First Name"].lower() + " " + \
                        i["Last Name"].lower()
                    score = int(i["Score"])
                    string_list = (i["Accuracy"]).split()
                    accuracy = int(string_list[0])
                    list_join.append(
                        {"name": name, "score": score, "accuracy": accuracy})
        return list_join
    
    def process_file(self, list_join):
        """Este método requiere la lista (list_join) que es retornada por el método open_files(), esta lista contiene la informacion agrupada de archivos .csv
        Args:
            list_join (list): lista de diccionarios
        Returns:
            dict: Retorna un diccionario con la informacion procesada
        """

        self.list_join = self.open_files(list_join)
        for i in list_join:
            if i["name"] in final_list.keys():
                final_list[i["name"]]["score"] += i["score"]
                final_list[i["name"]]["accuracy"] += i["accuracy"]
            else:
                final_list[i["name"]] = {"score": i["score"], "accuracy": i["accuracy"]}

        if "diego angeles" in final_list.keys():
            final_list["diego angeles"]["score"] += 2000

        if "kevin salvador casas" in final_list.keys():
            final_list["kevin salvador casas"]["score"] += 8000
   
        return final_list

    def process_seventy(self, final_list):
        """Requiere dict: datos informacion procesada 
        Args:
            final_list
        Returns:
            dict: Un diccionario con las personas que obtuvieron un porcentaje de acierto mayor al 70%.
        """
        seventy = {}
        for i in final_list:
            final_list[i]["accuracy"] = (final_list[i]["accuracy"])/4
            if final_list[i]["accuracy"] >= 70:
                seventy[i] = final_list[i]
                seventy[i]["accuracy"] = str(seventy[i]["accuracy"]) + "%"
        print(f"Las personas con porcentaje mayor a 70% son: {seventy}")
        return seventy

    def sorted_files(self,final_list):
        """Requiere dict: datos informacion actualizada
        Args:
            dict(dict): Diccionario con valores actualizados
        Returns:
            str: Los nombres y puntajes obtenidos en los quiz de los 2 primeros lugares.
        """
        self.final_list = final_list
        res = sorted(final_list.items(), key=lambda x: x[1]["score"], reverse=True)
        return (f"El ganador es: {res[0]}, el segundo lugar es para: {res[1]}")

 
