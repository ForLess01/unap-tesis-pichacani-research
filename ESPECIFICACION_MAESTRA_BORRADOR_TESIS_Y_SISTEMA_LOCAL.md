# ESPECIFICACIÓN MAESTRA PARA EL BORRADOR DE TESIS Y EL SISTEMA LOCAL

**Universidad:** Universidad Nacional del Altiplano – Puno  
**Facultad:** Facultad de Ingeniería Mecánica Eléctrica, Electrónica y Sistemas  
**Escuela profesional:** Escuela Profesional de Ingeniería de Sistemas  
**Tesista:** Rendo Alfonte Tarqui  
**Título de investigación:** **Sistema de soporte a decisiones geoespacial multicriterio para evaluar la sostenibilidad territorial de puestos de salud rurales en Pichacani, Puno, 2026**  
**Año:** 2026  
**Estado del documento:** especificación de trabajo para construir el borrador de tesis, ejecutar el análisis y desarrollar el prototipo completamente en local.

---

# PARTE A. INSTRUCCIONES OBLIGATORIAS PARA CODEX

## A.1. Objetivo de esta especificación

Codex debe usar este archivo como **fuente maestra de requisitos académicos, documentales, matemáticos y técnicos**. Debe producir dos entregables relacionados, pero independientes:

1. **Borrador de tesis** conforme a la plantilla de la Universidad Nacional del Altiplano proporcionada por el tesista.
2. **Sistema de soporte a decisiones geoespacial multicriterio** ejecutable completamente en local, con una canalización reproducible de datos, cálculo del modelo, generación de mapas, análisis de escenarios y exportación de resultados.

El sistema debe generar los datos, tablas y figuras que posteriormente alimentarán los capítulos IV, V y VI de la tesis. El documento no debe contener resultados inventados ni valores de demostración presentados como si fueran hallazgos reales.

## A.2. Reglas no negociables

1. **No inventar datos, resultados, nombres de jurados, nombre del asesor, coordenadas, establecimientos, población, pesos AHP, umbrales normativos, tiempos de viaje ni conclusiones.**
2. Todo dato de resultado debe provenir de un archivo trazable ubicado en `data/`, de una tabla de la base de datos o de un artefacto generado por el código.
3. Si falta un dato necesario, usar un marcador con la forma `{{PENDIENTE: descripción exacta}}`. Nunca completar el vacío por intuición.
4. El modo de compilación `final` debe fallar cuando exista algún marcador `{{PENDIENTE: ...}}`, `{{RESULTADO: ...}}` o `{{VERIFICAR: ...}}`.
5. El borrador puede compilarse en modo `draft`, pero debe mostrar en el encabezado o marca de agua: **BORRADOR — RESULTADOS PENDIENTES DE EJECUCIÓN**.
6. Las citas deben generarse desde un archivo local `references.bib`; no se deben escribir manualmente citas parentéticas duplicadas como “Wood et al. ... Wood et al. (2023)”.
7. Todas las referencias citadas deben aparecer en la bibliografía y ninguna referencia no citada debe mantenerse en la versión final.
8. Las tablas tendrán el título en la parte superior. Las figuras tendrán el título en la parte inferior.
9. Las tablas y figuras deben numerarse arábiga y consecutivamente según el orden de aparición.
10. Las figuras, mapas, gráficos y diagramas deben estar próximos al párrafo donde se citan.
11. El resumen final debe ser un único párrafo de máximo 350 palabras, sin referencias bibliográficas y con máximo cinco palabras clave.
12. La introducción final debe ocupar como máximo dos páginas en el formato oficial y debe terminar con el objetivo general y los objetivos específicos.
13. Debe existir una conclusión por cada objetivo específico. En esta tesis deben existir **cuatro conclusiones**.
14. No se debe afirmar que un establecimiento debe cerrarse. El sistema solo debe **evaluar pertinencia territorial y simular escenarios de permanencia, fortalecimiento, reubicación o creación**.
15. El proyecto no tratará datos clínicos ni historias clínicas. No almacenar datos personales de pacientes.
16. Todo el procesamiento debe ejecutarse en local. No depender de APIs remotas durante la ejecución normal del sistema.
17. Los datos descargados previamente de fuentes oficiales pueden importarse desde archivos locales, conservando fecha, URL de origen, licencia, checksum y responsable de descarga.
18. La plantilla oficial `.docx` de la UNA es la fuente de verdad para márgenes, tipografía, interlineado y estilos. Si el archivo oficial no está disponible, Codex debe detener la generación definitiva y solicitarlo; no debe afirmar que un formato supuesto es oficial.
19. El contenido metodológico debe distinguir claramente entre:
    - fórmulas guía de coherencia metodológica;
    - fórmulas efectivamente implementadas por el modelo;
    - fórmulas revisadas pero no aplicables al diseño.
20. Cada fórmula implementada debe tener una función de código, pruebas unitarias y un archivo de resultados reproducible.

## A.3. Entradas mínimas

Codex debe trabajar con las siguientes entradas locales:

```text
assets/plantilla_una.docx               # plantilla oficial, obligatoria para versión final
assets/logo_una.png                      # solo si la plantilla oficial lo requiere
references/references.bib               # bibliografía local
references/apa7-es.csl                  # estilo APA 7 en español, local
content/tesis.md                         # contenido académico
config/research.yml                     # parámetros metodológicos
config/criteria.yml                     # criterios, dirección y pesos
config/scenarios.yml                    # escenarios de simulación
data/raw/                                # archivos originales sin modificar
data/interim/                            # datos depurados intermedios
data/processed/                          # datos finales de análisis
outputs/tables/                          # CSV/XLSX/Markdown de tablas
outputs/figures/                         # PNG/SVG/PDF de figuras
outputs/reports/                         # reportes de calidad, validación y reproducibilidad
```

## A.4. Salidas obligatorias

```text
build/Borrador_Tesis_Rendo_Alfonte_Tarqui.docx
build/Borrador_Tesis_Rendo_Alfonte_Tarqui.pdf
build/Informe_reproducibilidad.html
build/Reporte_calidad_datos.html
build/Reporte_validacion_modelo.html
build/Reporte_pruebas_sistema.html
build/manifest.json
```

El archivo `manifest.json` debe registrar versión del código, fecha de ejecución, hashes de entradas, parámetros utilizados y hashes de salidas.

## A.5. Estructura recomendada del repositorio local

```text
tesis-pichacani/
├── README.md
├── Makefile
├── docker-compose.yml
├── .env.example
├── .gitignore
├── pyproject.toml
├── package.json
├── config/
│   ├── research.yml
│   ├── criteria.yml
│   ├── scenarios.yml
│   └── logging.yml
├── assets/
│   ├── plantilla_una.docx
│   └── logo_una.png
├── content/
│   ├── tesis.md
│   ├── frontmatter.md
│   ├── annexes.md
│   └── placeholders.yml
├── references/
│   ├── references.bib
│   └── apa7-es.csl
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── metadata/
├── etl/
│   ├── import_facilities.py
│   ├── import_population_centers.py
│   ├── import_demographics.py
│   ├── import_roads.py
│   ├── validate_spatial_data.py
│   └── build_network.py
├── model/
│   ├── normalization.py
│   ├── ahp.py
│   ├── indicators.py
│   ├── ist.py
│   ├── scenarios.py
│   ├── sensitivity.py
│   └── validation.py
├── backend/
│   ├── manage.py
│   ├── config/
│   └── apps/
│       ├── catalog/
│       ├── geography/
│       ├── multicriteria/
│       ├── scenarios/
│       └── exports/
├── frontend/
│   ├── src/
│   └── tests/
├── document/
│   ├── build_docx.py
│   ├── postprocess_docx.py
│   ├── validate_document.py
│   └── render_pdf.sh
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── spatial/
│   └── fixtures/
├── outputs/
│   ├── tables/
│   ├── figures/
│   └── reports/
└── build/
```

## A.6. Comandos locales requeridos

El `Makefile` debe incluir, como mínimo:

```makefile
make setup             # prepara el entorno local
make db                # inicia PostgreSQL/PostGIS
make data-audit        # valida datos brutos sin modificarlos
make etl               # genera datos procesados
make criteria          # procesa matrices de expertos y AHP
make model             # calcula indicadores e IST
make scenarios         # ejecuta escenarios
make figures           # genera todas las figuras
make tables            # genera todas las tablas
make app               # inicia backend y frontend local
make test              # ejecuta pruebas completas
make thesis-draft      # genera DOCX/PDF con marcadores permitidos
make thesis-final      # falla si existen marcadores o resultados sin trazabilidad
make reproduce         # ejecuta todo desde cero y crea manifest
```

## A.7. Reglas de generación del documento

1. El archivo fuente será Markdown con ecuaciones LaTeX y citas Pandoc.
2. Generar DOCX con Pandoc usando `--reference-doc=assets/plantilla_una.docx`.
3. Usar el archivo CSL local y la configuración de idioma español para mostrar “s. f.”, “y” y demás convenciones APA 7 en español.
4. Insertar campos automáticos de Word para:
   - índice general;
   - índice de figuras;
   - índice de tablas;
   - numeración de páginas.
5. Configurar `w:updateFields` para que Word solicite o realice la actualización de campos al abrir el documento.
6. Usar saltos de sección para páginas horizontales únicamente cuando una tabla no pueda presentarse legiblemente en orientación vertical.
7. No escribir números de página manuales en los índices.
8. No incluir en el documento final notas dirigidas a Codex ni bloques de requisitos técnicos.
9. Conservar en el repositorio una versión `tesis_con_anotaciones.md`; compilar el documento final desde `tesis.md` sin anotaciones.

