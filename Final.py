#Importiere die benötigten Bibliotheken pandas und matplotlib​
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from google.colab import files
#Öffne einen Dateidialog, um eine CSV-Datei hochzuladen​
uploaded_files = files.upload()
#Lies die hochgeladene CSV-Datei mit Pandas ein​
pd.read_csv(next(iter(uploaded_files)))
#Gib die ersten Zeilen des DataFrames aus, um sicherzustellen, dass die Daten richtig eingelesen wurden​
print(df.head())
#Plotte die Daten aus dem DataFrame mit Matplotlib​

# plt.figure(figsize=(10, 6))  # Größe des Plots festlegen
plt.plot(df.index, df['Werte'], marker='o', linestyle='-')  # Daten plotten mit Index als x-Achse und 'Werte' als y-Achse
# plt.xlabel('Index')  # Beschriftung der x-Achse
# plt.ylabel('Werte')  # Beschriftung der y-Achse
# plt.title('CSV-Datenplot')  # Titel des Plots
# plt.grid(True)  # Gitter anzeigen
plt.show()  # Plot anzeigen
