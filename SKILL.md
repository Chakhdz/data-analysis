---
name: analisis-de-textos-museograficos
description: Analizar textos de museo (cédulas, catálogos, fichas) con el marco Ravelli/Halliday/Van Leeuwen: clasificar el texto, codificar con matrices y revisar antes de reportar.
---

# Análisis de textos museográficos

Usar cuando se pidan analizar cédulas, textos de sala, catálogos o fichas de museo: quién aparece, qué se dice, cómo se legitima y cómo se atribuye a las comunidades de origen.

## Pasos
1. Clasificar cada texto con `references/clases-de-texto.md` (o `scripts/texto_clase.py` como modelo). Analizar solo cédulas e interpretativos; los de inventario aparte.
2. Elegir las variables de `references/matrices.md` (matriz operativa) según la pregunta de investigación.
3. Codificar siguiendo `references/flujo-codificacion.md`: precodificación automática, luego revisión manual.
4. Reportar con la proporción revisada, intervalo de Wilson de la cobertura y sesgo por museo.

## Reglas
- Contar piezas solo con las filas de tipo objeto.
- Nunca presentar la codificación automática sin revisar como resultado.
- Los textos de museo son de terceros: citar fragmentos breves, no reproducirlos completos.
- Corpus multilingüe: indicar el idioma de cada texto.