---

# PARTE B. DATOS DE PORTADA Y PÁGINAS PRELIMINARES

## B.1. Portada

Usar exactamente el orden y jerarquía de la plantilla oficial:

```text
UNIVERSIDAD NACIONAL DEL ALTIPLANO - PUNO
FACULTAD DE INGENIERÍA MECÁNICA ELÉCTRICA, ELECTRÓNICA Y SISTEMAS
ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS

SISTEMA DE SOPORTE A DECISIONES GEOESPACIAL MULTICRITERIO PARA EVALUAR LA SOSTENIBILIDAD TERRITORIAL DE PUESTOS DE SALUD RURALES EN PICHACANI, PUNO, 2026

BORRADOR DE TESIS

PRESENTADA POR:
Bach. Rendo Alfonte Tarqui

PARA OPTAR EL TÍTULO PROFESIONAL DE:
INGENIERO DE SISTEMAS

PUNO – PERÚ
2026
```

**Validación obligatoria:** confirmar que el tesista ya puede usar oficialmente la denominación “Bach.”. Si no corresponde, mantener `{{PENDIENTE: grado académico exacto del autor}}`.

## B.2. Página de aprobación

```text
UNIVERSIDAD NACIONAL DEL ALTIPLANO - PUNO
FACULTAD DE INGENIERÍA MECÁNICA ELÉCTRICA, ELECTRÓNICA Y SISTEMAS
ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS

BORRADOR DE TESIS

SISTEMA DE SOPORTE A DECISIONES GEOESPACIAL MULTICRITERIO PARA EVALUAR LA SOSTENIBILIDAD TERRITORIAL DE PUESTOS DE SALUD RURALES EN PICHACANI, PUNO, 2026

PRESENTADA POR:
Bach. Rendo Alfonte Tarqui

PARA OPTAR EL TÍTULO PROFESIONAL DE:
INGENIERO DE SISTEMAS

APROBADA POR:

PRESIDENTE:             ____________________________________
                        {{PENDIENTE: grado y nombre del presidente de jurado}}

PRIMER MIEMBRO:         ____________________________________
                        {{PENDIENTE: grado y nombre del primer miembro}}

SEGUNDO MIEMBRO:        ____________________________________
                        {{PENDIENTE: grado y nombre del segundo miembro}}

DIRECTOR / ASESOR:      ____________________________________
                        {{PENDIENTE: grado y nombre del asesor}}

Área    : Ingeniería de Sistemas
Tema    : Sistemas de soporte a decisiones geoespaciales y análisis multicriterio aplicados a la planificación territorial de la salud rural
```

## B.3. Índices automáticos

Codex debe generar automáticamente:

- ÍNDICE GENERAL
- ÍNDICE DE FIGURAS
- ÍNDICE DE TABLAS
- ÍNDICE DE ACRÓNIMOS

No copiar los ejemplos de la plantilla como contenido final.

## B.4. Acrónimos previstos

Incluir únicamente los acrónimos realmente usados y definir cada uno la primera vez que aparezca en el texto.

| Acrónimo | Significado |
|---|---|
| AHP | Proceso Analítico Jerárquico |
| API | Interfaz de Programación de Aplicaciones |
| DIRESA | Dirección Regional de Salud |
| GIS / SIG | Sistema de Información Geográfica |
| INEI | Instituto Nacional de Estadística e Informática |
| IST | Índice de Sostenibilidad Territorial |
| MCDA | Análisis de Decisión Multicriterio |
| MINSA | Ministerio de Salud |
| OSM | OpenStreetMap |
| RENIPRESS | Registro Nacional de Instituciones Prestadoras de Servicios de Salud |
| SDSS | Sistema de Soporte a Decisiones Espaciales |
| SUSALUD | Superintendencia Nacional de Salud |
| WLC | Combinación Lineal Ponderada |

Eliminar los acrónimos que no se utilicen en el texto final.

---

# PARTE C. CONTENIDO ACADÉMICO DEL BORRADOR DE TESIS

## C.0. Regla sobre el estado de resultados

Los capítulos I, II y III pueden redactarse antes de ejecutar la investigación. Los capítulos IV, V y parte de VI deben completarse únicamente con resultados generados por el sistema y validados. En modo borrador se usarán marcadores; en modo final no debe quedar ninguno.

## RESUMEN

### Texto provisional de trabajo — no presentar como resumen final

La investigación tiene como propósito desarrollar un sistema de soporte a decisiones geoespacial multicriterio para evaluar la sostenibilidad territorial de puestos de salud rurales en el distrito de Pichacani, Puno, durante 2026. El problema se relaciona con la dispersión de la información sobre establecimientos, centros poblados, población, vías y cobertura, lo que limita una evaluación territorial integrada del primer nivel de atención. El estudio es aplicado, de enfoque cuantitativo, diseño no experimental y alcance descriptivo-propositivo. Se emplearán datos oficiales y abiertos provenientes de RENIPRESS, GeoMINSA, INEI, Red de Salud Puno y archivos locales derivados de OpenStreetMap. La metodología comprenderá la caracterización territorial, la definición y validación de criterios, el cálculo de un Índice de Sostenibilidad Territorial mediante normalización y ponderación multicriterio, y la implementación de un prototipo local con mapas, ranking y análisis de escenarios. La evaluación considerará demanda poblacional, accesibilidad geográfica, cobertura territorial, singularidad de cobertura frente a otros establecimientos y vulnerabilidad poblacional. El modelo y el prototipo serán validados mediante juicio de expertos, análisis de consistencia, análisis de sensibilidad y pruebas funcionales. `{{RESULTADO: principal hallazgo cuantitativo}}`. `{{RESULTADO: desempeño del prototipo y validación}}`. Se concluye que `{{RESULTADO: conclusión general sustentada en los resultados}}`.

**Palabras clave:** soporte a decisiones, análisis geoespacial, multicriterio, sostenibilidad territorial, puestos de salud.

### Regla para el resumen final

- Un solo párrafo.
- Máximo 350 palabras.
- Debe contener problema, lugar, periodo, justificación, objetivo, métodos, resultados principales y conclusión.
- No incluir citas.
- No incluir resultados esperados; incluir resultados reales.
- El comando `make thesis-final` debe comprobar automáticamente el conteo de palabras y la ausencia de marcadores.

## ABSTRACT

### Working draft — not for final submission

This research aims to develop a multicriteria geospatial decision support system to assess the territorial sustainability of rural health posts in the district of Pichacani, Puno, in 2026. The problem concerns the fragmentation of information on health facilities, population centres, population, roads and service coverage, which limits an integrated territorial assessment of primary health care. The study follows an applied, quantitative, non-experimental and descriptive-propositional design. Official and open data from RENIPRESS, GeoMINSA, the National Institute of Statistics and Informatics, the Puno Health Network and local OpenStreetMap-derived files will be used. The methodology includes territorial characterisation, definition and expert validation of criteria, calculation of a Territorial Sustainability Index through normalisation and multicriteria weighting, and implementation of a local prototype with maps, rankings and scenario analysis. The assessment considers population demand, geographic accessibility, territorial coverage, uniqueness of coverage relative to other facilities and population vulnerability. The model and prototype will be validated through expert judgement, consistency analysis, sensitivity analysis and functional testing. `{{RESULT: main quantitative finding}}`. `{{RESULT: prototype and validation performance}}`. It is concluded that `{{RESULT: overall conclusion supported by evidence}}`.

**Keywords:** decision support, geospatial analysis, multicriteria, territorial sustainability, health posts.

---

# I. INTRODUCCIÓN

El primer nivel de atención constituye el punto inicial de contacto entre la población y el sistema sanitario, y adquiere especial relevancia en territorios rurales donde las distancias, la dispersión de centros poblados y las limitaciones de la red vial pueden convertir la localización de un establecimiento en un factor determinante del acceso efectivo. La existencia administrativa de un puesto de salud no garantiza por sí sola que su ubicación responda a la distribución actual de la población ni que su área de influencia sea accesible en condiciones reales. La literatura sobre accesibilidad espacial señala que las medidas basadas únicamente en distancia euclidiana pueden ocultar barreras asociadas al relieve, la conectividad vial y los tiempos de viaje [@wood2023; @verma2020; @bhangdia2022].

En el Perú, el análisis de tiempos de viaje hacia establecimientos de salud ha mostrado la necesidad de integrar cobertura del suelo, vías, hidrografía y elevación para representar de manera más realista la accesibilidad geográfica [@carrasco2020]. Esta necesidad es especialmente pertinente en ámbitos altoandinos como Pichacani, donde los centros poblados se encuentran dispersos y la movilidad puede depender de rutas secundarias o no pavimentadas. A ello se suma que la información relevante para la planificación se encuentra distribuida entre registros de establecimientos, plataformas geográficas, información censal y documentos de gestión institucional [@inei2018; @minsa_geomin; @susalud_renipress; @redsaludpuno2024].

