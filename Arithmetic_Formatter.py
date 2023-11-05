def arithmetic_arranger(lista_aritmetica, solucion = False):
  numero_superior = ""
  operador = ""
  separadores = ""
  numero_inferior = ""
  sumaAcumulativa = ""
  resultado = ""
  suma = ""


  if(len(lista_aritmetica) > 5):
    return "Error: Too many problems."

  for elemento in lista_aritmetica:
    #se divide la cadena de caracteres en numeros y operadores
    primerNumero = elemento.split(" ")[0]
    operador = elemento.split(" ")[1]
    segundoNumero = elemento.split(" ")[2]

    # verificar que los numeros no superen los digitos 
    if (len(primerNumero) > 4 or len(segundoNumero) > 4):
      return "Error: Numbers cannot be more than four digits."

    # validad que el dato ingresado sea numerico
    if not primerNumero.isnumeric() or not segundoNumero.isnumeric():
      return "Error: Numbers must only contain digits."

    if operador not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."

    if operador == "+":
      suma = str(int(primerNumero) + int(segundoNumero))
    elif operador == "-":
      suma = str(int(primerNumero) - int(segundoNumero))
    largo_maximo = max(len(primerNumero) , len(segundoNumero)) + 2
    primera_linea = str(primerNumero).rjust(largo_maximo)
    segunda_linea = operador + str(segundoNumero.rjust(largo_maximo - 1))
    sltn = str(suma.rjust(largo_maximo))


    separador = "".join("-" for _ in range(largo_maximo))
    if elemento != lista_aritmetica[-1]: 
      numero_superior += f'{primera_linea}    '
      numero_inferior += f'{segunda_linea}    '
      separadores += f'{separador}    '
      sumaAcumulativa += f'{sltn}    '
    else: 
      numero_superior += primera_linea
      numero_inferior += segunda_linea
      separadores += separador
      sumaAcumulativa += sltn  

  return (numero_superior + "\n" + numero_inferior + "\n" + separadores +
          "\n" + sumaAcumulativa if solucion else numero_superior + "\n" +
          numero_inferior + "\n" + separadores)

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
