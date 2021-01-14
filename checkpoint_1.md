![](/images/itam_logo.png)

M. Sc. Liliana Millán Núñez liliana.millan@itam.mx

Enero 2021

### Checkpoint 1

**Jueves 21 enero 2021 23:59:59 CST**

+ Repositorio del proyecto
+ Agregarme a su repo, mi usuario es `silil`
+ README.md
  + Integrantes del equipo
  + Summary de los datos con los que trabajarás:
    + Número de registros
    + Número de columnas
    + Qué variables son, qué información tiene
  + Pregunta analítica a contestar con el modelo predictivo
  + Frecuencia de actualización de los datos
+ Estructura básica del proyecto (recuerda ocupar .gitkeep para subir carpetas vacías a github). Ver Figura 1
+ EDA (en la carpeta `notebooks/eda`)
  + 5 visualizaciones de sus datos, una de ellas debe ser un mapa indicando las inspecciones que pasaron y las que no (histórico)
+ `requirements.txt` con las librerías que ocupes hasta el momento de la entrega (`pip freeze > requirements.txt`)



```
├── README.md          <- The top-level README for developers using this project.
├── conf
│   ├── base           <- Space for shared configurations like parameters
│   └── local          <- Space for local configurations, usually credentials
│
├── docs               <- Space for Sphinx documentation
│
├── notebooks          <- Jupyter notebooks.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── results            <- Intermediate analysis as HTML, PDF, LaTeX, etc.
│
├── requirements.txt   <- The requirements file
│
├── .gitignore         <- Avoids uploading data, credentials, outputs, system files etc
│
├── infrastructure
├── sql
├── setup.py
└── src                <- Source code for use in this project.
    ├── __init__.py    <- Makes src a Python module
    │
    ├── utils      <- Functions used across the project
    │
    │
    ├── etl       <- Scripts to transform data from raw to intermediate
    │
    │
    ├── pipeline
```
Figura 1. Estructura básica del proyecto.

![](images/pointer.png) La carpeta `conf/local` **NO** debe subirse a github, agrégala a tu `.gitignore`.
