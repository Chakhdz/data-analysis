# Clases de texto (`texto_clase`)

Clasificar cada texto por su función antes de analizarlo: no se pueden comparar un dato de inventario y una cédula interpretativa.

| Clase | Qué es | Regla |
|---|---|---|
| `parafrasis` | Resumen propio, no transcripción del museo | marcado como paráfrasis |
| `generico_museo` | Texto general compartido por varias piezas | marcado como genérico |
| `cedula_sala` | Cédula, texto de sala, vitrina, cartel | por tipo de documento |
| `catalogo_publicacion` | Catálogo, folleto, boletín, ficha técnica | por tipo de documento |
| `inventario` | Dato de ficha, no interpretación | museo de inventario, texto en mayúsculas o menor de 150 caracteres |
| `interpretativo` | Explica la pieza | el resto de las piezas con texto |
| `empty` | Sin texto | |

Reglas de cuidado: los textos en mayúsculas sostenidas casi siempre son inventario; un pie de foto corto de un museo interpretativo no es inventario.