Los Sistemas de Información Geográfica permiten integrar y representar estas fuentes; sin embargo, un visor cartográfico no resuelve por sí solo el problema de decisión. La evaluación de la pertinencia territorial requiere combinar criterios heterogéneos, entre ellos demanda poblacional, accesibilidad, cobertura, superposición con otros establecimientos y vulnerabilidad. El Análisis de Decisión Multicriterio y el Proceso Analítico Jerárquico permiten estructurar estos criterios, asignar pesos verificables y documentar la consistencia de las preferencias expertas [@frazao2018; @aroge2023; @tripathi2022; @zandi2024]. Los modelos de localización-asignación y accesibilidad complementan este enfoque al permitir comparar la situación actual con escenarios alternativos [@polo2015; @murad2021; @murad2024; @pan2023; @balsa2025].

En esta investigación, la sostenibilidad territorial se define operacionalmente como el grado en que la ubicación de un puesto de salud, su población de influencia, su accesibilidad, su cobertura, su singularidad frente a otros establecimientos y la vulnerabilidad de la población justifican su pertinencia dentro de la red rural. Esta definición no equivale a sostenibilidad ambiental o financiera y no autoriza decisiones automáticas de cierre. El sistema propuesto debe proporcionar evidencia trazable para analizar escenarios de permanencia, fortalecimiento, reubicación o creación, mientras la decisión administrativa corresponde a las autoridades competentes.

El problema general se formula así: **¿Cómo evaluar la sostenibilidad territorial de los puestos de salud rurales en Pichacani, Puno, mediante un sistema de soporte a decisiones geoespacial multicriterio durante 2026?** La investigación busca superar la evaluación fragmentada mediante una base territorial integrada, un modelo multicriterio reproducible y un prototipo que permita visualizar resultados y simular cambios en la red.

El objetivo general es **desarrollar un sistema de soporte a decisiones geoespacial multicriterio para evaluar la sostenibilidad territorial de puestos de salud rurales en Pichacani, Puno, 2026**. Los objetivos específicos son: **1)** caracterizar la distribución territorial de los puestos de salud rurales, centros poblados, población y vías de acceso; **2)** definir las dimensiones, criterios e indicadores para evaluar la sostenibilidad territorial; **3)** diseñar un modelo multicriterio ponderado que calcule un Índice de Sostenibilidad Territorial; y **4)** implementar y validar un prototipo con visualización cartográfica, ranking y análisis de escenarios.

**Control de extensión:** Codex debe ajustar esta sección para que, al aplicar la plantilla oficial, no exceda dos páginas. No reducir los objetivos ni eliminar la delimitación del problema.

---

# II. REVISIÓN DE LITERATURA

## 2.1. Atención primaria, ruralidad y barreras de acceso

La atención primaria en zonas rurales presenta retos que exceden la disponibilidad nominal de infraestructura. Las barreras pueden originarse en la distancia, el costo del desplazamiento, la organización del servicio, la disponibilidad de personal y la dispersión territorial. Las revisiones sobre atención primaria rural identifican dificultades de acceso y organización que requieren respuestas diferenciadas respecto de los entornos urbanos [@franco2021]. En comunidades rurales y dispersas de las Américas, el análisis de barreras debe considerar las condiciones locales y la forma en que la población utiliza realmente la red de servicios [@houghton2023]. En la Amazonía, las barreras de acceso y la organización de servicios para poblaciones rurales muestran que la proximidad cartográfica no siempre representa accesibilidad efectiva [@garnelo2020].

Para la presente tesis, estos antecedentes sustentan la inclusión de variables territoriales y de vulnerabilidad, pero también delimitan el alcance: el modelo no medirá calidad clínica ni desempeño del personal, debido a que no se contará con información clínica u operativa individual. El análisis se concentrará en pertinencia territorial y utilizará únicamente variables verificables disponibles en fuentes oficiales o validadas por expertos.

## 2.2. Accesibilidad geográfica y tiempo de viaje

La accesibilidad geográfica puede medirse mediante distancias, tiempos de viaje, áreas de servicio o métodos que relacionan oferta y demanda. Las revisiones de medidas espaciales señalan que la elección del método afecta la interpretación de la equidad y debe documentarse de manera transparente [@wood2023]. En zonas rurales de Polonia, la relación entre población, ubicación de establecimientos y desplazamiento evidenció diferencias de acceso que no podían describirse únicamente con la existencia de centros [@lechowski2021]. En India rural y remota, la topografía, la capacidad de los servicios y la red vial se asociaron con desigualdades de cobertura [@verma2020]. En Haití rural, las medidas absolutas y relativas de tiempo y distancia produjeron perspectivas diferentes del acceso [@bhangdia2022].

Carrasco-Escobar et al. [@carrasco2020] estimaron tiempos de viaje hacia establecimientos de salud en el Perú integrando centros poblados, red vial, cobertura terrestre, ríos y elevación. Este antecedente respalda el uso de tiempos de viaje por red o superficie de costo. En esta tesis se priorizará el cálculo por red vial cuando el grafo tenga conectividad suficiente; cuando una ruta no exista o el grafo sea incompleto, el caso se marcará como no calculable y no se sustituirá silenciosamente por distancia en línea recta.

## 2.3. Sistemas de información geográfica y modelos de localización-asignación

Los modelos de localización-asignación permiten relacionar puntos de demanda con establecimientos existentes o candidatos. Polo et al. [@polo2015] integraron accesibilidad y localización-asignación para mejorar la planificación de servicios de salud, incorporando impedancia y rutas de red. El modelo p-mediana ha sido utilizado para minimizar distancias agregadas hacia centros de atención [@murad2021], mientras enfoques combinados de decisión multicriterio y p-mediana han permitido evaluar alternativas de localización [@murad2024]. Pan et al. [@pan2023] emplearon optimización en dos pasos para estudiar cambios de accesibilidad al agregar hospitales.

La presente investigación no ejecutará una optimización que determine de manera automática la ubicación oficial de un nuevo establecimiento. Usará los modelos de asignación y los indicadores de red para comparar escenarios explícitos. Toda ubicación candidata deberá provenir de un archivo de escenarios aprobado, y los resultados se presentarán como simulaciones, no como decisiones institucionales.

## 2.4. Análisis de decisión multicriterio y AHP

Las decisiones de planificación sanitaria involucran criterios que pueden tener escalas y direcciones distintas. El MCDA ofrece un marco para estructurar estos criterios y transparentar la combinación de resultados [@frazao2018]. Aroge et al. [@aroge2023] combinaron GIS, MCDA y AHP para seleccionar ubicaciones de atención primaria. Tripathi et al. [@tripathi2022] compararon AHP y fuzzy AHP en selección de sitios hospitalarios, y Zandi et al. [@zandi2024] aplicaron evaluación multicriterio espacial para idoneidad hospitalaria.

AHP será empleado para obtener pesos de criterios a partir de comparaciones pareadas de expertos. La matriz deberá cumplir reciprocidad y su razón de consistencia deberá calcularse y reportarse. Cuando la consistencia no sea aceptable según el protocolo aprobado, se solicitará al experto revisar la matriz; no se corregirán valores automáticamente.

## 2.5. Planificación adaptativa y análisis de escenarios

Los sistemas sanitarios pueden requerir adaptación ante cambios demográficos, cierres temporales, variación de accesibilidad o incorporación de nuevos servicios. Balsa-Barreiro et al. [@balsa2025] estudiaron accesibilidad por tiempo de viaje y soluciones de planificación espacial adaptativa. Este enfoque respalda el diseño de escenarios de esta tesis: situación actual, reducción funcional de un establecimiento y adición o reubicación de un punto de atención.

Los escenarios se compararán mediante métricas comunes, entre ellas cobertura poblacional dentro de un umbral de viaje, tiempo promedio ponderado por población, población no cubierta y variación del Índice de Sostenibilidad Territorial. Los umbrales no deben inventarse; deben provenir de norma, literatura o acuerdo experto documentado.

## 2.6. Contexto institucional y fuentes peruanas

La categorización de establecimientos del sector salud permite delimitar los puestos de salud y su nivel de atención [@minsa_categoria]. RENIPRESS constituye la fuente principal para identificar establecimientos registrados y atributos institucionales [@susalud_renipress]. GeoMINSA permitirá contrastar ubicaciones y redes [@minsa_geomin]. La información censal y de centros poblados del INEI se empleará para representar demanda y características demográficas [@inei2018]. El diagnóstico de brechas del sector salud contextualiza la necesidad de analizar infraestructura y acceso [@minsa_brechas2023], mientras el Plan Operativo Institucional de la Red de Salud Puno aporta contexto regional [@redsaludpuno2024].

Estas fuentes poseen finalidades, fechas y niveles de actualización diferentes. Por ello, el sistema debe registrar procedencia, fecha de corte y discrepancias. Cuando dos fuentes difieran en coordenadas o atributos, el dato no debe reemplazarse sin evidencia; debe conservarse un registro de conciliación.

## 2.7. Brecha de investigación

La revisión evidencia métodos maduros para medir accesibilidad, combinar criterios y simular localizaciones; sin embargo, no se ha identificado en el material revisado una herramienta aplicada a Pichacani que integre establecimientos rurales, centros poblados, red vial, indicadores de vulnerabilidad, pesos validados y escenarios reproducibles en un sistema local. La contribución de la tesis consiste en adaptar e integrar estos componentes en un Índice de Sostenibilidad Territorial y un prototipo orientado al apoyo de decisiones.

**Regla de control:** antes de la versión final, actualizar la búsqueda en el Repositorio Institucional de la UNA Puno y añadir únicamente tesis verificadas con autor, año, título, escuela y enlace oficial. No afirmar ausencia total de trabajos similares sin registrar estrategia y fecha de búsqueda.

---

# III. MATERIALES Y MÉTODOS

