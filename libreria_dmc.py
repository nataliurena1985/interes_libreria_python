def sumar_dos_numeros(valor_1, valor_2):
  resultado_suma = valor_1 + valor_2
  return resultado_suma

def saludar_usuario(nombre):
    """
    Recibe un nombre como parámetro y saluda al usuario.
    """
    print(f"Hola, {nombre}! Bienvenido al curso de Python.")


def doble_numero(numero):
    """
    Calcula y devuelve el doble del número dado.
    """
    return numero * 2


def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo usando la fórmula: (base * altura) / 2.
    """
    return (base * altura) / 2

def calcular_interes (monto,tasa_interes,tiempo_meses):
    """
    calcula  el interes simple.
    parametro:monto del  prestamo(en dolares)
    parametro:tasainteres;tasa de interes anual (valor entero)
    parametro:tiempo_meses
    """
    interes=monto*(tasa_interes/100)*tiempo_meses/12
    interes=round(interes,2)
    return interes