#1
fruit_prices = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
def new_fruits():
    fruit_prices["Naranja"] = 1200
    fruit_prices["Manzana"] = 1500
    fruit_prices["Pera"] = 2300
    print(fruit_prices)
#2
def new_prices():
    fruit_prices["Banana"] = 1330
    fruit_prices["Manzana"] = 1700
    fruit_prices["Melón"] = 2800
    print(fruit_prices)

#3
def list_of_keys():

    list_keys = list (fruit_prices.keys())
    print(list_keys)


#4
dictionary_telephone = {}
def telephone_log():
    for i in range (5):
        flag_key = True
        while flag_key:
            key_name = input("ingrese el nombre a registrar: ").title()
            if key_name.isalpha() and len(key_name) > 2:
                flag_key = False
            else:
                print ("nombre invalido")
        flag_value = True
        while flag_value:
            value_number = input("ingrese el numero a asignar al nombre")
            value_number = value_number.strip()
            len_number = len(value_number)
            if value_number.isdecimal():
                if len_number == 6: #siguendo el ejemplo, los telefonos son de 6 cifras
                    dictionary_telephone[key_name] = value_number
                    flag_value = False
                    print("numero ingresado con existo")
                elif len_number > 6:
                    print ("numero demasiado largo")
                else:
                    print("numero demasiado corto")
            
            else:
                print("entrada invalida")
        print("registro exitoso")

    name = input("ingrese el nombre del usuario y se le dara su numero").title()
    number = dictionary_telephone.get(name)
    if number:
        print("el numero de telefono de ",name,"es:",number)
    else:
        print("usuario inexistente")
    

#5
def unique_words():
    words = input ("ingrese su frase/palabras").lower()
    if words.replace(" ","").isalpha():
        list_words = words.split()
        set_words = set(list_words)
        words_log = {}
        print(set_words)
        for word in set_words:
            words_log[word] = list_words.count(word)
        print(words_log)
    else:
        print("entrada invalida") # incompleto revisar
#6

def students_score():
    students_log ={}
    students_names = ""
    for i in range (3):
        flag_name = True
        while flag_name:
            student = input("nombre del estudiante").title()
            if student.isalpha() and student not in students_names and len(student)>2:
                students_names = students_names + " " + student
                tupla_student=()
                for j in range (3):
                    flag_score = True
                    while flag_score:
                        student_score = input(f"Ingrese la nota {j+1}/3 (solo números enteros del 0 al 10): ")
                        if student_score.isdecimal():
                            if int(student_score) >= 0 and int(student_score)<=10:
                                tupla_student = tupla_student + (int(student_score),)
                                flag_score = False
                            else:
                                print("valor fuera de los rangos, intente nuevamente")
                        else:
                            print("datos invalidos, intente nuevamente")
                students_log[student] = tupla_student
                flag_name = False
                
            else:
                print(" nombre invalido, intente nuevamente")
    for key in students_log:
        print(f" el estudiante {key} tiene un promedio de: {(sum(students_log[key])/3):.2f}")

#7
def students_midterm():
    first_midterm = [3,6,5,6,10,3,7,10]
    second_midterm= [10,3,5,7,8,3,9,10]
    students_names = ["Juan","Luis","Pepe","Sol","Luna","Leo","Aby","Miguel"]
    both_passed = []
    one_passed = []
    least_one_passed = []
    for i in range(len(students_names)):
        if first_midterm[i] >=6 or second_midterm[i] >=6:
            least_one_passed.append(students_names[i])
        if first_midterm[i] >=6 and second_midterm[i] >=6:
            both_passed.append(f"Estudiante {students_names[i]} aprobo ambos examenes. El primero con {first_midterm[i]} y el segundo con {second_midterm[i]}")
        elif (first_midterm[i] >=6 and second_midterm[i] < 6) or (first_midterm[i] < 6 and second_midterm[i] >=6):
            if first_midterm[i] >= 6:
                one_passed.append(f"Estudiante {students_names[i]} solo aprobo el primer examen con {first_midterm[i]}")
            else:
                one_passed.append(f"Estudiante {students_names[i]} solo aprobo el segundo examen con {second_midterm[i]}")
    print("los estudiantes que aprobaron todos los parciales son:")
    for i in range(len(both_passed)):
        print("*",both_passed[i])
    print("\n los estudiantes que aprobaron un parcial son:")
    for i in range(len(one_passed)):
        print("*",one_passed[i])
    print("\n los entudientes que aprobaron al menos un parcial son:")
    for i in range(len(least_one_passed)):
        print("*",least_one_passed[i])
