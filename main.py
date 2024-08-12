import string
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

def create_universal_set():
    universal_elements = string.ascii_uppercase + string.digits  # 'A'-'Z' and '0'-'9'
    universal_set = DMSet()
    for char in universal_elements:
        universal_set.add(char)
    return universal_set

def main():
    set1 = DMSet()
    set2 = DMSet()
    universal_set = create_universal_set()

    while True:
        display_menu()
        choice = input("Seleccione una opción (1-3): ")

        if choice == "1":
            print("\nConstruir conjunto 1:")
            build_set(set1)
            print("\nConstruir conjunto 2:")
            build_set(set2)

            print("\nConjunto 1:", set1)
            print("Conjunto 2:", set2)
            print("Conjunto universal:", universal_set)

        elif choice == "2":
            print("\nSeleccione la operación que desea realizar:")
            print("1. Unión")
            print("2. Intersección")
            print("3. Complemento de Conjunto 1 en Conjunto Universal")
            print("4. Diferencia (Conjunto 1 - Conjunto 2)")
            print("5. Diferencia Simétrica")
            op_choice = input("Seleccione una opción (1-5): ")

            if op_choice == "1":
                print("Unión:", set1.union(set2))
            elif op_choice == "2":
                print("Intersección:", set1.intersection(set2))
            elif op_choice == "3":
                print("Complemento de Conjunto 1 en Conjunto Universal:", set1.complement(universal_set))
            elif op_choice == "4":
                print("Diferencia (Conjunto 1 - Conjunto 2):", set1.difference(set2))
            elif op_choice == "5":
                print("Diferencia Simétrica:", set1.symmetric_difference(set2))
            else:
                print("Opción no válida.")

        elif choice == "3":
            print("Finalizando programa.")
            break

        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main()