
# Autor: Arroyo Rojas Luisi Leao

def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_envio(subtotal):
    if subtotal >= 300:
        return 0
    else:
        return 20


def calcular_total(subtotal, envio):
    return subtotal + envio


precio = 80
cantidad = 3

subtotal = calcular_subtotal(precio, cantidad)
envio = calcular_envio(subtotal)
total = calcular_total(subtotal, envio)

print("Subtotal: S/", subtotal)
print("Costo de envio: S/", envio)
print("Total del pedido: S/", total)
