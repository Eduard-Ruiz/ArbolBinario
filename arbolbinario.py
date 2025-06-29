# ---------------------------------------------
# Programa: Árbol Binario con Recorridos
# Autor: Eduard Yezid Ruiz Ordoñez
# Curso: Estructura de Datos - Semana 8
# Docente: Carmen Emilia Rubio Vanegas
# ---------------------------------------------
# Descripción: Inserta nodos en un árbol binario
# y realiza recorridos inorder, preorder y postorder
# mediante un menú interactivo.
# ---------------------------------------------

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izq = self._insertar_recursivo(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._insertar_recursivo(nodo.der, valor)
        else:
            print(f"El valor {valor} ya existe en el árbol.")
        return nodo

    def inorder(self, nodo):
        if nodo:
            self.inorder(nodo.izq)
            print(nodo.valor, end=" ")
            self.inorder(nodo.der)

    def preorder(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.preorder(nodo.izq)
            self.preorder(nodo.der)

    def postorder(self, nodo):
        if nodo:
            self.postorder(nodo.izq)
            self.postorder(nodo.der)
            print(nodo.valor, end=" ")

def menu():
    print("\n====== MENÚ DEL ÁRBOL BINARIO ======")
    print("1. Insertar elemento")
    print("2. Recorrido Inorder (izq - raíz - der)")
    print("3. Recorrido Preorder (raíz - izq - der)")
    print("4. Recorrido Postorder (izq - der - raíz)")
    print("5. Insertar elementos de ejemplo automáticamente")
    print("6. Salir")
    print("====================================")

def insertar_ejemplo(arbol):
    valores = [50, 30, 70, 20, 40, 60, 80]
    for valor in valores:
        arbol.insertar(valor)
    print(f"Se han insertado correctamente los valores: {valores}")

def main():
    arbol = ArbolBinario()

    while True:
        menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            try:
                valor = int(input("Ingrese el número que desea insertar: "))
                arbol.insertar(valor)
                print(f"Se ha insertado correctamente el valor {valor}.")
            except ValueError:
                print("Entrada inválida. Solo se permiten números enteros.")
        elif opcion == 2:
            print("Recorrido Inorder:")
            arbol.inorder(arbol.raiz)
            print()
        elif opcion == 3:
            print("Recorrido Preorder:")
            arbol.preorder(arbol.raiz)
            print()
        elif opcion == 4:
            print("Recorrido Postorder:")
            arbol.postorder(arbol.raiz)
            print()
        elif opcion == 5:
            insertar_ejemplo(arbol)
        elif opcion == 6:
            print("Finalizando el programa... ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