## 3.1. Lugar de estudio

La investigación se desarrollará en el distrito de Pichacani, provincia y departamento de Puno, con énfasis en los puestos de salud rurales vinculados al ámbito de la Microred Laraqueri. El procesamiento se realizará principalmente en gabinete mediante infraestructura informática local. Las visitas de validación territorial, cuando correspondan, deberán documentarse mediante fecha, propósito, participante y ficha de observación, sin recolectar información clínica de pacientes.

Codex debe generar la **Figura 1. Ubicación del distrito de Pichacani y ámbito de estudio**, usando límites oficiales disponibles localmente. El mapa debe incluir norte, escala, sistema de coordenadas, fuente, fecha de corte y autoría. No usar un polígono obtenido de una fuente no documentada.

## 3.2. Enfoque, tipo, nivel y diseño

La investigación es aplicada porque desarrolla una herramienta tecnológica para un problema de planificación territorial. Tiene enfoque cuantitativo porque procesa población, tiempos de viaje, cobertura, indicadores normalizados y pesos. El diseño es no experimental, dado que no se manipulan condiciones reales de prestación sanitaria. El alcance es descriptivo-propositivo: caracteriza la configuración territorial, construye un modelo y evalúa un prototipo y escenarios.

La unidad principal de análisis es cada puesto de salud rural incluido en el ámbito definido. Las unidades complementarias son los centros poblados, unidades demográficas, segmentos viales y áreas de influencia utilizadas para calcular indicadores.

## 3.3. Población y muestra

### 3.3.1. Unidades territoriales

Se aplicará un **censo** de todos los puestos de salud rurales y centros poblados que cumplan los criterios de inclusión dentro del polígono del estudio y tengan datos verificables. No se calculará una muestra probabilística de establecimientos, porque el objetivo es evaluar el conjunto completo del ámbito delimitado.

Criterios de inclusión de establecimientos:

1. registro verificable en RENIPRESS o fuente oficial equivalente;
2. localización dentro del ámbito de estudio;
3. pertenencia al primer nivel de atención y carácter rural según la delimitación adoptada;
4. coordenadas verificables o corregibles mediante evidencia documentada.

Criterios de exclusión:

1. establecimientos duplicados sin posibilidad de conciliación;
2. registros sin ubicación verificable luego del proceso de control de calidad;
3. establecimientos fuera del ámbito geográfico definido;
4. registros cuya situación institucional no pueda determinarse con la fecha de corte.

### 3.3.2. Expertos

La selección de expertos será no probabilística e intencional. Se buscará un mínimo de cinco participantes con experiencia en al menos uno de estos dominios: gestión del primer nivel, planificación sanitaria, estadística o información de salud, análisis territorial/SIG o Ingeniería de Sistemas. El número final, perfil, criterios de inclusión y posibles retiros deben reportarse de forma transparente.

### 3.3.3. Fórmula de muestra revisada y decisión de no aplicación

El material metodológico proporcionado incluye la fórmula para población finita:

$$
n=\frac{N Z^2 p q}{e^2(N-1)+Z^2pq}
$$

Esta fórmula **no se aplicará a los puestos de salud ni a los centros poblados**, porque se realizará un censo del ámbito. Tampoco se aplicará a los expertos, debido a que la selección es intencional por competencia y no pretende inferencia probabilística a una población de expertos. Codex debe conservar esta justificación y no calcular una muestra ficticia.

## 3.4. Materiales, equipos y tecnologías

| Categoría | Recurso | Especificación que debe registrarse | Uso |
|---|---|---|---|
| Equipo principal | Computadora personal del investigador | modelo, procesador, memoria RAM, almacenamiento y sistema operativo reales | ETL, modelamiento, desarrollo y redacción |
| Base de datos | PostgreSQL con PostGIS | versiones instaladas | datos alfanuméricos y geográficos |
| Análisis | Python | versión y archivo de dependencias bloqueadas | ETL, indicadores, AHP y escenarios |
| SIG | QGIS | versión instalada | verificación cartográfica y análisis manual |
| Backend | Django y Django REST Framework | versiones bloqueadas | API local y lógica de negocio |
| Frontend | React, TypeScript y Leaflet | versiones bloqueadas | interfaz cartográfica local |
| Contenedores | Docker / Docker Compose | versiones instaladas | reproducibilidad local |
| Documentación | Pandoc y plantilla DOCX oficial | versiones y hash de plantilla | generación del borrador |

Codex debe reemplazar “versión instalada” y las especificaciones del equipo con valores detectados y verificados. No usar marcas o modelos inventados.

## 3.5. Fuentes de datos

| Fuente | Contenido previsto | Uso | Control obligatorio |
|---|---|---|---|
| RENIPRESS | establecimientos, categoría, red, microred, estado y atributos disponibles | catálogo oficial de establecimientos | fecha de consulta, URL, checksum y duplicados |
| GeoMINSA | ubicación y visualización oficial | contraste de coordenadas | registrar discrepancias |
| INEI | centros poblados, población e indicadores demográficos disponibles | demanda y vulnerabilidad | año censal y cobertura espacial |
| Red de Salud Puno / DIRESA | organización y documentos de gestión | contexto y validación institucional | versión y fecha del documento |
| OpenStreetMap exportado localmente | red vial y atributos disponibles | cálculo de rutas | fecha de descarga, licencia y conectividad del grafo |
| Modelos de elevación, si se aprueban | elevación y pendiente | análisis complementario | fuente, resolución y licencia |

## 3.6. Variables y operacionalización

### 3.6.1. Variable independiente

**Sistema de soporte a decisiones geoespacial multicriterio.** Se operacionaliza mediante integración de datos, motor multicriterio, visualización, análisis de escenarios, trazabilidad y exportación.

### 3.6.2. Variable dependiente

**Sostenibilidad territorial de puestos de salud rurales.** Se operacionaliza como un índice continuo de 0 a 100 construido con cinco dimensiones. El índice expresa pertinencia territorial relativa bajo los datos, criterios y pesos declarados; no representa autorización administrativa.

| Dimensión | Indicadores mínimos | Dirección favorable | Fuente |
|---|---|---|---|
| Demanda poblacional (D) | población asignada o dentro del área de influencia; tendencia demográfica solo si existen series comparables | mayor es favorable | INEI y asignación espacial |
| Accesibilidad geográfica (A) | tiempo promedio ponderado; percentil 90 de tiempo; proximidad a red vial si está justificada | menor tiempo es favorable | red vial local y análisis de rutas |
| Cobertura territorial (C) | porcentaje de población dentro del umbral aprobado; centros poblados cubiertos | mayor es favorable | población y rutas |
| Singularidad territorial (R) | proporción de población cubierta exclusivamente por el establecimiento; inversa de superposición | mayor singularidad es favorable | áreas de servicio y establecimientos |
| Vulnerabilidad poblacional (V) | subindicadores oficiales disponibles y validados | mayor vulnerabilidad aumenta la pertinencia territorial | INEI y fuentes oficiales |

Se usa la etiqueta **singularidad territorial** en la operacionalización para evitar interpretar que “más redundancia” es favorable. En la fórmula se conserva la letra `R` por continuidad con el proyecto, pero su valor normalizado representa **baja redundancia o cobertura única**.

## 3.7. Procedimiento por objetivos específicos

### OE1. Caracterizar la distribución territorial

1. inventariar archivos y registrar metadatos;
2. importar establecimientos, centros poblados, población y vías;
3. validar tipos, dominios, identificadores y geometrías;
4. conciliar coordenadas entre fuentes;
5. proyectar temporalmente a un CRS métrico verificado para el ámbito;
6. construir el grafo vial;
7. asignar centros poblados a establecimientos por tiempo mínimo de viaje o criterio aprobado;
8. generar mapas y estadística descriptiva.

### OE2. Definir criterios e indicadores

1. extraer criterios de literatura, normativa y disponibilidad real de datos;
2. redactar definición conceptual, operacional y dirección de cada indicador;
3. someter criterios e indicadores a juicio de expertos;
4. calcular validez de contenido;
5. registrar cambios y versión final del modelo.

### OE3. Diseñar y calcular el IST

1. preparar matrices de comparación pareada;
2. calcular pesos y consistencia AHP;
3. calcular indicadores brutos;
4. normalizar indicadores;
5. agregar subindicadores por dimensión;
6. calcular IST;
7. ejecutar análisis de sensibilidad;
8. generar ranking y mapa.

### OE4. Implementar y validar el prototipo

1. diseñar base de datos y API;
2. implementar mapa, filtros, detalle de establecimientos, pesos y escenarios;
3. generar exportaciones reproducibles;
4. realizar pruebas unitarias, integración, geoespaciales y de interfaz;
5. validar utilidad y claridad con expertos o usuarios definidos;
6. documentar limitaciones.

## 3.8. Fórmulas guía de coherencia metodológica

Estas expresiones provienen del material metodológico proporcionado y se usan como **guías de verificación estructural**, no como operaciones estadísticas.

### 3.8.1. Título

$$
T_p=[(1\rightarrow2)+p+l+t]k
$$

Aplicación:

- `1`: sistema de soporte a decisiones geoespacial multicriterio;
- `2`: evaluación de sostenibilidad territorial;
- `p`: puestos de salud rurales;
- `l`: Pichacani, Puno;
- `t`: 2026;
- `k`: conectores necesarios.

### 3.8.2. Problema general

$$
P_g=[i(1\rightarrow2)+p+l+t]k
$$

