#1

def init_file():
    with open("productos.txt","w") as archivo:
        print("entre")
        archivo.write("Pan,5,100\n")
        archivo.write("Torta,10,50\n")
        archivo.write("Factura,15,25\n")


#2
def show_products():
    with open("productos.txt","r") as archivo:
        for line in archivo:
            line = line.strip()
            parts = line.split(",")
            print(f"Producto: {parts[0].title()} | Precio: ${parts[1]} | Cantidad: {parts[2]}")


#3

def check_product_line(line_product:str):
    parted_product = line_product.split(",")
    if len(parted_product) !=3:
        print("linea invalida, debe tener Nombre, Precio y Cantidad. Todo en separado por comas")
        return False
    if not parted_product[1].isdecimal() or not parted_product[2].isdecimal():
        print("numeros invalidos")
        return False
    product_new_name = parted_product[0]
    with open("productos.txt","r") as archivo:
        for line in archivo:
            if product_new_name == line.strip().split(",")[0]:
                print("producto ya existente")
                return False
    return True

def fit_product(line_product:str):
    parted_product = line_product.split(",")
    if len(parted_product) != 3:
        print("producto mal redactado")
        return "nocumple"
    name = parted_product[0].strip().title()
    price = parted_product[1].strip()
    stock = parted_product[2].strip()
    return f"{name},{price},{stock}" 

def add_product():
    flag = True
    while flag:
        line_product = input("ingrese el producto a agregar en el siguiente formato nombre,precio,cantidad ")
        line_clean = fit_product(line_product)
        if check_product_line(line_clean) and line_clean: # tuve unos problemas con esta linea, creo que es un poco rebundante pero previene errores
            with open("productos.txt","a") as archivo:
                archivo.write(f"{line_clean} \n")
            print("producto agregado correctamente \n")
            choise = input("quiere agregar otro producto? 1-si , otra tecla no")
            if choise != "1":
                flag = False
        else:
            print("no se logro agregar el producto")

#4
def create_list():
    products = []
    with open("productos.txt","r") as archivo:
        for line in archivo:
            line_descomp = line.split(",")
            product_dict = { "nombre": line_descomp[0].strip(), "precio":line_descomp[1].strip(), "cantidad":line_descomp[2].strip()}
            products.append(product_dict)
    return products

#5
def search_product_in_the_list(list_products:list):
    name_product = input("ingrese el nombre del producto a buscar: ")
    for product in list_products:
        if product["nombre"] == name_product.title():
            print(f"Producto encontrado \n Nombre: {product['nombre']} | Precio: ${product['precio']} | Cantidad: {product['cantidad']}")
            return
    print("producto no encontrado")

#6
def update_products(list_products:list):
    with open("productos.txt","w") as archivo:
        for product in list_products:
            archivo.write(f"{product['nombre']},{product['precio']},{product['cantidad']} \n")


def main():
    print("inicia el programa creando el archivo y agregando productos \n")
    init_file()
    print("\n mostrando productos actuales \n")
    show_products()
    print("\n agregando productos \n")
    add_product()
    print("\n creando lista de productos \n")
    list_products = create_list()
    print("\n buscando un producto en la lista \n")
    search_product_in_the_list(list_products)
    print("\n actualizando archivo de productos \n")
    update_products(list_products)

if __name__ == "__main__":
    main()
