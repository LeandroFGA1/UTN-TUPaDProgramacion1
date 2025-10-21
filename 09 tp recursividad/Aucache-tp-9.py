
#1
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
#2
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)    
#3
def power_of_a_num(base,num):
    if num == 0:
        return 1
    else:
        return base * power_of_a_num(base,num-1)
#4    
def decimal_to_binary(num:int,register:str=""):
    if num < 2:
        return register +str(num)
    else:
        register = decimal_to_binary(num // 2, register)
        return register +str(num % 2)
#5   
def is_palindromo(text:str):
    if text == "":
        print("no introdujo nada, el vacio se toma como afirmativo, ya que la nada se lee igual desde sus extremos inexistentes")
        return True
    if len(text) != 1:
        if text[0] != text[-1]:
            return False
        else:
            if len(text) == 2:
                return True
            return is_palindromo(text[1:-1])
    else:
        return True
#6
def sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n%10) + sum_digits(n//10)
#7
def block_pyramid(n):
    if n == 0:
        return 0
    else:
        return n + block_pyramid(n-1)
    
#8
def count_digit(num,digit):
    if num ==0:
        return 0
    
    current_digit = num%10
    if current_digit == digit:
        count = 1
    else:
        count = 0
    remainder = count_digit(num//10, digit)
    return count + remainder

def main():
    functions = [factorial,fibonacci,power_of_a_num, decimal_to_binary,is_palindromo,sum_digits,block_pyramid,count_digit]
    descrip_function = ["Ingrese un numero para saber su factorial", "ingrese un numero para saber su fibonacci", "Ingrese un numero para conocer el calculo de la potencia de un número base elevado a exponente","Ingrese un numero en base decimal(un numero normal) para saber como es en binario","ingrese su texto para saber si es palindromo","ingrese un numero para saber la suma de sus digitos", "ingrese un numero para saber la cantidad de bloques para la piramide","ingrese un numero y un digito para saber cuantas veces se repite el digito en el numero"]
    for i in range(len(functions)):
        print(f"el ejercicio {i+1} llamado: {functions[i].__name__} \n")
        print(descrip_function[i])
        num = 5
        if i == 2:
            recursion_response = functions[i](5,5)
            num = "base 5 y num 5"
        elif i == 4: 
            recursion_response = functions[i]("radar")
            num ="radar"
        elif i == 7:
            recursion_response = functions[i](112113, 1)
            num = "112113 y el digito 1"
        else:
            recursion_response = functions[i](5)
        print(f"la respuesta de este ejercicio cuando el input es {num} es: {recursion_response}")
        print("----------------------")


    
if __name__ == "__main__":
    main()