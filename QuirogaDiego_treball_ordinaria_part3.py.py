import sqlite3
apunts = []
matriu = []
diccionari = {}
conexió = sqlite3.connect("Notes.db")
cursor = conexió.cursor()
taula = cursor.execute("SELECT * FROM Notes")
llista = taula.fetchall()
print (llista)
estudiant = 0
qualificacions = 3
print(len(llista))
while estudiant < len(llista):
     
     suma = 0
     while qualificacions < len(llista[0][3:])+3: 
         suma += llista[estudiant][qualificacions]
         qualificacions +=1
     suma = suma/(qualificacions-3)
     qualificacions = 3
     estudiant +=1
     
     print("Mitjana alumne",llista[estudiant-1][1],"és",suma,"\n")
     matriu.append(llista[estudiant-1][1])
     apunts.append(suma)
matriu2 = [matriu,apunts]
auxiliar = 0
for i in matriu2[1]:
   if i >= 0 and i <= 2.49:
     print("l'estudiant",matriu2[0][auxiliar],"és novell \n")
   elif i > 2.49 and i <= 6.24:
     print("l'estudiant",matriu2[0][auxiliar],"aprenent \n")
   elif i > 6.24 and i <= 8.74:
     print("l'estudiant",matriu2[0][auxiliar],"avançat \n")
   else:
     print("l'estudiant",matriu2[0][auxiliar],"expert \n" ) 