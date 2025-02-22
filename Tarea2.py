def binario (numero):
    if numero==0:
        return "0"
    if numero==1:
        return "1" 
    return binario(numero//2)+str(numero%2)

def contar_digitos(n):
    if n < 10:
        return 1
    return 1 + contar_digitos(n//10)

def calcular_raiz_cuadrada(n, bajo, alto):
    if bajo > alto:
        return alto
    medio = (bajo + alto) // 2
    if medio * medio == n:
        return medio
    elif medio * medio < n:
        return calcular_raiz_cuadrada(n, medio + 1, alto)
    else:
        return calcular_raiz_cuadrada(n, bajo, medio - 1)


def raiz_cuadrada_entera(n):
    if n < 0:
        return None
    return calcular_raiz_cuadrada(n, 0, n)

valores_romanos = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000, 'i' : 1, 'v' : 5, 'x' : 10, 'l' : 50, 'c' : 100, 'd' : 500, 'm' : 1000, } 

def convertir_a_decimal(romano, i=0):
    if i >= len(romano):
        return 0
    valor_actual = valores_romanos[romano[i]]
    if i + 1 < len(romano) and valores_romanos[romano[i + 1]] > valor_actual:
        return -valor_actual + convertir_a_decimal(romano, i +1)
    else:
        return valor_actual + convertir_a_decimal(romano, i + 1)
    
def suma_numeros_enteros(n4):
    if n4==0:
        return 0
    return n4 + suma_numeros_enteros(n4 - 1)

def menu():
    while True:
        print("\nMenú de Operaciones Matemáticas:")
        print("1. Convertir a Binario")
        print("2. Contar Dígitos")
        print("3. Raíz Cuadrada Entera")
        print("4. Convertir a Decimal desde Romano")
        print("5. Suma de Números Enteros")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            num = int(input("Ingrese un número entero: "))
            print("Binario:", binario(num))
        elif opcion == "2":
            num = int(input("Ingrese un número entero: "))
            print("Cantidad de dígitos:", contar_digitos(num))
        elif opcion == "3":
            num = int(input("Ingrese un número entero: "))
            print("Raíz cuadrada entera:", raiz_cuadrada_entera(num))
        elif opcion == "4":
            romano = input("Ingrese un número en romano: ").upper()
            print("Decimal:", convertir_a_decimal(romano))
        elif opcion == "5":
            num = int(input("Ingrese un número entero positivo: "))
            print("Suma total:", suma_numeros_enteros(num))
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()