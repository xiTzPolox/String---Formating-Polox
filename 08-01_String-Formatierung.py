
"""
Aufgabe 08-01: String-Formatierung

1.
Benutzen Sie die .format()-Methode, um sich die korrekten Kasusformen für die  
lateinische a-Deklination und o-Deklination (Maskulinum und Neutrum) ausgeben 
zu lassen.

- a-Deklination:
https://de.wikipedia.org/wiki/O-Deklination#Erste_Deklination_(a-Deklination)
- o-Deklination:
https://de.wikipedia.org/wiki/O-Deklination#Zweite_Deklination_(o-Deklination)

2.
Entwickeln Sie eine Funktion, die genau ein lateinisches Nomen in der Nominativ-    #aimca, amicus, pensum
form entgegen nimmt und 
   1. in Abhängigkeit von dessen Endung entscheidet, welche Deklination für #Nominativform defnieren
      dieses Wort angewendet werden muss und 
   2. die zutreffenden Deklinationsformen für das jeweilige Nomen ausgibt.

3.
Wenden Sie Ihre neue Funktion auf die Nomen amica, amicus, und pensum an.

Tipp: 
- Speichern Sie die Kasusbezeichnung und die zugehörigen Endungen in Dictionarys
  ab.
- Benutzen Sie zum Erkennen der Wortendung die String-Methode .endswith()
  https://docs.python.org/3/library/stdtypes.html
- Recherchieren Sie auf https://pyformat.info, wie Sie die Ausgabe wie gezeigt
  ausrichten können:

Beispielausgabe:

Eingabe:    amica

Ausgabe:
Nominativ:  amica
Genitiv:    amicae
Dativ:      amicae
Akkusativ:  amicam
Ablativ:    amica
"""
"""
def der_deklinierer(eingabewort):         #für 2 und 3 benutzbar
    a_deklination = {"TO":"DO"}          #erstmal nur SG einsetzen und testen  #für jede Deklination gucken ob das drin ist
    o_deklination_maskulinum = {"TO":"DO"}
    o_deklination_neutrum = {"TO":"DO"}
    if eingabewort.endswith("TO-DO"):
        endung = "TO-DO"
        stamm = "TO-DO"
        richtige_deklination = "TO-DO"
    #elif: TO-DO
    #elif: TO-DO
    else:
        ausgabe = "Dieses Wort kann ich nicht verarbeiten. Sorry.")
        return ausgabe
 

Hier muss noch die Ausgabe für das return-Statement unten gebaut werden-
         Vielleicht mit einer Schleife?

    return "TO-DO"
"""

#1
femininSG = {"Nominativ": "a", "Genitiv": "ae", "Dativ": "ae", "Akkusativ": "am", "Ablativ": "a"}
femininPL = {"Nominativ": "ae", "Genitiv": "arum", "Dativ": "is", "Akkusativ": "as", "Ablativ": "is"}
maskulinSG = {"Nominativ": "us", "Genitiv": "i", "Dativ": "o", "Akkusativ": "um", "Ablativ": "o", "Vokativ": "e"}
maskulinPL = {"Nominativ": "i", "Genitiv": "orum", "Dativ": "is", "Akkusativ": "os", "Ablativ": "is", "Vokativ": "i"}
neutrumSG = {"Nominativ": "um", "Genitiv": "i", "Dativ": "o", "Akkusativ": "um", "Ablativ": "o", "Vokativ": "um"}
neutrumPL = {"Nominativ": "a", "Genitiv": "orum", "Dativ": "is", "Akkusativ": "a", "Ablativ": "is", "Vokativ": "a"}
"""
print("Hier stehen die Singular Endungen des Femininums.")
for word in femininSG:
  output = "Der Kasus lautet {} und besitzt eine '{}'-Endung".format(word, femininSG[word])
  print(output)
print("-----")
print("Hier stehen die Plural Endungen des Femininums.")
for word in femininPL:
  output = "Der Kasus lautet {} und besitzt eine '{}'-Endung".format(word, femininPL[word])
  print(output)
print("-----")
print("Hier stehen die Singular Endungen des Maskulinums.")
for word in maskulinSG:
  output = "Der Kasus lautet {} und besitzt eine '{}'-Endung".format(word, maskulinSG[word])
  print(output)
print("-----")
print("Hier stehen die Plural Endungen des Maskulinums.")
for word in maskulinPL:
  output = "Der Kasus lautet {} und besitzt eine '{}'-Endung".format(word, maskulinPL[word])
  print(output)
print("-----")
print("Hier stehen die Singular Endungen des Neutrums.")
for word in neutrumSG:
  output = "Der Kasus lautet {} und besitzt eine '{}'-Endung".format(word, neutrumSG[word])
  print(output)
print("-----")
print("Hier stehen die Plural Endungen des Neutrums.")
for word in neutrumPL:
  output = "Der Kasus lautet {} und besitzt eine '{}'-Endung".format(word, neutrumPL[word])
  print(output)
"""
#a_deklination = {"NominativSG": "a", "GenitivSG": "ae", "DativSG": "ae", "AkkusativSG": "am", "AblativSG": "a"}
a_deklination = femininSG
o_deklination_maskulinum = maskulinSG
o_deklination_neutrum = neutrumSG

def der_deklinierer(eingabewort):        
    a_deklination = femininSG        
    o_deklination_maskulinum = maskulinSG
    o_deklination_neutrum = neutrumSG
    if eingabewort.endswith((a_deklination.get("Nominativ")):
        endung = a_deklination("Nominativ")
        stamm = eingabewort[:-1]
        richtige_deklination = femininSG
    elif eingabewort.endswith((o_deklination_maskulinum.get("Nominativ")):
        endung = o_deklination_maskulinum("Nominativ")
        stamm = eingabewort[:-1]
        richtige_deklination = maskulinSG
    elif eingabewort.endswith((o_deklination_neutrum.get("Nominativ")):
        endung = o_deklination_neutrum.get("Nominativ")
        stamm = eingabewort[:-1]
        richtige_deklination = neutrumSG
    else:
        ausgabe = "Dieses Wort kann ich nicht verarbeiten. Sorry.")
        return ausgabe
 

Hier muss noch die Ausgabe für das return-Statement unten gebaut werden-
         Vielleicht mit einer Schleife?

    return "TO-DO"