La incógnita `i` se expresa mediante “¿Cómo evaluar...?”.

### 3.8.3. Objetivo general

$$
O_g=[v(1\rightarrow2)+p+l+t]k
$$

El verbo `v` es “desarrollar”.

### 3.8.4. Hipótesis general

$$
H_g=[c(1\rightarrow2)+p+l+t]k
$$

La proposición debe ser medible y coherente con los datos y métodos. No afirmar “mejora significativa” sin una prueba y comparador definidos.

### 3.8.5. Correspondencia de problemas, objetivos e hipótesis específicas

Como guía de consistencia estructural para cada componente `i`:

$$
P_{e_i}=i(2.i+p)k
$$

$$
O_{e_i}=v(2.i+p)k
$$

$$
H_{e_i}=c(2.i+p)k
$$

Estas expresiones no obligan a tratar cada indicador como un objetivo independiente. En esta tesis se mantienen cuatro objetivos porque representan las cuatro etapas verificables del trabajo: caracterización, definición de criterios, modelamiento e implementación/validación.

## 3.9. Ponderación AHP

Para `n` criterios se construye la matriz recíproca:

$$
A=[a_{ij}],\qquad a_{ji}=\frac{1}{a_{ij}},\qquad a_{ii}=1
$$

Los pesos se calcularán por media geométrica:

$$
g_i=\left(\prod_{j=1}^{n}a_{ij}\right)^{1/n}
$$

$$
w_i=\frac{g_i}{\sum_{k=1}^{n}g_k}
$$

La suma debe cumplir:

$$
\sum_{i=1}^{n}w_i=1
$$

La consistencia se calcula mediante:

$$
\lambda_{\max}=\frac{1}{n}\sum_{i=1}^{n}\frac{(Aw)_i}{w_i}
$$

$$
CI=\frac{\lambda_{\max}-n}{n-1}
$$

$$
CR=\frac{CI}{RI_n}
$$

Valores de referencia previstos para `RI_n`:

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| RI | 0.00 | 0.00 | 0.58 | 0.90 | 1.12 | 1.24 | 1.32 | 1.41 | 1.45 | 1.49 |

Para cinco criterios se prevé `RI_5=1.12`. Codex debe verificar esta tabla contra la fuente AHP finalmente citada y registrar la versión utilizada. No aceptar una matriz inconsistente ni modificarla automáticamente.

Si existen varios expertos, se agregan sus juicios mediante media geométrica por elemento:

$$
\bar a_{ij}=\left(\prod_{h=1}^{H}a_{ij}^{(h)}\right)^{1/H}
$$

## 3.10. Normalización de indicadores

Para un indicador de beneficio:

$$
x'_{ij}=100\frac{x_{ij}-\min(x_j)}{\max(x_j)-\min(x_j)}
$$

Para un indicador de costo:

$$
x'_{ij}=100\frac{\max(x_j)-x_{ij}}{\max(x_j)-\min(x_j)}
$$

Si `max(x_j)=min(x_j)`, el indicador no discrimina. El sistema debe detener el cálculo de ese indicador, marcarlo como no informativo y requerir una decisión metodológica; no asignar un valor arbitrario.

## 3.11. Indicadores territoriales

### 3.11.1. Demanda poblacional

Sea `J_i` el conjunto de centros poblados asignados al establecimiento `i`:

$$
P_i=\sum_{j\in J_i}P_j
$$

El puntaje `D_i` se obtiene normalizando `P_i` como criterio de beneficio. Si existen datos demográficos comparables en dos fechas, la tasa media anual puede calcularse como análisis complementario:

$$
g_j=\left[\left(\frac{P_{j,t_2}}{P_{j,t_1}}\right)^{\frac{1}{t_2-t_1}}-1\right]100
$$

No usar esta tasa si los límites, definiciones o unidades no son comparables.

### 3.11.2. Accesibilidad geográfica

Tiempo promedio ponderado por población:

$$
\bar t_i=\frac{\sum_{j\in J_i}P_jt_{ij}}{\sum_{j\in J_i}P_j}
$$

`A_i` se obtiene normalizando `\bar t_i` como criterio de costo. También se reportará el percentil 90 de los tiempos asignados, pero no se mezclará con el promedio sin un peso explícito.

El tiempo de cada arista vial es:

$$
t_e=\frac{L_e}{v_e}\times60
$$

con `L_e` en kilómetros, `v_e` en kilómetros por hora y `t_e` en minutos. Toda velocidad debe provenir de un parámetro documentado y someterse a sensibilidad. No usar velocidades ocultas.

### 3.11.3. Cobertura territorial

Para un umbral de tiempo `T` validado:

$$
C_i=100\frac{\sum_{j\in J_i}P_j\,\mathbb{I}(t_{ij}\leq T)}{\sum_{j\in J_i}P_j}
$$

Cobertura distrital del escenario `s`:

$$
C_s^{dist}=100\frac{\sum_jP_j\,\mathbb{I}(\min_i t_{ij}^{(s)}\leq T)}{\sum_jP_j}
$$

### 3.11.4. Singularidad o baja redundancia

Proporción de población cubierta por `i` que también está cubierta por al menos otro establecimiento:

$$
O_i=\frac{\sum_jP_j\,\mathbb{I}(i\text{ cubre }j\land\exists k\neq i:k\text{ cubre }j)}{\sum_jP_j\,\mathbb{I}(i\text{ cubre }j)}
$$

Puntaje de singularidad:

$$
R_i=100(1-O_i)
$$

Si el denominador es cero, el valor es indefinido y el sistema debe marcar el caso para revisión.

### 3.11.5. Vulnerabilidad

Si existen `m` subindicadores oficiales normalizados:

$$
V_i=\sum_{r=1}^{m}\alpha_rv'_{ir},\qquad \sum_{r=1}^{m}\alpha_r=1
$$

Los subindicadores y pesos `\alpha_r` deben quedar en `config/criteria.yml`. Cuando un subindicador no esté disponible para todo el ámbito, no se imputará sin un método aprobado.

## 3.12. Índice de Sostenibilidad Territorial

$$
IST_i=w_DD_i+w_AA_i+w_CC_i+w_RR_i+w_VV_i
$$

sujeto a:

$$
w_D+w_A+w_C+w_R+w_V=1,\qquad 0\leq IST_i\leq100
$$

El resultado principal será el valor continuo y el ranking. Si se requieren categorías, estas deben generarse mediante un método documentado —por ejemplo, cuantiles o cortes naturales— y se deben denominar **niveles relativos dentro del ámbito**, no umbrales normativos universales.

## 3.13. Análisis de escenarios

Escenarios mínimos:

- `S0`: red actual;
- `S1(-i)`: reducción funcional o retiro simulado de un establecimiento, uno por ejecución;
- `S2(+c)`: incorporación de una ubicación candidata;
- `S3(reloc i→c)`: reubicación simulada, solo si la ubicación candidata fue proporcionada y aprobada.

Métricas:

$$
\bar t_s^{dist}=\frac{\sum_jP_j\min_i(t_{ij}^{(s)})}{\sum_jP_j}
$$

$$
P_s^{no\ cub}=\sum_jP_j\,\mathbb{I}(\min_i t_{ij}^{(s)}>T)
$$

$$
\Delta C_s=C_s^{dist}-C_0^{dist}
$$

$$
\Delta \bar t_s=\bar t_s^{dist}-\bar t_0^{dist}
$$

Cada escenario debe registrar parámetros, fecha, usuario, instalaciones activas, candidatos y hash de resultados.

## 3.14. Validez de contenido mediante V de Aiken

Para cada ítem:

$$
V=\frac{\sum_{h=1}^{n}s_h}{n(c-1)},\qquad s_h=r_h-l_0
$$

Donde `r_h` es la calificación del experto, `l_0` es el valor mínimo de la escala, `c` es el número de categorías y `n` es el número de expertos. Para una escala de 1 a 5, `l_0=1` y `c=5`.

El criterio de aceptación debe definirse antes de analizar resultados y quedar aprobado en el protocolo. Codex debe reportar `V` por ítem, por dimensión y el número de expertos; no debe declarar validez solo con el promedio Likert.

## 3.15. Análisis de sensibilidad

Se variará cada peso dentro de un rango predefinido y se renormalizarán los demás:

$$
w'_k=w_k+\delta
$$

$$
w'_j=w_j\frac{1-w'_k}{1-w_k},\qquad j\neq k
$$

Se calcularán cambios de posición, correlación del ranking y estabilidad de los primeros y últimos lugares. El rango `\delta` debe configurarse y justificarse; no se debe ocultar el efecto de pesos alternativos.

## 3.16. Validación del prototipo

La evaluación del prototipo considerará:

- corrección funcional;
- trazabilidad de datos;
- claridad de mapas y leyendas;
- comprensión del IST;
- facilidad de uso;
- utilidad para comparar escenarios;
- exportación de resultados.

La ficha usará escala de 1 a 5 y preguntas abiertas. Los resultados se analizarán descriptivamente. No se inferirá representatividad poblacional de una muestra intencional pequeña.

## 3.17. Análisis estadístico y geoespacial

Se aplicarán:

1. frecuencias, porcentajes, media, mediana, rango y percentiles;
2. normalización min-max;
3. AHP y razón de consistencia;
4. V de Aiken;
5. análisis de sensibilidad;
6. comparación de escenarios;
7. análisis de proximidad y rutas;
8. áreas de servicio y superposición;
9. mapas coropléticos o graduados, evitando clases engañosas.

