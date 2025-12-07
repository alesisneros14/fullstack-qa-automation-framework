# 🚀 FullStack QA Automation Framework

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4-green)
![Build](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange)
![Pattern](https://img.shields.io/badge/Pattern-Page%20Object%20Model-purple)

Este repositorio contiene un framework de pruebas automatizadas **híbrido** diseñado para validar aplicaciones web modernas. Simula un entorno empresarial real abarcando pruebas de **Frontend (UI)**, **Backend (API)** y **Base de Datos**, todo orquestado bajo un pipeline de Integración Continua.

## 🛠️ Tecnologías y Arquitectura

El proyecto sigue las mejores prácticas de la industria para garantizar escalabilidad y mantenibilidad:

*   **Lenguaje:** Python 3.12+
*   **Web Automation:** Selenium WebDriver (Gestión dinámica de drivers).
*   **API Automation:** Requests (Validación de endpoints REST).
*   **Test Runner:** Pytest (con fixtures para manejo de setup/teardown).
*   **Patrón de Diseño:** **Page Object Model (POM)** para desacoplar la lógica de prueba de los elementos UI.
*   **CI/CD:** GitHub Actions para ejecución automática de pruebas en cada Push.
*   **Infraestructura:**
    *   **Docker:** Contenerización de la aplicación y pruebas.
    *   **GitOps:** Manifiestos de Kubernetes (`/k8s`) listos para despliegue continuo con **ArgoCD**.

## 📂 Estructura del Proyecto

```text
├── .github/workflows  # Pipeline de CI/CD (GitHub Actions)
├── app/               # Aplicación Web y API (Flask) simulada para pruebas
├── k8s/               # Manifiestos de infraestructura (GitOps/ArgoCD)
├── tests/
│   ├── pages/         # Page Objects (Mapeo de elementos y acciones)
│   │   ├── base_page.py   # Wrapper para esperas explícitas (WebDriverWait)
│   │   └── login_page.py  # Lógica específica de la página de Login
│   ├── test_ui.py     # Pruebas End-to-End de la interfaz
│   ├── test_api.py    # Pruebas de integración de API
│   └── conftest.py    # Configuración global de Pytest (Drivers, Headless mode)
└── requirements.txt   # Dependencias del proyecto