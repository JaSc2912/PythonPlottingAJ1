import numpy as np
#lies eine Zahl aus der Konsole ein
radius = input("Gib einen Radius für deinen Kreis ein")
#füge oben die benötigten imports hinzu
pi = np.pi
#erstelle eine pi Variable mithilfe der NumPy Bibliothek
fi = pi*radius*radius
#Berechne den Flächeninhalt des Kreises Tipp: pi*r²
print("Der Flaecheninhalt beträgt: "+fi)
#Gib das Ergebnis auf der Konsole aus