No aplicar t de Student, ANOVA, chi-cuadrado o pruebas de hipótesis por inercia. Solo incorporarlas si una hipótesis y diseño posterior justifican su uso.

## 3.18. Consideraciones éticas

- No recolectar datos de pacientes.
- No incluir información que identifique a personas.
- Solicitar consentimiento informado a expertos.
- Proteger sus respuestas y publicar resultados agregados.
- Registrar licencias y atribución de datos.
- Solicitar evaluación ética institucional si el asesor o la normativa lo requieren.
- No presentar el ranking como orden de cierre ni como mandato administrativo.

---

# IV. RESULTADOS Y DISCUSIÓN

## 4.0. Regla absoluta

Esta sección no debe contener números simulados. Codex la completará únicamente a partir de archivos generados por la ejecución reproducible.

## 4.1. Calidad y consolidación de datos

Texto final a generar:

```text
Se integraron {{RESULTADO: número de fuentes}} fuentes y se procesaron {{RESULTADO: número de registros}} registros. Después del control de calidad se conservaron {{RESULTADO}} establecimientos, {{RESULTADO}} centros poblados y {{RESULTADO}} segmentos viales. Las principales incidencias fueron {{RESULTADO: incidencias documentadas}}.
```

Artefactos obligatorios:

- Tabla: resumen de fuentes y fecha de corte.
- Tabla: reglas de calidad y cantidad de incidencias.
- Figura: mapa de establecimientos y centros poblados.
- Reporte: `outputs/reports/data_quality.json`.

## 4.2. Caracterización territorial — OE1

Reportar:

- número de establecimientos incluidos;
- población total considerada;
- distribución de centros poblados;
- conectividad del grafo vial;
- tiempos de viaje descriptivos;
- áreas sin ruta calculable.

Comparar los hallazgos con Carrasco-Escobar et al. [@carrasco2020], Verma y Dash [@verma2020], Bhangdia et al. [@bhangdia2022] y Wood et al. [@wood2023], sin afirmar equivalencia entre contextos.

## 4.3. Criterios, indicadores y pesos — OE2

Incluir:

- perfil de expertos;
- V de Aiken por ítem;
- matriz agregada AHP;
- pesos finales;
- `CI` y `CR`;
- criterios revisados o excluidos.

Tabla obligatoria:

| Criterio | Peso | V de Aiken | Dirección | Fuente de datos | Observación |
|---|---:|---:|---|---|---|
| Demanda | `{{AUTO}}` | `{{AUTO}}` | beneficio | `{{AUTO}}` | `{{AUTO}}` |
| Accesibilidad | `{{AUTO}}` | `{{AUTO}}` | costo transformado | `{{AUTO}}` | `{{AUTO}}` |
| Cobertura | `{{AUTO}}` | `{{AUTO}}` | beneficio | `{{AUTO}}` | `{{AUTO}}` |
| Singularidad | `{{AUTO}}` | `{{AUTO}}` | beneficio | `{{AUTO}}` | `{{AUTO}}` |
| Vulnerabilidad | `{{AUTO}}` | `{{AUTO}}` | beneficio | `{{AUTO}}` | `{{AUTO}}` |

Discutir con Frazão et al. [@frazao2018], Aroge et al. [@aroge2023], Tripathi et al. [@tripathi2022] y Zandi et al. [@zandi2024].

## 4.4. Índice de Sostenibilidad Territorial — OE3

Presentar:

- indicadores brutos y normalizados;
- IST por establecimiento;
- ranking;
- mapa;
- análisis de sensibilidad;
- limitaciones por datos faltantes.

No usar lenguaje como “posta inútil” o “debe eliminarse”. Emplear “menor/ mayor sostenibilidad territorial relativa bajo el modelo” y explicar los factores del puntaje.

## 4.5. Prototipo local — OE4

Documentar:

- arquitectura;
- módulos implementados;
- flujo de usuario;
- capturas de pantalla;
- pruebas funcionales;
- rendimiento local;
- exportaciones.

Figuras previstas:

1. arquitectura lógica;
2. modelo de datos;
3. mapa principal;
4. detalle de establecimiento;
5. panel de pesos;
6. comparador de escenarios;
7. exportación de reporte.

## 4.6. Escenarios

Para cada escenario presentar la misma tabla:

| Escenario | Cobertura (%) | Tiempo medio (min) | P90 (min) | Población no cubierta | Variación frente a S0 |
|---|---:|---:|---:|---:|---:|
| S0 | `{{AUTO}}` | `{{AUTO}}` | `{{AUTO}}` | `{{AUTO}}` | 0 |
| S1 | `{{AUTO}}` | `{{AUTO}}` | `{{AUTO}}` | `{{AUTO}}` | `{{AUTO}}` |
| S2 | `{{AUTO}}` | `{{AUTO}}` | `{{AUTO}}` | `{{AUTO}}` | `{{AUTO}}` |

Discutir con Polo et al. [@polo2015], Murad et al. [@murad2021; @murad2024], Pan et al. [@pan2023] y Balsa-Barreiro et al. [@balsa2025].

## 4.7. Validación y limitaciones

Reportar resultados reales de utilidad, claridad, facilidad de uso y comprensión. Incluir comentarios cualitativos anonimizados. Discutir como limitaciones:

- actualización y granularidad de datos censales;
- incompletitud o conectividad de la red vial;
- velocidades de viaje parametrizadas;
- número de expertos;
- ausencia de información operativa o clínica;
- alcance restringido a Pichacani.

---

# V. CONCLUSIONES

En modo borrador mantener cuatro marcadores. En modo final redactar una conclusión cualitativa por objetivo, sin citas y sin repetir tablas completas.

1. **OE1:** `{{RESULTADO: conclusión sobre la caracterización territorial y la calidad/disponibilidad de datos}}`.
2. **OE2:** `{{RESULTADO: conclusión sobre dimensiones, criterios, validez y pesos}}`.
3. **OE3:** `{{RESULTADO: conclusión sobre el IST, capacidad de discriminación y estabilidad}}`.
4. **OE4:** `{{RESULTADO: conclusión sobre implementación, validación y utilidad del prototipo}}`.

No añadir una quinta conclusión genérica que no corresponda a un objetivo, salvo requerimiento explícito del jurado.

---

# VI. RECOMENDACIONES

Las recomendaciones finales deben derivarse de las limitaciones y resultados. Se proponen como estructura, no como afirmaciones definitivas:

1. actualizar periódicamente la base territorial con nuevas versiones oficiales;
2. validar tiempos de viaje mediante observación o registros de campo en rutas críticas;
3. incorporar en trabajos futuros capacidad operativa, cartera de servicios y disponibilidad de personal, siempre que exista acceso autorizado a datos;
4. evaluar la transferibilidad del modelo a otros distritos rurales de Puno;
5. ampliar la evaluación con usuarios institucionales y documentar decisiones reales apoyadas por el sistema;
6. evitar interpretar el IST como decisión automática de cierre o inversión.

Codex debe adaptar estas recomendaciones a los hallazgos y eliminar las que no estén sustentadas.

---

# VII. REFERENCIAS

Codex debe generar esta sección desde `references.bib` con APA 7 en español. Los citekeys usados en el texto deben ser exactamente los siguientes:

| Citekey | Fuente |
|---|---|
| `aroge2023` | Aroge et al. (2023) |
| `balsa2025` | Balsa-Barreiro et al. (2025) |
| `bhangdia2022` | Bhangdia et al. (2022) |
| `carrasco2020` | Carrasco-Escobar et al. (2020) |
| `franco2021` | Franco et al. (2021) |
| `frazao2018` | Frazão et al. (2018) |
| `garnelo2020` | Garnelo et al. (2020) |
| `houghton2023` | Houghton et al. (2023) |
| `inei2018` | Instituto Nacional de Estadística e Informática (2018) |
| `lechowski2021` | Lechowski y Jasion (2021) |
| `minsa_categoria` | Ministerio de Salud, categorías de establecimientos |
| `minsa_geomin` | Ministerio de Salud, GeoMINSA |
| `minsa_brechas2023` | Ministerio de Salud, diagnóstico de brechas |
| `murad2021` | Murad et al. (2021) |
| `murad2024` | Murad et al. (2024) |
| `pan2023` | Pan et al. (2023) |
| `polo2015` | Polo et al. (2015) |
| `redsaludpuno2024` | Red de Salud Puno (2024) |
| `susalud_renipress` | Superintendencia Nacional de Salud, RENIPRESS |
| `tripathi2022` | Tripathi et al. (2022) |
| `verma2020` | Verma y Dash (2020) |
| `wood2023` | Wood et al. (2023) |
| `zandi2024` | Zandi et al. (2024) |

Lista base a registrar:

