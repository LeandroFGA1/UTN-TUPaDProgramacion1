number_pi = 3.1415



def is_num(num :str):
    num = num.strip()
    if num.isdecimal():
        return int(num)
    if num == "" or num.isspace():
        print("el contenido no puede estar vacio")
        return False
    if num.isalpha():
        print("numero invalido")
        return False
    if num.count(".") > 1 or num == "." :
        print(" un numero no puede tener tantos puntos o ser un punto")
    if num.isdecimal():
        return int(num)
    if num.count(".") == 1 and num[0] != "." and num.replace(".","").isdecimal():
        num_list = num.split(".")
        num = float (num_list[0]+"."+num_list[1])
        return num
    else:
        print(" formato invalido")
        return False


def is_text(text: str):
    text = text.strip()
    if text == "" or text.isspace():
        print("el contenido no puede estar vacio")
        return False
    elif text.isdecimal():
        print(" solo se aceptan letras")
        return False
    elif len(text.replace(" ","").replace("'","")) < 2:
        print(" texto demaciado corto")
        return False
    elif text.replace(" ","").replace("'","").isalpha(): # casos correctos 
        return True
    else: # por si olvide algun filtro
        return False 

#1
def hi_world ():
    print (" Hola Mundo!")
#2
def greet_user(name :str):
    name = name.strip()
    if is_text(name):
        print("Hola", name+"!")

#3
def personal_information(first_name :str, last_name :str, age :str , residence :str):
    first_name = first_name.strip()
    last_name = last_name.strip()
    age = age.strip()
    residence = residence.strip()
    if not is_text(first_name):
        print("nombre invalido")
    if not is_text(last_name):
        print("apellido invalido")
    if  not age.isdecimal():
        print(" edad invalida")
    if not is_text(residence): # se toma provincia, asi se evitan fallos con municipios o barrios que tienen numeros en su nombre
        print ("provincia invalida")
    print ("Hola, soy ",first_name,last_name," tengo ",age," años"," y vivo en ",residence)
#4.1
def calculate_area_of_circle(radio):
        return number_pi * radio ** 2
#4.2
def calculate_perimeter_of_circle(radio):
    return number_pi * 2 * radio
#4
def calculate_circle(radio :str):
    radio = radio.strip()
    check_radio = is_num(radio)
    if check_radio is not False: # hice unas pruebas y si el numero es 0 lo detecta como falso. Con is not False se soluciona
        area = round(calculate_area_of_circle(check_radio),3)
        perimeter = round(calculate_perimeter_of_circle(check_radio),3)
        print("El circulo cuyo radio es : ",check_radio, " tiene un area de: ", area, " y un perimetro de: ",perimeter)
    else:
        print("datos invalidos")
    
#5
def seconds_to_hours(seconds:str):
    seconds = seconds.strip()
    if seconds == "0" or seconds =="" or seconds.isspace():
        print(" no paso nada de tiempo")
    if seconds.isdecimal():
        seconds = int(seconds)
        hours = int(seconds/3600)
        minutes = int(seconds % 3600 / 60) # aqui busque las formulas para convertir por que desconocia
        seconds_module = int (seconds % 60)# aqui busque las formulas para convertir por que desconocia
        print(seconds,"segndos pasados a horas son:",hours,"horas y",minutes,"minutos con",seconds_module,"segundos")
    else:
        print(" segundos invalidos")
#6
def multiplication_table(num):
    check_num = is_num(num)
    if check_num is not False:
        print("tabla de 1 a 10 del numero:",num)
        for i in range(1,11):
            print (check_num,"x", i, "=", check_num * i)
    else:
        print(" numero invalido")
#7
def basic_operations(num_one,num_two):
    check_num_one = is_num(num_one)
    check_num_two = is_num(num_two)
    if check_num_one is not False and check_num_two is not False:

        sum_  = f"{check_num_one} + {check_num_two} = {check_num_one + check_num_two}"
        res   = f"{check_num_one} - {check_num_two} = {check_num_one - check_num_two}"
        mult  = f"{check_num_one} x {check_num_two} = {check_num_one * check_num_two}"
        if check_num_two == 0:
            div = " no se puede dividir por 0"
        else:
            div = f"{check_num_one} / {check_num_two} = {check_num_one / check_num_two}"
        return [sum_,res,mult,div]
    else:
        print("hay al menos un numero con formato invalido")
        return False
#8
def calculate_BMI(weight :str,height :str):
    weight = weight.strip()
    height = height.strip()
    check_weight = is_num(weight)
    check_height = is_num(height)
    if check_height is not False and check_weight is not False :
        check_height = check_height / 100
        bmi = round(check_weight / (check_height ** 2), 2)
        if bmi < 18.5:
            men = "Bajo peso"
        elif 18.5 <= bmi < 25:
            men = "peso normal"
        elif 25 <= bmi < 30:
            men = "Sobrepeso"
        elif 30 <= bmi < 35:
            men = "Obesidad grado 1"
        elif 35 <= bmi < 40:
            men = "obesidad grado 2"
        else:
            men = "obesidad grado 3"
            
        if bmi < 18:
            woman = "bajo peso"
        elif 18 <= bmi < 24:
            woman = "peso normal"
        elif 24 <= bmi < 29:
            woman = "sobrepeso"
        elif 29 <= bmi < 34:
            woman = "obesidad grado 1"
        elif 34 <= bmi < 39:
            woman = "obesidad grado 2"
        else:
            woman = "Obesidad grado 3"

        print("suponiendo que el usuario tiene entre 20 y 50 años,"," una altura de:",height + "cm"," y un peso de:",weight + "kg", "y con un IMC de ", bmi," entonces:")
        print("si es hombre tiene ",men)
        print("si es mujer tiene ", woman)

        return bmi
    else:
        print("datos invalidos")
        return False
#9
def celsius_to_fahrenheit(celsius:str):
    check_cel = is_num(celsius)
    if check_cel is not False:
        return (float(celsius) * 1.8) + 32
    else: 
        print("temperatura invalida")
#10
def calculate_average(nun_one,num_two,num_three):
    check_one = is_num(nun_one)
    check_two = is_num(num_two)
    check_three = is_num(num_three)
    if check_one is not False and check_two is not False and check_three is not False:
        return (check_one+check_two+check_three)/3
    else:
        print (" hay al menos un input invalido")


if __name__ == "__main__":
    print("ejercicio 1 \n")
    hi_world()
    print("---------------------------")

    print("ejercicio 2 \n")
    greet_user("Juan")
    print("---------------------------")

    print(" ejercicio 3 \n")
    personal_information("Juan","Doe","20","Madrid")
    print("---------------------------")

    print("ejercicio 4 \n")
    calculate_circle("2.2")
    print("---------------------------")

    print("ejercicio 5 \n")
    seconds_to_hours("5000")

    print("ejercicio 6 \n")
    multiplication_table("13")
    print("---------------------------")

    print("ejercicio 7 \n")
    print(basic_operations("1","2"))
    print("---------------------------")

    print("ejercicio 8 \n")
    calculate_BMI("70","168")
    print("---------------------------")

    print("ejercicio 9 \n")
    print(celsius_to_fahrenheit("5"))
    print("---------------------------")

    print("ejercicio 10 \n")
    print(calculate_average("1","2","3"))
    