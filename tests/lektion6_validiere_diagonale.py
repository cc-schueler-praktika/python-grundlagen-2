from math import sqrt
import sys

try:
    a
except: 
    print('❌ Du hast die Variable a nicht definiert.')
    sys.exit()
    
try:
    b
except: 
    print('❌ Du hast die Variable b nicht definiert.')
    sys.exit()

try:
    diagonale
except: 
    print('❌ Du hast die Variable diagonale nicht definiert.')
    sys.exit()

try:
    assert diagonale == sqrt(a**2 + b**2), "Du hast die Diagonale nicht richtig berechnet. Überprüfe deine Rechnung. Die Formel für die Diagonale kannst du im Internet nachschauen."  
except AssertionError as inst:
    print ("❌ " + str(inst))
    sys.exit()
 
print("✅ Sehr gut!")