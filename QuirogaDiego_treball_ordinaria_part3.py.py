import sqlite3
#obrir la biblioteca "sqlite3"
conexió = sqlite3.connect("Notes.db")
#cream una connexió
cursor = conexió.cursor()
#cream un cursor
taula = cursor.execute("SELECT * FROM Notes")
#seleccionam tota la taula
llista = taula.fetchall()
#assignam la taula a una variable
print (llista[0][3:])
estudiant = 0
qualificacions = 3
#cream variables auxiliars
while estudiant < len(llista[0]):
    #iniciam el primer bucle
     suma = 0
     while qualificacions < len(llista[0][3:])+3:
        #iniciam segon bucle
         suma += llista[estudiant][qualificacions]
         #actualitzam la nota
         qualificacions +=1
     suma = suma/(qualificacions-3)
    #calculam la mitjana
     qualificacions = 3
     estudiant +=1
     print("Mitjana alumne",llista[estudiant-1][1],"és",suma,"\n")
    #imprimim la mitjana
     matriu.append(llista[estudiant-1][1])
     #afegim l'alumne a la matriu principal
     apunts.append(suma)
matriu2 = [matriu,apunts]
auxiliar = 0

for i in matriu2[1]:
     #iniciam bucle for
   if i >= 0 and i <= 2.49:
     print("l'estudiant",matriu2[0][auxiliar],"és novell \n")
   elif i > 2.49 and i <= 6.24:
     print("l'estudiant",matriu2[0][auxiliar],"aprenent \n")
   elif i > 6.24 and i <= 8.74:
     print("l'estudiant",matriu2[0][auxiliar],"avançat \n")
     #classificam els estudiants segons el nivell
   else:
     print("l'estudiant",matriu2[0][auxiliar],"expert \n" ) 
#classificam la nota segons el nivell
