
# Inicializa un diccionario vacio para almacenar el inventario.
# Cada producto sera una clave en el diccionario, y su valor sera otro diccionario con 'precio' y 'cantidad'.
inventario = {}

def agregar_producto(inventario_local):#definicion de la funcion
    print("\n\033[94m\033[1mAñadir Producto\033[0m")#imprimir titulo
    nombre = input("\n\033[1mIngrese el nombre del producto: ").strip()#ingresar nombre del producto(.strip para limpiar espacios)
    if nombre in inventario_local:#condicional para validar si el usuario ya existe, si existe...
        print(f"\n\033[93m El producto '{nombre}' ya existe\033[0m")#imprime mensaje que el producto ya existe
        return#retorna a pedir el nombre del producto
    while True:#bucle para ingresar precio y sus validaciones
        try:#try para validar
            precio_str = input("\n\033[1mIngrese el precio del producto: ").replace(',', '.')#ingresa precio en letras y si ingresa ","los remplaza por "."
            precio = float(precio_str)#cambia el precio en letras por un valor decimal 
            if precio < 0:#bucle para validar que el precio sea positivo
                print("\n\033[93m El precio debe ser un valor positivo.\033[0m")#mensaje que imprime una alerta
                continue#Salta la iteración actual del bucle y pasa a la siguiente.
            break#Termina el bucle prematuramente y el control del programa pasa a la siguiente instruccion
        except ValueError:#captura una excepcion que se produce cuando se le pasa un valor incorrecto a una funcion
            print("\n\033[93m Ingrese un numero valido para el precio.\033[0m")#imprime instruccion 

    while True:#bucle para ingresar cantidad con sus validaciones
        try:#empezar validaciones
            cantidad_str = input("\n\033[1mIngrese la cantidad disponible: ")#pide la cantidad en string
            cantidad = int(cantidad_str)#cambia cantidad de string a numero entero
            if cantidad < 0:#condicional para validacion cantidad sea numero positivo
                print("\n\033[93m La cantidad debe ser un valor positivo.\033[0m")#imprime advertencia
                continue#Salta la iteración actual del bucle y pasa a la siguiente.
            break#Termina el bucle prematuramente y el control del programa pasa a la siguiente instruccion
        except ValueError:#captura una excepcion que se produce cuando se le pasa un valor incorrecto a una funcion
            print("\n\033[93m Ingrese un numero entero valido para la cantidad.\033[0m")#imprime mensaje con instruccion correcta

    inventario_local[nombre] = {'precio': precio, 'cantidad': cantidad}#en el parametro (que es una blioteca),en la clave nombre guardar los valores precio y cantiad en sus respectivas claves
    print(f"\n\033[1m\033[32mEl producto '{nombre}' ha sido añadido al inventario.\033[0m")#imprime mensaje si el producto es agregado correctamente 

def consultar_producto(inventario_local):#definicion funcion para consultar producto 
    print("\n\033[94m\033[1mConsultar Producto\033[0m")#imprime titulo
    nombre = input("\n\033[1mIngrese el nombre del producto que desea consultar: ").strip()#ingresar el el nombre del producto a consultar
    if nombre in inventario_local:#condicional para validar si el usuario si esta en la biblioteca
        info_producto = inventario_local[nombre]#se crea variable para extraer los datos de biblioteca inventario y asi utilizar su info mas adelante
        precio = info_producto['precio']#con la variable info_producto se extre la clave precio dela biblioteca nombre
        cantidad = info_producto['cantidad']#con la variable info_producto se extre la clave cantidad dela biblioteca nombre
        print("\n")#espacio
        print("\033[1m" + "-" * 30 + "\033[0m")#marquetado
        print(f"\033[1m| \033[94m{'Producto':<15} \033[0m| {nombre:<12} |\033[0m")#imprime producto y nombre
        print("\033[1m" + "-" * 30 + "\033[0m")#marquetado
        print(f"\033[1m| \033[94m{'Precio':<15}\033[0m | ${precio:11,.2f} |\033[0m")#imprime precio
        print("\033[1m" + "-" * 30 + "\033[0m")#marquetado
        print(f"\033[1m|\033[94m {'Cantidad':<15}\033[0m | {cantidad:<12} |\033[0m")#imprime cantidad 
        print("\033[1m" + "-" * 30 + "\033[0m")#marquetado
    else:
        print(f"\033[93m El producto '{nombre}' no se encuentra en el inventario.\033[0m")#si el productno no esta en la biblioteca imprime mensaje de que no esta 

