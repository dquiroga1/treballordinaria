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
     diccionari[llista[estudiant-1][1]] = suma
print(diccionari)
#mostram el nom dels alumnes i les seves mitjanes en forma de matriu
