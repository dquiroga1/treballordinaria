import sqlite3
conexió = sqlite3.connect("Notes.db")
cursor = conexió.cursor()
taula = cursor.execute("SELECT * FROM Notes")
llista = taula.fetchall()
print (llista[0][3:])
estudiant = 0
qualificacions = 3
while estudiant < len(llista[0]):
    
     suma = 0
     while qualificacions < len(llista[0][3:])+3:
        
         suma += llista[estudiant][qualificacions]
         qualificacions +=1
     suma = suma/(qualificacions-3)
     qualificacions = 3
     estudiant +=1
     print("Mitjana alumne",llista[estudiant-1][1],"és",suma,"\n")