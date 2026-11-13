
# Solicitudes de Cambio - Arroyo Pedidos

**Autor:** Arroyo Rojas Luisi Leao

## 1. INC-014: Corrección del cálculo del subtotal

- **Descripción:** El sistema devuelve el precio unitario como subtotal, sin considerar la cantidad solicitada.
- **Tipo de cambio:** Correctivo.
- **Justificación:** El resultado del subtotal es incorrecto porque no multiplica el precio unitario por la cantidad.
- **Requisito relacionado:** RN-01.
- **Archivos afectados:** codigo/pedidos.py.
- **Riesgo:** Los pedidos pueden mostrar importes incorrectos y generar errores en los cobros.
- **Criterio de aceptación:** Para un precio de S/ 80 y una cantidad de 3 unidades, el sistema debe calcular un subtotal de S/ 240.
- **Decisión de aprobación simulada:** APROBADO. Se autoriza la corrección de la función calcular_subtotal().

## 2. CR-015: Incorporación del cálculo del costo de envío

- **Descripción:** La gerencia solicita incorporar el cálculo automático del costo de envío y el total del pedido.
- **Tipo de cambio:** Evolutivo (nueva funcionalidad).
- **Justificación:** Permitir que el sistema determine automáticamente el costo de envío según el subtotal y muestre el total del pedido.
- **Requisitos relacionados:** RN-02, RN-03 y RN-04.
- **Archivos afectados:** codigo/pedidos.py y documentos/requisitos.md.
- **Riesgo:** Un cálculo incorrecto podría generar cobros equivocados a los clientes.
- **Criterio de aceptación:**
  - Subtotal de S/ 240: envío S/ 20, total S/ 260.
  - Subtotal de S/ 300: envío S/ 0, total S/ 300.
  - Subtotal de S/ 450: envío S/ 0, total S/ 450.
- **Decisión de aprobación simulada:** APROBADO. Se autoriza implementar el cálculo automático del envío y del total del pedido.
