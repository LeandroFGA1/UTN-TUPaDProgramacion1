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
        print("Hola ", name,"!")

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
    if check_radio is not False: # hice unas pruebas y si el numero es 0 lo detecta como falso si solo hago un if check_radio
        area = calculate_area_of_circle(check_radio)
        perimeter = calculate_perimeter_of_circle(check_radio)
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
        hours = seconds/3600
        print(seconds," pasado a horas son: ",hours)
    else:
        print(" segundos invalidos")
#6
def multiplication_table(num):
    check_num = is_num(num)
    if check_num is not False:
        for i in range(1,11):
            print (check_num, " x", i, " = ", check_num * i)
    else:
        print(" numero invalido")
#7
def basic_operations(num_one,num_two):
    check_num_one = is_num(num_one)
    check_num_two = is_num(num_two)
    if check_num_one is not False and check_num_two is not False:

        sum_     =  check_num_one , " + ", check_num_two, " = ", check_num_two + check_num_one
        res     =  check_num_one , " - ", check_num_two, " = ", check_num_one - check_num_two
        mult    = check_num_one , " x ", check_num_two, " = ", check_num_one * check_num_two
        if check_num_two == 0:
            div = " no se puede dividir por 0"
        else:
            div     = check_num_one , " / ", check_num_two, " = ", check_num_one / check_num_two
        return [sum_,res,mult,div]
    else:
        print("hay al menos un numero con formato invalido")
        return False
#8
def calculate_BMI(weight,height):
    return weight/(height**2)
#9
def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32
#10
def calculate_average(nun_one,num_two,num_three):
    return (nun_one+num_two+num_three)/3