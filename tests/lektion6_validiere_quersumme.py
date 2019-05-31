from math import sqrt
import sys

try:
    quersumme(1)
except: 
    print("❌ Deine Funktion ist nicht korrekt benannt. Nenne sie quersumme.")
    sys.exit()
    
try:
    qs = quersumme(1)
    assert qs == 1, "Die Quersumme von 1 ist nicht " + str(qs)
except AssertionError as inst:
    print ("❌ " + str(inst))
    sys.exit()
    
try:
    qs = quersumme(17)
    assert qs == 8, "Die Quersumme von 17 ist nicht " + str(qs)
except AssertionError as inst:
    print ("❌ " + str(inst))
    sys.exit()

try:
    qs = quersumme(100000000001)
    assert qs == 2, "Die Quersumme von 100000000001 ist nicht " + str(qs)
except AssertionError as inst:
    print ("❌ " + str(inst))
    sys.exit()
 
print("✅ Sehr gut!")