#8
def stock_products():
    products_log = {"papa":3,"arroz":5,"leche":0}
    flag = True
    options_valid =["1","2","3","4"]
    while flag:
        option = input("Ingrese el numero correspondiente para:\n 1-consultar stock \n 2-agregar unidades al stock de un producto \n 3-agregar un producto \n 4-finalizar")
        if option not in options_valid:
            print(" numero invalido, intente nuevamente")
        elif option =="1":
            view_stock = input("ingrese el nombre del producto para ver su stock").lower()
            if view_stock in products_log:
                print(f"{view_stock} tiene un stock de: {products_log[view_stock]}")
            else: 
                print("producto inexistente")
        elif option == "2":
            add_stock = input("ingrese el nombre del producto para agregarle stock").lower()
            if add_stock in products_log:
                flag_number_stock = True
                while flag_number_stock:
                    number_stock = input("ingrese la cantidad de stock a agregar")
                    if number_stock.isdecimal():
                        products_log[add_stock] += int(number_stock)
                        flag_number_stock = False
                    else:
                        print("numero invalido. intente nuevamente")
            else:
                print("producto inexistente en el catalogo")
        elif option == "3":
            new_product = input("ingrese el nombre del nuevo producto").lower()
            if new_product in products_log:
                print("producto ya existente")
            else:
                products_log[new_product] = 0
                print("producto agregado con exito")
        elif option =="4":
            print("Hasta luego")
            flag = False
#9
def calendar():
    days = ("lunes","martes","miercoles","jueves","viernes","sabado","domingo") #se sobre entiende que la agenda se actualiza cada semana
    # los horarios de las reuniones solo pueden de 8am a 8 pm, a la hora comparar usare los numeros sin los : para mayor facilidad de verificacion
    calendar_log ={("lunes","10:00"):"Reunión",("martes","15:00"):"Clase de ingles"}
    flag_day = True
    while flag_day:
        day_select = input("ingrese el dia que quiere buscar: ").lower()
        if day_select in days:
            flag_day = False
            flag_hour = True
            while flag_hour:
                hour_select = input("ingrese la hora de la reunion. separe la partes con : y rellene con 0 si hace falta.\n ej: 08:05\n ingrese:")
                if hour_select.replace(":","").isdecimal() and hour_select.count(":") == 1 and len(hour_select) == 5:
                    check_time = hour_select.split(":")
                    if int(check_time[1]) <= 59 and (8 <= int(check_time[0]) <=20):
                        flag_hour = False
                    else:
                        print("recuerde que las reuniones son entre 08:00 a 20:00, intente nuevamente\n")
                else:
                    print("hora invalida, intente de nuevo\n")
        else:
            print("dia invalido, intente de nuevo \n")
    key_input = (day_select,hour_select)
    if key_input in calendar_log:
        print(f" en el dia {day_select} a las {hour_select} tiene la actividad: {calendar_log[key_input]}")
    else:
        print(f"no hay ninguna actividad ese dia a ese horario")
#10
def swap_key_value():
    origin = {"Argentina":"Buenos Aires","Chile":"Santiago","Uruguay": "Montevideo","Peru":"Lima","Colombia":"Bogota","España":"Madrid","Italia":"Roma"}
    new_log = {}
    for key in origin:
        new_log[origin[key]] = key
    print(new_log)
    
def main():
    function_names = [new_fruits,new_prices,list_of_keys,telephone_log,unique_words,students_score,students_midterm,stock_products,calendar,swap_key_value]
    for i in range(10):
        print(f"----ejercicio {i+1}----")
        function_names[i]()
        print(f"----fin ejercicio {i+1}----\n")

if __name__ == "__main__":
    main()