#importaciones
import json
f = open('repertorio_funciones.json',)
menu = json.load(f)

#Listas y tuples
misa = ('funeral','boda','primera comunion')
canto = ('cortejo','entrada','senior ten piedad','gloria'\
           ,'aleluya','ofertorio','santo','cordero','comunion','salida' )

#Funciones
def imprime():
    print('-------------')
    print('\n')
    for v in menu:
        print('Titulo: ', menu[v]['titulo'])
        print('Canto de', menu[v]['canto'])
        print(menu[v]['integrantes'], ' integrantes')
        if 'recomendado' in menu[v]['tags']:
            print('*** recomendado para: ', menu[v]['tags'][0])
            print('\n\n')
        else:
            print('\n')
    print('-------------')

def preguntatipomisa():
#Despliega el menu para elegir el tipo de misa (funeral, boda, etc)
    print('Elige el tipo de misa: \n')
    for v in misa:
        print(misa.index(v),': ',v)
    requestmisa_index = int(input())
    if requestmisa_index > len(misa) or requestmisa_index < 0:
        print('no existe esa opcion')
    tipodemisa_elegido = misa[requestmisa_index]
    return tipodemisa_elegido 

def preguntaintegrantes():
#despliega el menu para elegir el numero de integrantes
    print('cuantos integrantes, presionar 0 si no te importa cuantos')
    integrantes_elegidos = int(input())
    if int(integrantes_elegidos) > 11:
        print('no tenemos misas de mas de 11 integrantes')
    return integrantes_elegidos

def preguntacanto():
#despliega el menu para elegir el canto para la misa 
   print('Elige el canto de la misa')         
   for v in canto:
       print(canto.index(v), ':', v)
   requestmisa_canto = int(input()) 
   print ('pediste: ',requestmisa_canto)
   if requestmisa_canto > len(canto) or requestmisa_canto< 0:
       print('no existe esa opcion, elige otra')
       return
   else:
       return canto[requestmisa_canto]

   
   
"""
#prueba imprime titulos para boda
print('\n\nImprime titulos para boda')
for v in menu:
    if 'boda' in menu[v]['tags']:
        imprime()

#prueba imprime titulos de boda para 3 integrantes
print('\n\nImprime titulos para boda de 3 integrantes')

for v in menu:
    if '3 integrantes' and 'boda' in menu[v]['tags']:
        imprime()
"""
