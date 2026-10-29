# QA Project — Urban Grocers: API Test Automation

Proyecto de automatización de pruebas para la API de Urban Grocers. Se valida el endpoint de creación de kits usando clases de equivalencia y análisis de valores límite.

## Contexto

Urban Grocers es una aplicación de delivery. El objetivo es automatizar la validación del campo `name` en el endpoint `POST /api/v1/kit`, cubriendo casos positivos y negativos.

## Casos de prueba automatizados (9)

| # | Caso | Resultado esperado |
|---|------|--------------------|
| 1 | Nombre con 1 carácter | 201 Created |
| 2 | Nombre con 511 caracteres | 201 Created |
| 3 | Nombre vacío (0 caracteres) | 400 Bad Request |
| 4 | Nombre con 512 caracteres | 400 Bad Request |
| 5 | Caracteres especiales en el nombre | 201 Created |
| 6 | Espacios en el nombre | 201 Created |
| 7 | Números como string | 201 Created |
| 8 | Parámetro `name` ausente en el body | 400 Bad Request |
| 9 | Tipo numérico en lugar de string | 400 Bad Request |

## Técnica de diseño

- **Clases de equivalencia**: valores válidos (1–511 chars) vs. inválidos
- **Valores límite**: extremos del rango permitido (1, 511, 0, 512)
- **Tipos de dato**: validación del tipo esperado (string vs. número)

## Tecnologías

- Python 3.14
- Pytest
- Requests

## Estructura del proyecto

- `create_kit_name_kit_test.py` — casos de prueba
- `sender_stand_request.py` — funciones para enviar requests a la API
- `data.py` — datos de prueba centralizados
- `configuration.py` — configuración de la URL base
- `test_results.txt` — resultados de ejecución

## Cómo ejecutar las pruebas

1. Instalar dependencias: `pip install requests pytest`
2. Ejecutar pruebas: `pytest create_kit_name_kit_test.py -v`
