# 🛠️ Proyecto Django GraphQL API con Autenticación

## 📋 Descripción
Este proyecto es una API basada en Django que utiliza GraphQL (a través de la librería graphene-django) para proporcionar una interfaz flexible para la gestión de usuarios y enlaces (links). Además, incluye autenticación JWT para asegurar los endpoints y permitir la obtención y verificación de tokens, así como su renovación.

## 🌟 Características Principales
* __GraphQL API:__ Consultas y mutaciones para gestionar usuarios y enlaces.
* __Autenticación JWT__:
  * Generación de tokens.
  * Verificación de tokens.
  * Renovación de tokens.
* __Docker:__ Configuración de Docker y Docker Compose para desplegar la aplicación de forma rápida.
* __Variables de entorno:__ Uso de un archivo .env para gestionar las configuraciones sensibles.
* __Modularidad:__ Organización clara y modular con aplicaciones independientes (users y links).
