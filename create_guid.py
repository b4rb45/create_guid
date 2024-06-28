import uuid

def generate_guids(num_guids):
    return [str(uuid.uuid4()) for i in range(num_guids)]

def save_guids_to_file(guids, filename="guids.txt"):
    with open(filename, 'w') as file:
        for guid in guids:
            file.write(f"{guid}\n")

if __name__ == "__main__":
    try:
        num_guids = int(input("Ingrese la cantidad de GUIDs a crear: "))
        if num_guids <= 0:
            print("Por favor ingrese un número positivo.")
        else:
            guids = generate_guids(num_guids)
            save_guids_to_file(guids)
            print(f"Se han generado {num_guids} GUIDs y se han guardado en el archivo 'guids.txt'.")
    except ValueError:
        print("Por favor ingrese un número válido.")
