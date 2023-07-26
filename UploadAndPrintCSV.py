#Importiere die auf der Folie genannte Bibliothek
from google.colab import files

#Öffne einen Dateidialog und speichere die Datei in einer Variablen

uploaded_files = files.upload()

for filename, file_content in uploaded_files.items():
 print(file_content)

#Gebe jede Zeile auf der Konsole aus Tipp: vgl. vorherige Aufgaben
