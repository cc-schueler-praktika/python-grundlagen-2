import sys

try:
    summe
except: 
    print('❌ Du hast die Summe nicht definiert.')
    sys.exit()
    
try:
    wuerfel_1
except: 
    print('❌ Du hast die Variable wuerfel_1 nicht definiert.')
    sys.exit()

try:
    wuerfel_2
except: 
    print('❌ Du hast die Variable wuerfel_2 nicht definiert.')
    sys.exit()
    
try:
    wuerfel_3
except: 
    print('❌ Du hast die Variable wuerfel_3 nicht definiert.')
    sys.exit()

try:
    assert summe >= 3 and summe <= 18, "Die Summe muss zwischen 3 und 18 liegen! Würfel können nur die Werte zwischen 1 und 6 annehmen."
except AssertionError as inst:
    print ("❌ " + str(inst))
    sys.exit()

try:
    assert summe == wuerfel_1 + wuerfel_2 + wuerfel_3, "Du hast die Summe nicht richtig berechnet. Addiere die 3 Würfel."
except AssertionError as inst:
    print ("❌ " + str(inst))
    sys.exit()
 
print("✅ Sehr gut!")