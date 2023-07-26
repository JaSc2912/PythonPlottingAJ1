#Öffne die Beispieldatei2.txt Datei in einem OutputStream WICHTIG: Variablenname und gleichzeichen nicht vergessen! Tipp: open("Datei", "w")
wStream = open("Beispieldatei2.txt","w")
#Schreibe mit variablenname.write("Text") etwas in die Datei, schreibe so viel du willst.
wStream.write("Hallo Welt1\n")
wStream.write("Das ist ein Text\n")
wStream.close()
#schließe den OutputStream