def actualizar_precio(inventario_local):#definicion funcion variable
    print("\n\033[94m\033[1mActualizar Precio\033[0m")#imprime titulo
    nombre = input("\n\033[1mIngrese el nombre del producto cuyo precio quiere actualizar: ").strip()#ingresa nombre del producto a actualizar
    if nombre in inventario_local:#condicional de validacion
        while True:#bucle para actulixar y sus validaciones 
            try:#empieza validacion
                nuevo_precio_str = input("\n\033[1mIngrese el nuevo precio: ").replace(',', '.')#ingresa nuevo precio en string y cambia ","por puntos
                nuevo_precio = float(nuevo_precio_str)#cambia string por decimal
                if nuevo_precio < 0:#condicional para verificar si el numero es positivo
                    print("\n\033[93mEl precio debe ser un valor positivo.\033[0m")#si no es positivo imprime este mensaje 
                    continue#Salta la iteración actual del bucle y pasa a la siguiente.
                inventario_local[nombre]['precio'] = nuevo_precio#la variable nuevo precio se guarda en el diccionario en la clave nombre en la clave precio
                print(f"\n\033[1m\033[32mEl precio de '{nombre}' ha sido actualizado a ${nuevo_precio:,.2f}.\033[0m")#imprime nombre del producto y el nuevo precio
                break#Termina el bucle prematuramente y el control del programa pasa a la siguiente instruccion
            except ValueError:#captura una excepcion que se produce cuando se le pasa un valor incorrecto a una funcion
                print("\n\033[93mPor favor, ingrese un numero valido para el precio.\033[0m")#imprime una instruccion para la validacion
    else:
        print(f"\n\033[93m El producto '{nombre}' no se encuentra en el inventario.\033[0m")#si el producto ya existe imprime mensaje de que no existe


def eliminar_producto(inventario_local):#definicion funcion para eliminar producto del inventario
    print("\n\033[94m\033[1mEliminar Producto\033[0m")#imprime titulo
    nombre = input("\033[1mIngrese el nombre del producto que quiere eliminar: ").strip()#ingresa el nombre de producto a ingresar 
    if nombre in inventario_local:#condicional para validar que nombre este en el diccionario lista
        del inventario_local[nombre]#elimina nombre de la biblioteca
        print(f"\n\033[1m\033[31mEl producto '{nombre}' ha sido eliminado.\033[0m")#imprime mensaje que confirma que el producto ha sido eliminado
    else:
        print(f"\n\033[93m El producto no se encuentra en el inventario.\033[0m")#si el producto no esta en el inventario imprime mensaje

def calcular_valor_total(inventario_local):#definicion de funcion para calcular valor del inventario
    print("\n\033[94m\033[1mValor Total del Inventario\033[0m")#imprime tirulo
    valor_total_lambda = lambda inventario: sum(producto['precio'] * producto['cantidad'] for producto in inventario.values())#obtiene los valores del diccionario inventario,itera sobre cada diccionario 
    valor_total = valor_total_lambda(inventario_local)#asigna el resultado de la funcion lamda a variable valor total
    print(f"\n\033[1mEl valor total del inventario es: ${valor_total:,.2f}\033[0m")#imprime valor total
    return #retorna a la variable

def mostrar_inventario(inventario_local):#definicion de la funcion 
    print("\n\033[94m\033[1mMostrar Inventario\033[0m")#imprime titulo
    if not inventario_local:#condicional que valida que si hay elementos en el diccionario
        print("\033[1m\n\033[93m\El inventario está vacio.\033[0m")#imprime que invetario esta vacio
        return#retorna  a menu
    print("\033[94m\033[1mInventario Actual   \033[0m")#imprime tirulo
    for nombre, info_producto in inventario_local.items():#tera sobre los elementos de un diccionario inventario utilizando el método items(). 
        precio = info_producto['precio']#asigna a la variable precio la llave de precio
        cantidad = info_producto['cantidad']#asigna a la variable cantidad la llave de cantidad
        print(f"\n\033[1mProducto: {nombre}, Precio: ${precio:,.2f}, Cantidad: {cantidad}\033[0m")#imprime el resultado
    print("-" * 35)#marquetado
#Menu 
while True:
    print("\n\033[94m\033[1m" + "═" * 35 + "\033[0m")
    print("\033[94m\033[1m" + "  SISTEMA DE INVENTARIO  ".center(35) + "\033[0m")
    print("\033[94m\033[1m" + "═" * 35 + "\033[0m")
    print("\033[1m  Opciones:\033[0m")
    print(f"\033[1m  1. Añadir producto{''.ljust(31)}\033[0m")
    print(f"\033[1m  2. Consultar producto{''.ljust(29)}\033[0m")
    print(f"\033[1m  3. Actualizar precio{''.ljust(30)}\033[0m")
    print(f"\033[1m  4. Eliminar producto{''.ljust(30)}\033[0m")
    print(f"\033[1m  5. Calcular valor total del inventario{''.ljust(24)}\033[0m")
    print(f"\033[1m  6. Mostrar inventario{''.ljust(27)}\033[0m")
    print(f"\033[1m  7. Salir{''.ljust(34)}\033[0m")
    print("\033[94m" + "═" * 35 + "\033[0m")

    opcion = input("\033[94m\033[1mSeleccione una opcion: \033[0m")#ingrese opcion
#condiconales para ingresar la funciones 
    if opcion == '1':
        agregar_producto(inventario)
    elif opcion == '2':
        consultar_producto(inventario)
    elif opcion == '3':
        actualizar_precio(inventario)
    elif opcion == '4':
        eliminar_producto(inventario)
    elif opcion == '5':
        valor_total = calcular_valor_total(inventario)
    elif opcion == '6':
        mostrar_inventario(inventario)
    elif opcion == '7':
        print("\n\033[94m\033[1mSaliendo del programa\033[0m")
        break
    else:
        print("\n\033[93m Opcion invalida. seleccione una opcion valida.\033[0m")
