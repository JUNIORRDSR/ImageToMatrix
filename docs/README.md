# Documentación de ImageToMatrix API

## Descripción General

ImageToMatrix es una API para convertir imágenes a matrices numéricas para su procesamiento posterior. La API está diseñada como un microservicio independiente que puede integrarse fácilmente en una arquitectura de microservicios más grande.

## Arquitectura

El proyecto sigue una arquitectura en capas:

```
ImageToMatrix/
├── src/                  # Código fuente principal
│   ├── api/              # Endpoints de la API y controladores
│   ├── services/         # Lógica de negocio
│   ├── utils/            # Utilidades
│   └── config/           # Configuración
```

### Componentes Principales

1. **API Layer**: Gestiona las peticiones HTTP entrantes y las respuestas.
2. **Service Layer**: Contiene la lógica de negocio para el procesamiento de imágenes.
3. **Utilities**: Funciones auxiliares para el procesamiento y la validación.
4. **Configuration**: Gestión de configuraciones y variables de entorno.

## Endpoints

### `GET /health`

Comprueba si la API está funcionando correctamente.

**Respuesta**:
```json
{
  "status": "healthy"
}
```

### `POST /api/v1/convert`

Convierte una imagen a una matriz numérica.

**Parámetros**:
- `image`: Archivo de imagen a convertir (multipart/form-data)
- `format`: Formato de salida (json, numpy)
- `preprocess`: Opciones de preprocesamiento como una lista (grayscale, normalize, resize_WxH)

**Cabeceras**:
- `X-API-Key`: Clave API para autenticación

**Ejemplo de respuesta (formato json)**:
```json
{
  "matrix": [[[255, 0, 0], [255, 0, 0]], [[255, 0, 0], [255, 0, 0]]],
  "shape": [2, 2, 3],
  "dtype": "uint8"
}
```

## Opciones de Preprocesamiento

- `grayscale`: Convierte la imagen a escala de grises
- `normalize`: Normaliza los valores de píxeles al rango [0, 1]
- `resize_WxH`: Redimensiona la imagen al ancho W y alto H especificados

## Integración como Microservicio

Para integrar esta API en una arquitectura de microservicios:

1. **Docker**: El proyecto incluye un Dockerfile y docker-compose.yml para facilitar la containerización.
2. **Variables de Entorno**: La configuración se gestiona a través de variables de entorno.
3. **Healthcheck**: Endpoint /health para monitoreo.
4. **API Gateway**: Compatible con API Gateway para gestión centralizada.

## Escalabilidad

La API está diseñada para ser escalada horizontalmente:

1. **Stateless**: No mantiene estado entre peticiones.
2. **Containerización**: Fácil de escalar con Kubernetes o Docker Swarm.
3. **Configuración Externalizada**: Separación de configuración y código.

## Seguridad

- Autenticación mediante API Key
- Validación de tipos de archivos y tamaño máximo
- Sanitización de entradas

## Monitorización

- Logging detallado de cada petición
- Métricas de tiempo de procesamiento
- Compatible con herramientas estándar de monitorización de microservicios
