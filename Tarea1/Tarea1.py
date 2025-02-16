from graphviz import Digraph

class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_principio(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.generar_grafico()

    def insertar_al_final(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            temp = self.cabeza
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo
            nuevo_nodo.anterior = temp
        self.generar_grafico()

    def eliminar_por_valor(self, carnet):
        temp = self.cabeza
        while temp:
            if temp.carnet == carnet:
                if temp.anterior:
                    temp.anterior.siguiente = temp.siguiente
                if temp.siguiente:
                    temp.siguiente.anterior = temp.anterior
                if temp == self.cabeza:
                    self.cabeza = temp.siguiente
                del temp
                self.generar_grafico()
                return
            temp = temp.siguiente
        print("Carnet no encontrado.")

    def mostrar_lista(self):
        temp = self.cabeza
        resultado = "None"
        while temp:
            resultado += f" <- [{temp.nombre} {temp.apellido} ({temp.carnet})] ->"
            temp = temp.siguiente
        resultado += " None"
        print(resultado)

    def generar_grafico(self):
        dot = Digraph()
        temp = self.cabeza
        while temp:
            dot.node(str(temp.carnet), f"{temp.nombre} {temp.apellido} ({temp.carnet})")
            if temp.siguiente:
                dot.edge(str(temp.carnet), str(temp.siguiente.carnet))
                dot.edge(str(temp.siguiente.carnet), str(temp.carnet))
            temp = temp.siguiente
        dot.render("lista_doblemente_enlazada", format="png", cleanup=False)

if __name__ == "__main__":
    lista = ListaDoblementeEnlazada()
    while True:
        print("\n1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por carnet")
        print("4. Mostrar lista")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            carnet = input("Ingrese el carnet: ")
            lista.insertar_al_principio(nombre, apellido, carnet)
        elif opcion == "2":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            carnet = input("Ingrese el carnet: ")
            lista.insertar_al_final(nombre, apellido, carnet)
        elif opcion == "3":
            carnet = input("Ingrese el carnet a eliminar: ")
            lista.eliminar_por_valor(carnet)
        elif opcion == "4":
            lista.mostrar_lista()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
