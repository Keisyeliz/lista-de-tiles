import os
os.system('cls')

var_totalGFlt =0
cons_libretaInt = 5000
cons_borradorInt = 1000
cons_reglaInt = 1000
cons_lapizInt = 1500
cons_morralInt = 300000
cons_coloresInt = 60000
cons_uniformesInt = 200000
var_nombreStr = input('Nombre del estudiante ->')
var_contactoStr = input('Contacto del estudiante ->')
var_direccionStr = input('direccion del estudiante ->')
var_presupuestoFlt = float(input('presupueto ->'))
var_controlBln = True
while var_controlBln ==True:
    os.system('cls')
    print('cliente:  ',var_nombreStr)
    var_opcionStr = int(input('<<<MENÚ DE OPCIONE>>>\n\n1. libretas\n2. borrador\n3. regla\n4. lapiz\n5. morral\n6. colores\n7. uniformes\n8. salir\n ->'))
    if var_opcionStr >1 and var_opcionStr <=7:
        var_cantidadInt = int(input('cantidad ->'))

    if var_opcionStr == 1:
        var_totalGFlt += (var_cantidadInt * cons_libretaInt)

    if var_opcionStr == 2:
        var_totalGFlt += (var_cantidadInt * cons_borradorInt)

    if var_opcionStr == 3:
        var_totalGFlt += (var_cantidadInt * cons_reglaInt)

    if var_opcionStr == 4:
        var_totalGFlt += (var_cantidadInt * cons_lapizInt)

    if var_opcionStr == 5:
        var_totalGFlt += (var_cantidadInt * cons_morralInt)

    if var_opcionStr == 6:
        var_totalGFlt += (var_cantidadInt * cons_coloresInt)

    if var_opcionStr == 7:
        var_totalGFlt += (var_cantidadInt * cons_uniformesInt)

    if var_opcionStr == 8:
        print('El total a pagar es $',var_totalGFlt)
        if var_presupuestoFlt >= var_totalGFlt:
          print('Gracias por su compra')
        else:
             print('No tienes fondos suficiente para realizar tu compra')
        var_controlBln = False