1. Aroge, S. K., Emmanuel, A. B., Babatunde, A. N., y Sola, A. J. (2023). Combination of GIS, MCDA and AHP for the selection of most suitable location for primary health care facilities. *American Journal of Geospatial Technology, 2*(1), 1–6. https://doi.org/10.54536/ajgt.v2i1.1820
2. Balsa-Barreiro, J., Batista, S. F. A., Hannoun, G. J., y Menendez, M. (2025). Travel-time accessibility and adaptive spatial planning solutions for the healthcare system. *npj Health Systems, 2*(1). https://doi.org/10.1038/s44401-025-00028-1
3. Bhangdia, K. P., Iyer, H. S., Joseph, J. P., Dorne, R. L., Mukherjee, J., y Fadelu, T. (2022). Comparing absolute and relative distance and time travel measures of geographic access to healthcare facilities in rural Haiti. *BMJ Open, 12*(5). https://doi.org/10.1136/bmjopen-2021-056123
4. Carrasco-Escobar, G., Manrique, E., Tello-Lizarraga, K., y Miranda, J. J. (2020). Travel time to health facilities as a marker of geographical accessibility across heterogeneous land coverage in Peru. *Frontiers in Public Health, 8*. https://doi.org/10.3389/fpubh.2020.00498
5. Franco, C. M., Lima, J. G., y Giovanella, L. (2021). Primary healthcare in rural areas: Access, organization, and health workforce in an integrative literature review. *Cadernos de Saúde Pública, 37*(7). https://doi.org/10.1590/0102-311X00310520
6. Frazão, T. D. C., Camilo, D. G. G., Cabral, E. L. S., y Souza, R. P. (2018). Multicriteria decision analysis in health care: A systematic review of the main characteristics and methodological steps. *BMC Medical Informatics and Decision Making, 18*(1). https://doi.org/10.1186/s12911-018-0663-1
7. Garnelo, L., Parente, R. C. P., Puchiarelli, M. L. R., Correia, P. C., Torres, M. V., y Herkrath, F. J. (2020). Barriers to access and organization of primary health care services for rural riverside populations in the Amazon. *International Journal for Equity in Health, 19*(1). https://doi.org/10.1186/s12939-020-01171-x
8. Houghton, N., Báscolo, E., Cohen, R. R., Vilcarromero, N. L. C., González, H. R., Albrecht, D., Koller, T. S., y Fitzgerald, J. (2023). Identifying access barriers faced by rural and dispersed communities to better address their needs: Implications and lessons learned for rural proofing for health in the Americas and beyond. *Rural and Remote Health, 23*(1). https://doi.org/10.22605/RRH7822
9. Instituto Nacional de Estadística e Informática. (2018). *Perú: Resultados definitivos de los Censos Nacionales 2017*. https://www.inei.gob.pe/media/MenuRecursivo/publicaciones_digitales/Est/Lib1544/
10. Lechowski, Ł., y Jasion, A. (2021). Spatial accessibility of primary health care in rural areas in Poland. *International Journal of Environmental Research and Public Health, 18*(17). https://doi.org/10.3390/ijerph18179282
11. Ministerio de Salud. (s. f.-a). *Categorías de establecimientos del sector salud: NT N.° 021-MINSA/DGSP V.01*. Recuperado el 31 de mayo de 2026, de https://www.gob.pe/institucion/minsa/informes-publicaciones/352897-categorias-de-establecimientos-del-sector-salud-nt-n-021-minsa-dgsp-v-01
12. Ministerio de Salud. (s. f.-b). *GeoMINSA*. Recuperado el 31 de mayo de 2026, de https://geo.minsa.gob.pe/
13. Ministerio de Salud. (2023). *Diagnóstico de brechas de infraestructura o acceso a servicios del sector salud 2024–2026*. https://www.minsa.gob.pe/Recursos/OTRANS/08Proyectos/2022/Diagnostico-Infraestructura-Sector-Salud-2024-2026.pdf
14. Murad, A., Faruque, F., Naji, A., y Tiwari, A. (2021). Using the location-allocation p-median model for optimising locations for health care centres in the city of Jeddah City, Saudi Arabia. *Geospatial Health, 16*(2). https://doi.org/10.4081/gh.2021.1002
15. Murad, A., Faruque, F., Naji, A., Tiwari, A., Qurnfulah, E., Rahman, M., y Dewan, A. (2024). Optimizing health service location in a highly urbanized city: Multi criteria decision making and p-median problem models for public hospitals in Jeddah City, KSA. *PLOS ONE, 19*(1). https://doi.org/10.1371/journal.pone.0294819
16. Pan, J., Deng, Y., Yang, Y., y Zhang, Y. (2023). Location-allocation modelling for rational health planning: Applying a two-step optimization approach to evaluate the spatial accessibility improvement of newly added tertiary hospitals in a metropolitan city of China. *Social Science & Medicine, 338*, 116296. https://doi.org/10.1016/j.socscimed.2023.116296
17. Polo, G., Acosta, C. M., Ferreira, F., y Dias, R. A. (2015). Location-allocation and accessibility models for improving the spatial planning of public health services. *PLOS ONE, 10*(3), e0119190. https://doi.org/10.1371/journal.pone.0119190
18. Red de Salud Puno. (2024). *Plan Operativo Institucional Anual 2025 de la Red de Salud Puno*. https://www.reddesaludpuno.gob.pe/documentos/doc_gest/POI%202025%20-%20RED%20DE%20SALUD%20PUNO..pdf
19. Superintendencia Nacional de Salud. (s. f.). *Obtener información de las Instituciones Prestadoras de Servicios de Salud - RENIPRESS*. Recuperado el 31 de mayo de 2026, de https://www.gob.pe/10202-obtener-informacion-de-las-instituciones-prestadoras-de-servicios-de-salud-renipress
20. Tripathi, A. K., Agrawal, S., y Gupta, R. D. (2022). Comparison of GIS-based AHP and fuzzy AHP methods for hospital site selection: A case study for Prayagraj City, India. *GeoJournal, 87*(5), 3507–3528. https://doi.org/10.1007/s10708-021-10445-y
21. Verma, V. R., y Dash, U. (2020). Geographical accessibility and spatial coverage modelling of public health care network in rural and remote India. *PLOS ONE, 15*(10), e0239326. https://doi.org/10.1371/journal.pone.0239326
22. Wood, S. M., Alston, L., Beks, H., Mc Namara, K., Coffee, N. T., Clark, R. A., Wong Shee, A., y Versace, V. L. (2023). The application of spatial measures to analyse health service accessibility in Australia: A systematic review and recommendations for future practice. *BMC Health Services Research, 23*(1). https://doi.org/10.1186/s12913-023-09342-6
23. Zandi, I., Pahlavani, P., Bigdeli, B., Lotfata, A., Alesheikh, A. A., y Garau, C. (2024). GIS-enabled multi-criteria assessment for hospital site suitability: A case study of Tehran. *Sustainability, 16*(5), 2079. https://doi.org/10.3390/su16052079

**Control bibliográfico obligatorio:** verificar metadatos contra el PDF o DOI antes del cierre. En particular, confirmar año y edición de documentos institucionales, nombres con tildes, número de artículo y fecha de consulta. No modificar metadatos únicamente para que “se vean mejor”.

---

# ANEXOS

## ANEXO A. Matriz de consistencia

| Elemento | General | Específico 1 | Específico 2 | Específico 3 | Específico 4 |
|---|---|---|---|---|---|
| Problema | ¿Cómo evaluar la sostenibilidad territorial mediante el sistema propuesto? | ¿Cuál es la distribución territorial? | ¿Qué criterios e indicadores son pertinentes? | ¿Cómo calcular el IST? | ¿Cómo implementar y validar el prototipo? |
| Objetivo | Desarrollar el sistema | Caracterizar | Definir | Diseñar | Implementar y validar |
| Hipótesis/proposición | La integración geoespacial y multicriterio permite una evaluación estructurada y trazable | Los datos integrados permiten caracterizar | Los criterios validados operacionalizan la variable | El modelo permite calcular y ordenar el IST | El prototipo permite visualizar y comparar escenarios |
| Producto | Sistema y evaluación | Base territorial | Modelo de criterios | IST y sensibilidad | Prototipo y validación |

Codex debe ampliar esta matriz con variables, dimensiones, indicadores, técnicas e instrumentos.

## ANEXO B. Matriz de operacionalización

Generar desde `config/criteria.yml`; no mantener dos versiones manuales divergentes.

## ANEXO C. Diccionario de datos

Campos mínimos:

| Entidad | Campo | Tipo | Unidad/dominio | Nulos | Fuente | Regla de calidad |
|---|---|---|---|---|---|---|
| Establecimiento | id_renipress | texto | identificador | no | RENIPRESS | único |
| Establecimiento | nombre | texto | libre controlado | no | RENIPRESS | normalización de espacios |
| Establecimiento | categoría | texto | catálogo | no | MINSA | dominio validado |
| Establecimiento | geom | punto | CRS oficial | no | RENIPRESS/GeoMINSA | dentro del ámbito |
| Centro poblado | id_cp | texto | identificador | no | INEI | único |
| Centro poblado | población | entero | personas | sí controlado | INEI | no negativo y año registrado |
| Vía | longitud_m | decimal | metros | no | OSM/local | mayor que cero |
| Vía | velocidad_kmh | decimal | km/h | no | parámetro | rango documentado |
| Resultado | ist | decimal | 0–100 | no | modelo | rango válido |

## ANEXO D. Instrumento de juicio de expertos

Debe incluir consentimiento, perfil, instrucciones, escala 1–5, matriz AHP, evaluación de pertinencia/claridad/relevancia/viabilidad y observaciones. No recolectar datos personales innecesarios.

## ANEXO E. Reporte AHP

Incluir matrices individuales anonimizadas, matriz agregada, pesos, `lambda_max`, `CI`, `CR`, decisiones de revisión y versión final.

## ANEXO F. Cálculo de V de Aiken

Tabla por ítem con calificaciones, `s`, suma, `V` y decisión según protocolo.

## ANEXO G. Arquitectura y requisitos del sistema

