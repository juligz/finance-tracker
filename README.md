# Finance Tracker

Rastreador de finanzas personales construido con Python 3.12.

## Stack

- Python 3.12 (via pyenv)
- SQLAlchemy 2.0 + SQLite (desarrollo) / PostgreSQL (producción)
- Typer (CLI)
- FastAPI + JWT (API REST)
- Pandas (analytics)
- React (frontend)
- Celery + Redis (tareas asíncronas)
- Docker + GitHub Actions (CI/CD)

## Configuración del entorno

### Requisitos
- pyenv instalado
- Python 3.12.13

### Instalación
```bash
git clone https://github.com/juligz/finance-tracker.git
cd finance-tracker
pyenv local 3.12.13
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Decisiones técnicas

### Por qué venv y no virtualenv o poetry

Se evaluaron tres opciones para gestionar el entorno virtual:

- **virtualenv**: herramienta externa más antigua, precursora de venv.
  Requiere instalación separada y no agrega valor para este proyecto.

- **poetry**: gestor de dependencias avanzado con lockfile y
  publicación de paquetes. Ideal para librerías, agrega complejidad
  innecesaria para una aplicación.

- **venv**: incluido en Python desde 3.3, sin dependencias externas,
  suficiente para gestionar el entorno de una aplicación. Es la
  opción más simple y estándar para este caso de uso.

**Elección: venv** por simplicidad, por estar incluido en Python
y por ser suficiente para las necesidades del proyecto.

## Flujo de trabajo Git

Este proyecto usa el flujo feature branch:
- `main` contiene siempre código estable
- Cada nueva funcionalidad se desarrolla en su propia rama
- Nunca se commitea directamente a `main`
```bash
git checkout -b feature/nombre-de-la-funcionalidad
# desarrollar...
git push origin feature/nombre-de-la-funcionalidad
# abrir Pull Request en GitHub
```
