
# LiteStart

<p align="center">
  <img src="assets/icons/icon.svg" alt="LiteStart Logo" width="128">
</p>

<p align="center">
  <strong>Un menú de inicio moderno, ligero y rápido para Linux.</strong>
</p>

<p align="center">
  Inspirado en la experiencia de los lanzadores modernos, construido con Python y PyQt6.
</p>

---

## Estado del Proyecto

![Status](https://img.shields.io/badge/status-alpha-orange)
![Platform](https://img.shields.io/badge/platform-Linux-blue)
![Python](https://img.shields.io/badge/python-3.14+-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## Características

| Función | Estado |
|----------|----------|
| Búsqueda de aplicaciones | ✅ |
| Aplicaciones ancladas | ✅ |
| Lanzamiento mediante archivos `.desktop` | ✅ |
| Iconos dinámicos del sistema | ✅ |
| Menú de energía | ✅ |
| System Tray | ✅ |
| Empaquetado con PyInstaller | ✅ |
| AppImage | 🚧 |
| Configuración gráfica | 🚧 |

---


## Objetivos

LiteStart busca ofrecer una alternativa ligera y moderna a los lanzadores tradicionales de Linux, manteniendo:

- Simplicidad
- Rapidez
- Bajo consumo de recursos
- Integración con el ecosistema Linux

---

## Tecnologías Utilizadas

- Python 3.14
- PyQt6
- PyInstaller
- Freedesktop Desktop Entries
- SVG Icons

---

## Instalación

### Opción 1 — Ejecutable

Descarga la última versión desde la sección Releases.

Otorga permisos de ejecución:

```bash
chmod +x LiteStart
````

Ejecuta:

```bash
./LiteStart
```

---

### Opción 2 — Desde el código fuente

Clonar el repositorio:

```bash
git clone https://github.com/GatoLocoYT/LiteStart.git
cd LiteStart
```

Crear entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar:

```bash
python main.py
```

---

## Integración con el Menú de Aplicaciones

Copiar el archivo `.desktop`:

```bash
cp LiteStart.desktop ~/.local/share/applications/
```

Actualizar la base de datos:

```bash
update-desktop-database ~/.local/share/applications
```

---

## Estructura del Proyecto

```text
LiteStart/
│
├── assets/
│   └── icons/
│
├── config/
│
├── core/
│
├── styles/
│
├── ui/
│
├── main.py
├── requirements.txt
└── LiteStart.desktop
```

### Directorios

| Carpeta  | Descripción                |
| -------- | -------------------------- |
| `assets` | Recursos visuales e iconos |
| `config` | Configuración del usuario  |
| `core`   | Lógica principal           |
| `styles` | Temas y estilos            |
| `ui`     | Componentes gráficos       |

---

## Roadmap

### Versión 1.x

* [x] Menú principal
* [x] Buscador
* [x] Aplicaciones ancladas
* [x] Power Menu
* [x] Tray Icon
* [x] Empaquetado PyInstaller
* [ ] AppImage
* [ ] Instalador simplificado
* [ ] Configuración gráfica

### Futuro

* [ ] Temas personalizables
* [ ] Acciones rápidas
* [ ] Mejor integración con KDE
* [ ] Mejor integración con XFCE
* [ ] Soporte para múltiples temas

---

## Compatibilidad

Actualmente probado en:

* Ubuntu 26.04 LTS

Compatibilidad esperada:

* Ubuntu
* Linux Mint
* Debian
* Kubuntu
* Xubuntu
* Lubuntu

---

## Contribuciones

Las contribuciones, sugerencias y reportes de errores son bienvenidos.

Si encuentras un problema:

1. Abre un Issue.
2. Describe el comportamiento.
3. Adjunta capturas si es posible.

---

## Licencia

Este proyecto está distribuido bajo la licencia MIT.

Consulta el archivo:

```text
LICENSE
```

para más información.

---

## Autor

**Ramiro Rahman Rintoul**

GitHub: https://github.com/GatoLocoYT

---

LiteStart nació como un proyecto personal para explorar el desarrollo de aplicaciones de escritorio modernas para Linux utilizando Python y PyQt6.

```
```