Incluir arquitectura, modelo entidad-relación, endpoints, requisitos funcionales/no funcionales, casos de uso y pruebas.

## ANEXO H. Reproducibilidad

Incluir versiones, comandos, hashes, manifest, parámetros y procedimiento para ejecutar todo sin conexión.

---

# PARTE D. ESPECIFICACIÓN DEL SISTEMA LOCAL

## D.1. Arquitectura obligatoria

- **Base de datos:** PostgreSQL + PostGIS.
- **Backend:** Django + Django REST Framework.
- **Frontend:** React + TypeScript + Leaflet.
- **ETL y modelo:** Python con Pandas, GeoPandas, Shapely, NetworkX o pgRouting según la red importada.
- **Validación cartográfica:** QGIS.
- **Despliegue:** Docker Compose local.
- **Autenticación:** local, con roles `investigador`, `experto` y `consulta`; no implementar autenticación externa.

## D.2. Entidades mínimas

```text
DataSource
ImportBatch
HealthFacility
PopulationCenter
DemographicIndicator
RoadNode
RoadEdge
TravelMatrix
Criterion
CriterionSubindicator
Expert
PairwiseComparison
AHPResult
FacilityRawIndicator
FacilityNormalizedScore
FacilityIST
Scenario
ScenarioFacility
ScenarioMetric
PrototypeEvaluation
AuditLog
```

Cada resultado debe enlazarse con el lote de importación y versión de parámetros.

## D.3. Requisitos funcionales

| Código | Requisito |
|---|---|
| RF-01 | Importar archivos locales de establecimientos, centros poblados, población y vías. |
| RF-02 | Mostrar errores de calidad antes de confirmar una importación. |
| RF-03 | Visualizar establecimientos, centros poblados y vías en el mapa. |
| RF-04 | Configurar criterios, subindicadores, dirección y fuente. |
| RF-05 | Registrar comparaciones pareadas y calcular AHP/consistencia. |
| RF-06 | Calcular indicadores brutos y normalizados. |
| RF-07 | Calcular IST con versión de pesos y datos. |
| RF-08 | Mostrar ranking, desglose y explicación de cada puntaje. |
| RF-09 | Crear y ejecutar escenarios. |
| RF-10 | Comparar cobertura, tiempos y población no cubierta. |
| RF-11 | Exportar CSV, GeoJSON, PNG y reporte PDF/DOCX. |
| RF-12 | Registrar auditoría y manifest de cada ejecución. |

## D.4. Requisitos no funcionales

- ejecución sin Internet después de instalar dependencias y cargar datos;
- reproducibilidad mediante Docker y archivos de bloqueo;
- manejo explícito de CRS;
- validación de geometrías;
- accesibilidad de la interfaz y leyendas comprensibles;
- tiempo de respuesta documentado para el conjunto real;
- pruebas automatizadas;
- no exponer información sensible;
- logs sin datos personales;
- exportaciones con fecha, parámetros y fuente.

## D.5. API mínima

```text
GET    /api/facilities/
GET    /api/facilities/{id}/
GET    /api/population-centers/
GET    /api/criteria/
POST   /api/ahp/calculate/
POST   /api/ist/calculate/
GET    /api/ist/ranking/
POST   /api/scenarios/
POST   /api/scenarios/{id}/run/
GET    /api/scenarios/{id}/metrics/
GET    /api/exports/{run_id}/
```

## D.6. Archivos de configuración

Ejemplo de `config/criteria.yml`:

```yaml
model_version: "0.1.0"
score_range: [0, 100]
criteria:
  demand:
    code: D
    direction: benefit
    weight_source: ahp
  accessibility:
    code: A
    direction: cost
    weight_source: ahp
  coverage:
    code: C
    direction: benefit
    weight_source: ahp
  uniqueness:
    code: R
    direction: benefit
    weight_source: ahp
  vulnerability:
    code: V
    direction: benefit
    weight_source: ahp
thresholds:
  travel_time_minutes: "{{PENDIENTE: valor validado}}"
```

El sistema debe rechazar la ejecución si el umbral sigue siendo un texto pendiente.

## D.7. Pruebas obligatorias

### Unitarias

- reciprocidad de matriz AHP;
- suma de pesos igual a 1;
- cálculo conocido de `CI` y `CR`;
- normalización beneficio/costo;
- error en columna constante;
- rango del IST;
- V de Aiken;
- cobertura con conjunto sintético;
- singularidad con cobertura superpuesta;
- variación de escenarios.

### Integración

- importación a PostGIS;
- cálculo completo desde datos sintéticos;
- generación de exportaciones;
- API y base de datos;
- regeneración idéntica con mismos hashes.

### Geoespaciales

- geometrías válidas;
- puntos dentro del ámbito;
- distancia calculada en CRS métrico;
- grafo conectado o componentes reportados;
- rutas reproducibles.

### Documentales

- resumen ≤350 palabras;
- introducción ≤2 páginas;
- cuatro objetivos y cuatro conclusiones;
- citas con referencia;
- figuras y tablas numeradas;
- ausencia de marcadores en modo final;
- índice actualizado.

---

# PARTE E. ÍNDICES PREVISTOS DE FIGURAS Y TABLAS

## E.1. Figuras previstas

1. Ubicación del distrito de Pichacani y ámbito de estudio.
2. Flujo metodológico de la investigación.
3. Arquitectura del sistema local.
4. Modelo entidad-relación.
5. Distribución de puestos de salud y centros poblados.
6. Red vial y conectividad del grafo.
7. Tiempos de viaje hacia establecimientos.
8. Cobertura territorial en el escenario actual.
9. Pesos del modelo multicriterio.
10. Mapa del Índice de Sostenibilidad Territorial.
11. Análisis de sensibilidad del ranking.
12. Comparación cartográfica de escenarios.
13. Interfaz principal del prototipo.
14. Panel de detalle y explicación del IST.

## E.2. Tablas previstas

1. Matriz de correspondencia entre objetivos, hipótesis y productos.
2. Fuentes de datos y fechas de corte.
3. Operacionalización de variables.
4. Criterios, indicadores y dirección.
5. Materiales, equipos y software.
6. Reglas de calidad de datos.
7. Perfil de expertos.
8. V de Aiken por ítem.
9. Matriz AHP agregada y consistencia.
10. Pesos finales.
11. Caracterización de establecimientos y centros poblados.
12. Indicadores brutos.
13. Indicadores normalizados e IST.
14. Ranking y desglose.
15. Métricas de escenarios.
16. Resultados de validación del prototipo.
17. Casos de prueba del sistema.

Los índices definitivos deben generarse automáticamente y contener solo elementos existentes.

---

# PARTE F. LISTA DE VERIFICACIÓN PARA ENTREGA

## F.1. Contenido académico

- [ ] título idéntico en portada, aprobación, resumen e índices;
- [ ] autor y grado verificados;
- [ ] asesor y jurados verificados;
- [ ] área y tema consignados;
- [ ] resumen final de un párrafo y ≤350 palabras;
- [ ] abstract equivalente al resumen final;
- [ ] máximo cinco palabras clave en cada idioma;
- [ ] introducción de máximo dos páginas;
- [ ] revisión crítica organizada por objetivos;
- [ ] materiales y métodos reproducibles;
- [ ] resultados reales y trazables;
- [ ] discusión contrastada con literatura;
- [ ] cuatro conclusiones para cuatro objetivos;
- [ ] recomendaciones derivadas de resultados;
- [ ] referencias completas y coherentes;
- [ ] anexos identificados A, B, C...;
- [ ] no hay afirmaciones de cierre automático de establecimientos.

## F.2. Datos y modelo

- [ ] fecha de corte de cada fuente;
- [ ] checksum de archivos brutos;
- [ ] coordenadas y CRS validados;
- [ ] discrepancias documentadas;
- [ ] grafo vial validado;
- [ ] umbral de viaje justificado;
- [ ] criterios validados;
- [ ] razón de consistencia reportada;
- [ ] normalización reproducible;
- [ ] IST dentro de 0–100;
- [ ] análisis de sensibilidad ejecutado;
- [ ] escenarios versionados.

## F.3. Sistema

- [ ] instalación local documentada;
- [ ] Docker Compose funcional;
- [ ] migraciones reproducibles;
- [ ] pruebas unitarias e integración aprobadas;
- [ ] exportaciones con metadatos;
- [ ] interfaz sin dependencias remotas;
- [ ] auditoría y manifest generados;
- [ ] datos sensibles ausentes.

## F.4. Documento

- [ ] plantilla oficial aplicada;
- [ ] índice general actualizado;
- [ ] índice de figuras actualizado;
- [ ] índice de tablas actualizado;
- [ ] acrónimos definidos en primer uso;
- [ ] títulos de tablas arriba;
- [ ] títulos de figuras abajo;
- [ ] ecuaciones numeradas;
- [ ] referencias APA 7 en español;
- [ ] no quedan marcadores `{{PENDIENTE}}` o `{{RESULTADO}}`;
- [ ] PDF revisado visualmente página por página.

---

# NOTA FINAL PARA CODEX

Este archivo no autoriza completar hallazgos inexistentes. La prioridad es producir una investigación reproducible y defendible. Cuando una decisión metodológica no esté respaldada por la plantilla, por los datos o por el protocolo aprobado, Codex debe dejarla explícitamente pendiente y explicar qué evidencia falta. El sistema debe ser capaz de reconstruir cada tabla y figura del capítulo de resultados desde los datos locales y los parámetros versionados.
