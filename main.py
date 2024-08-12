from dm_set.dm_set import DMSet

def display_menu():
    print("Menu:")
    print("1. Construir conjuntos")
    print("2. Operar conjuntos")
    print("3. Finalizar")

def build_set(custom_set):
    values = input("Ingrese los elementos del conjunto separados por espacio (A-Z, 0-9): ")
    values_list = values.split()
    
    for value in values_list:
        if len(value) == 1 and (value.isalnum()):
            custom_set.add(value)
        else:
            print(f"Elemento '{value}' no es válido. Debe ser un solo carácter alfanumérico.")

def operate_sets(set1, set2, universal_set):
    while True:
        print("Operaciones disponibles:")
        print("1. Complemento")
        print("2. Unión")
        print("3. Intersección")
        print("4. Diferencia")
        print("5. Diferencia Simétrica")
        choice = input("Elija una operación: ")

        if choice == '1':
            print("Complemento del Conjuto 1:", set1.complement(universal_set))
            print("Complemento del Conjuto 2:", set2.complement(universal_set))
            break
        elif choice == '2':
            print("Unión:", set1.union(set2))
            break
        elif choice == '3':
            print("Intersección:", set1.intersection(set2))
            break
        elif choice == '4':
            print("Diferencia (Conjuto 1 - Conjuto 2):", set1.difference(set2))
            break
        elif choice == '5':
            print("Diferencia Simétrica:", set1.symmetric_difference(set2))
            break
        else:
            print("Operación no válida. Por favor, intente de nuevo.")

def main():
    universal_set = DMSet()
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        universal_set.add(char)

    set1 = DMSet()
    set2 = DMSet()

    while True:
        display_menu()
        choice = input("Seleccione una opción: ")

        if choice == '1':
            print("Construir Conjuto 1")
            set1 = build_set()
            print("Construir Conjuto 2")
            set2 = build_set()
        elif choice == '2':
            operate_sets(set1, set2, universal_set)
        elif choice == '3':
            print("Finalizando...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()