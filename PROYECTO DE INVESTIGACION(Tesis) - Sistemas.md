**PROYECTO DE INVESTIGACIÓN** 

**Estudiante: Rendo Alfonte Tarqui**

1. **Título**

**Sistema de soporte a decisiones geoespacial multicriterio para evaluar la sostenibilidad territorial de puestos de salud rurales en Pichacani, Puno, 2026**

2. **Resumen del Proyecto de Tesis**

	El presente proyecto de investigación propone desarrollar un sistema de soporte a decisiones geoespacial multicriterio para evaluar la sostenibilidad territorial de puestos de salud rurales en el distrito de Pichacani, provincia y departamento de Puno. El problema se relaciona con la ausencia de una herramienta técnica que integre información geográfica, poblacional y territorial para analizar la pertinencia de los establecimientos de salud de primer nivel ubicados en zonas rurales dispersas. Esta situación dificulta identificar establecimientos con necesidad de fortalecimiento, zonas con brechas de acceso, áreas con posible superposición de cobertura y espacios donde podría evaluarse la creación o reubicación de puntos de atención.

	La investigación será de tipo aplicada, con enfoque cuantitativo, diseño no experimental y alcance descriptivo-propositivo, incorporando desarrollo tecnológico mediante la implementación de un prototipo funcional. Se emplearán fuentes oficiales y abiertas como RENIPRESS, GeoMINSA, INEI, DIRESA Puno, Red de Salud Puno y OpenStreetMap para construir una base territorial de establecimientos de salud, centros poblados, población y vías de acceso. El modelo utilizará análisis geoespacial y ponderación multicriterio para calcular un Índice de Sostenibilidad Territorial, considerando dimensiones como demanda poblacional, accesibilidad geográfica, cobertura territorial, redundancia de establecimientos y vulnerabilidad poblacional.

	Como resultado, se espera obtener un prototipo con visualización cartográfica, mapas de cobertura, ranking de sostenibilidad territorial y simulación de escenarios de intervención. La propuesta busca aportar una herramienta desde la Ingeniería de Sistemas para apoyar la toma de decisiones en la planificación territorial del primer nivel de atención, sin reemplazar criterios normativos ni decisiones institucionales, sino integrando datos verificables y criterios técnicos aplicables al contexto rural de Pichacani.

3. **Palabras claves (Keywords)**

**Soporte a decisiones; análisis geoespacial; multicriterio; sostenibilidad territorial; puestos de salud.**

4. **Justificación del proyecto**

	El primer nivel de atención constituye la puerta de entrada al sistema de salud y cumple un rol fundamental en la prevención, promoción, atención básica y continuidad del cuidado de la población. En el ámbito rural, los puestos de salud adquieren especial importancia porque atienden poblaciones dispersas, con limitaciones de acceso y mayores dificultades de desplazamiento hacia establecimientos de mayor capacidad resolutiva. Por ello, su ubicación y permanencia no deberían analizarse únicamente desde criterios administrativos, sino también desde criterios territoriales, poblacionales y geográficos.

En el distrito de Pichacani, provincia de Puno, existen condiciones rurales que hacen relevante analizar la sostenibilidad territorial de los puestos de salud. La dispersión de centros poblados, las distancias entre comunidades, las características de la red vial y la posible variación de la demanda poblacional pueden afectar la pertinencia territorial de los establecimientos de primer nivel. Sin embargo, la evaluación de estos establecimientos suele depender de información dispersa o de criterios no integrados en una herramienta geoespacial de apoyo a decisiones.

	En esta investigación, la sostenibilidad territorial se entiende como el grado en que la ubicación, accesibilidad, cobertura, población de influencia, redundancia con otros establecimientos y vulnerabilidad territorial justifican la permanencia, fortalecimiento, reubicación o creación de un puesto de salud rural. Este concepto no se refiere a sostenibilidad ambiental ni implica decidir cierres administrativos, sino a evaluar técnicamente la pertinencia territorial de los establecimientos para apoyar procesos de planificación.

	El problema general de investigación se formula de la siguiente manera: ¿Cómo un sistema de soporte a decisiones geoespacial multicriterio permite evaluar la sostenibilidad territorial de puestos de salud rurales en Pichacani, Puno, 2026? De este problema se desprenden interrogantes específicas relacionadas con la distribución espacial de establecimientos, centros poblados, población y vías; la definición de criterios de evaluación territorial; el cálculo de un índice multicriterio; y la simulación de escenarios de fortalecimiento, reubicación o creación de puntos de atención.

	El proyecto se justifica desde la Ingeniería de Sistemas porque integra análisis geoespacial, modelamiento multicriterio, procesamiento de datos, bases de datos territoriales, visualización cartográfica y desarrollo de un sistema de soporte a decisiones. A diferencia de un visor geográfico simple, la propuesta busca transformar datos oficiales y abiertos en indicadores útiles para evaluar la sostenibilidad territorial de puestos de salud rurales.

	La investigación se delimita al distrito de Pichacani, con énfasis en establecimientos rurales vinculados a la Microred Laraqueri, debido a que representa un ámbito con condiciones de ruralidad, dispersión territorial y viabilidad para el levantamiento de información contextual. Esta delimitación permite evitar un alcance excesivamente amplio y desarrollar un caso piloto que podría ser adaptado posteriormente a otros distritos rurales de la región Puno.

5. **Antecedentes del proyecto**

La accesibilidad geográfica a los servicios de salud constituye una dimensión fundamental para analizar la equidad territorial, especialmente en zonas rurales, dispersas o de difícil conectividad. Wood et al. identificaron que el uso de medidas espaciales objetivas y transparentes permite reconocer desigualdades territoriales y orientar una distribución más equitativa de los recursos sanitarios Wood et al. (2023). En una línea similar, Lechowski y Jasion estudiaron la accesibilidad espacial a la atención primaria en áreas rurales, evidenciando la importancia de evaluar la relación entre población, ubicación de establecimientos y condiciones de desplazamiento Lechowski & Jasion (2021). Estos antecedentes respaldan la necesidad de utilizar indicadores geoespaciales verificables para evaluar puestos de salud rurales.

En contextos rurales y remotos, Verma y Dash evaluaron la accesibilidad geográfica y la cobertura espacial de la red pública de salud en India, identificando que las largas distancias, las restricciones topográficas, la limitada capacidad de los establecimientos y las redes viales deficientes generan barreras relevantes para el acceso efectivo a los servicios de salud Verma & Dash (2020). Asimismo, Bhangdia et al.  compararon medidas absolutas y relativas de distancia y tiempo de viaje hacia establecimientos de salud en Haití rural, mostrando que la medición del acceso geográfico puede variar según el indicador utilizado Bhangdia et al. (2022). Estos estudios son pertinentes para la presente investigación porque evidencian que la evaluación territorial de establecimientos rurales no debe limitarse a su existencia administrativa, sino considerar accesibilidad real, red vial, cobertura espacial y condiciones físicas del desplazamiento.

Desde el enfoque de planificación espacial, Polo et al. integraron modelos de accesibilidad y localización-asignación en Sistemas de Información Geográfica para mejorar la planificación de servicios públicos de salud. Su investigación empleó un modelo 2SFCA modificado, función de impedancia, coeficiente de fricción, distancias mediante red vial y algoritmo de Dijkstra Polo et al. (2015). De manera complementaria, Murad et al. aplicaron el modelo p-mediana de localización-asignación para optimizar la ubicación de centros de salud, mostrando la utilidad de estos modelos para analizar la distribución territorial de servicios sanitarios Murad et al. (2021). Posteriormente, Murad et al. combinaron modelos de decisión multicriterio y p-mediana para optimizar la localización de servicios de salud en un contexto urbano Murad et al. (2024). Asimismo, Pan et al. aplicaron modelos de localización-asignación para evaluar mejoras de accesibilidad espacial derivadas de nuevos hospitales Polo et al. (2015). Estos antecedentes aportan una base metodológica para analizar cobertura, accesibilidad y asignación territorial de establecimientos de salud.

En el contexto peruano, Carrasco-Escobar et al. analizaron el tiempo de viaje hacia establecimientos de salud como marcador de accesibilidad geográfica en el Perú, considerando coberturas territoriales heterogéneas Carrasco-Escobar et al. (2020). El estudio empleó información geoespacial de centros poblados, establecimientos de salud, cobertura terrestre, red vial, ríos y elevación digital para estimar tiempos de desplazamiento. Este antecedente es central para la presente tesis porque demuestra que, en el contexto peruano, la accesibilidad no debe medirse únicamente mediante distancia lineal, sino también mediante condiciones territoriales que afectan el tiempo real de viaje.

En relación con los métodos multicriterio, Frazão et al. realizaron una revisión sistemática sobre el uso del análisis multicriterio en salud, señalando que el MCDA permite estructurar decisiones complejas en las que intervienen múltiples criterios, objetivos y actores Frazão et al. (2018). Este enfoque resulta pertinente porque la sostenibilidad territorial de un puesto de salud rural no depende de una sola variable, sino de la combinación de criterios como demanda poblacional, accesibilidad geográfica, cobertura territorial, redundancia de establecimientos, vulnerabilidad poblacional y criterios institucionales. En esa misma línea, Aroge et al. aplicaron una combinación de GIS, MCDA y AHP para seleccionar ubicaciones adecuadas de establecimientos de atención primaria Aroge et al. (2023). Este estudio se relaciona directamente con la investigación propuesta porque integra herramientas geoespaciales y ponderación multicriterio para apoyar decisiones sobre infraestructura sanitaria.

Otros estudios recientes también evidencian la utilidad de combinar análisis geoespacial y criterios de decisión para la planificación sanitaria. Tripathi et al. compararon métodos GIS-AHP y fuzzy AHP para la selección de sitios hospitalarios, mostrando que los métodos multicriterio permiten ponderar condiciones territoriales y criterios de localización Tripathi et al. (2022). Zandi et al. aplicaron una evaluación multicriterio habilitada por GIS para analizar la idoneidad de ubicación hospitalaria en Teherán Zandi et al. (2024). Aunque estos trabajos se orientan principalmente a hospitales o entornos urbanos, aportan criterios metodológicos útiles para adaptar el análisis multicriterio al estudio de puestos de salud rurales.

La planificación sanitaria también requiere incorporar escenarios de cambio territorial y adaptación del sistema de salud. Balsa-Barreiro et al. proponen el uso de accesibilidad por tiempo de viaje y soluciones de planificación espacial adaptativa para sistemas de salud Balsa-Barreiro et al. (2025). Este antecedente es relevante porque se aproxima a uno de los fenómenos que motivan la presente investigación: la necesidad de adaptar la planificación de establecimientos sanitarios ante cambios demográficos, territoriales y de accesibilidad. Su aporte respalda la incorporación de escenarios de simulación territorial en el sistema propuesto.

En América Latina y contextos rurales, Houghton et al. analizaron barreras de acceso enfrentadas por comunidades rurales y dispersas en las Américas, destacando la necesidad de identificar factores que limitan el acceso para orientar respuestas de política pública y planificación territorial Houghton et al. (2023). Franco et al. identificaron desafíos de acceso, organización y disponibilidad de fuerza laboral en la atención primaria rural Franco et al. (2021) Asimismo, Garnelo et al. estudiaron barreras de acceso y organización de los servicios de atención primaria en poblaciones rurales ribereñas de la Amazonía Garnelo et al. (2020). Estos antecedentes permiten contextualizar la investigación en realidades similares a las de Puno, donde la ruralidad, la dispersión poblacional, la vulnerabilidad y las condiciones geográficas pueden afectar la oportunidad de atención en el primer nivel.

En el ámbito nacional, el Instituto Nacional de Estadística e Informática proporciona información censal necesaria para analizar la distribución poblacional, centros poblados y características territoriales de la población Instituto Nacional de Estadística e Informática (2018) Estos datos resultan fundamentales para estimar la demanda potencial y la población de influencia de los puestos de salud rurales. Asimismo, el Ministerio de Salud establece la categorización de establecimientos del sector salud, lo cual permite delimitar técnicamente el objeto de estudio hacia establecimientos del primer nivel de atención, como puestos y postas de salud Ministerio de Salud (s/f-a). Además, el Ministerio de Salud presenta el Diagnóstico de Brechas de Infraestructura o Acceso a Servicios del Sector Salud 2024–2026, documento que permite contextualizar la necesidad de analizar brechas de infraestructura, capacidad instalada y acceso a servicios de salud en el país Ministerio de Salud (2023).

Desde las fuentes oficiales de información sanitaria, RENIPRESS constituye una fuente clave porque permite verificar establecimientos registrados y consultar información por departamento, provincia, distrito, institución, categoría, red y microred (Superintendencia Nacional de Salud, s/f). En esta tesis, RENIPRESS será utilizado como fuente principal para identificar los establecimientos de salud del ámbito de estudio. De manera complementaria, GeoMINSA proporciona una plataforma geográfica oficial para visualizar establecimientos y redes de salud, por lo que será empleada para contrastar la ubicación territorial de los establecimientos (Ministerio de Salud, s/f-b)

En el ámbito regional, el Plan Operativo Institucional Anual 2025 de la Red de Salud Puno constituye una fuente contextual relevante para comprender la organización sanitaria regional y la existencia de redes y microrredes de salud en el departamento de Puno (Red de Salud Puno, 2024). En este marco, la presente investigación se orienta al distrito de Pichacani, con énfasis en establecimientos rurales vinculados al ámbito de la Microred Laraqueri. Esta delimitación permite desarrollar un caso de estudio específico, viable y coherente con el análisis de sostenibilidad territorial en zonas rurales.

Respecto al ámbito local universitario, la revisión preliminar del repositorio de la Universidad Nacional del Altiplano muestra la existencia de tesis relacionadas con sistemas de información, salud, telemedicina, farmacia, minería de datos y aplicaciones geoespaciales. Sin embargo, hasta esta etapa no se ha identificado una tesis centrada específicamente en un sistema de soporte a decisiones geoespacial multicriterio para evaluar la sostenibilidad territorial de puestos de salud rurales en Pichacani. Esta revisión deberá actualizarse antes del registro oficial, pero permite sostener preliminarmente que la propuesta no replica directamente los temas más frecuentes del repositorio institucional.

En síntesis, los antecedentes revisados evidencian que existen investigaciones internacionales y nacionales sobre accesibilidad geográfica, SIG, MCDA, AHP y modelos de localización-asignación aplicados a servicios de salud. No obstante, se identifica una brecha local: la falta de una herramienta aplicada al contexto rural de Pichacani que integre datos oficiales, análisis geoespacial, ponderación multicriterio y simulación de escenarios para evaluar la sostenibilidad territorial de puestos de salud rurales. La presente tesis busca cubrir esa brecha mediante el desarrollo de un sistema de soporte a decisiones desde la Ingeniería de Sistemas.

6. **Hipótesis del trabajo**

Hipótesis general

La implementación de un sistema de soporte a decisiones geoespacial multicriterio permite evaluar de manera integral la sostenibilidad territorial de puestos de salud rurales en Pichacani, Puno, mediante la integración de criterios de demanda poblacional, accesibilidad geográfica, cobertura territorial, redundancia de establecimientos y vulnerabilidad poblacional.

Hipótesis específicas

H1: La integración de datos oficiales y geográficos sobre puestos de salud, centros poblados, población y vías de acceso permite caracterizar la distribución territorial de los establecimientos de salud rurales en Pichacani.

H2: La definición de criterios e indicadores geoespaciales y multicriterio permite operacionalizar la sostenibilidad territorial de los puestos de salud rurales.

H3: El modelo multicriterio ponderado permite calcular un Índice de Sostenibilidad Territorial para clasificar los puestos de salud rurales según su nivel de sostenibilidad territorial.

H4: El prototipo de sistema de soporte a decisiones permite visualizar resultados, analizar escenarios territoriales y apoyar la identificación de establecimientos o zonas prioritarias para intervención.

Hipótesis nula general

La implementación de un sistema de soporte a decisiones geoespacial multicriterio no mejora la evaluación de la sostenibilidad territorial de puestos de salud rurales en Pichacani, Puno, frente a una evaluación basada únicamente en ubicación administrativa.

7. **Objetivo general**

**Desarrollar un sistema de soporte a decisiones basado en análisis geoespacial multicriterio para evaluar la sostenibilidad territorial de puestos de salud rurales en Pichacani, Puno, 2026\.**

8. **Objetivos específicos**

1\.	Caracterizar la distribución territorial de los puestos de salud rurales, centros poblados, población y vías de acceso del distrito de Pichacani mediante fuentes oficiales y datos geográficos abiertos.

2\.	Definir las dimensiones, criterios e indicadores geoespaciales y multicriterio para evaluar la sostenibilidad territorial de los puestos de salud rurales.

3\.	Diseñar un modelo multicriterio ponderado que calcule un Índice de Sostenibilidad Territorial aplicable a los puestos de salud rurales del ámbito de estudio.

4\.	Implementar y validar un prototipo de sistema de soporte a decisiones con visualización cartográfica, ranking territorial y análisis de escenarios de intervención.

**Tabla 1\. Relación entre objetivos específicos, hipótesis específicas y productos esperados**

| Objetivo específico | Hipótesis vinculada | Producto esperado | Técnica / herramienta |
| ----- | ----- | ----- | ----- |
| OE1 | H1 | Base territorial caracterizada | Revisión documental, georreferenciación, SIG |
| OE2 | H2 | Dimensiones, criterios e indicadores definidos | Revisión bibliográfica, criterios normativos, juicio de expertos |
| OE3 | H3 | Índice de Sostenibilidad Territorial diseñado | Normalización, ponderación multicriterio, análisis de sensibilidad |
| OE4 | H4 | Prototipo validado con mapas y escenarios | PostGIS, Python, QGIS, interfaz web, evaluación por expertos |

9. **Metodología de investigación**

La investigación será de tipo aplicada, porque busca resolver un problema práctico de planificación territorial de servicios de salud mediante el desarrollo de un sistema de soporte a decisiones. Tendrá enfoque cuantitativo, debido a que utilizará datos georreferenciados, población, distancias, cobertura, puntajes normalizados e indicadores ponderados. El diseño será no experimental, ya que no se manipularán variables reales del sistema de salud, sino que se observarán y modelarán condiciones territoriales existentes. El alcance será descriptivo-propositivo, porque primero describirá la situación territorial actual y luego propondrá un modelo y prototipo tecnológico.

El ámbito de estudio será el distrito de Pichacani, provincia y departamento de Puno, con énfasis en puestos de salud rurales vinculados a la Microred Laraqueri. La delimitación responde a la presencia de condiciones rurales, dispersión territorial, establecimientos de primer nivel y viabilidad para levantar información contextual mediante fuentes oficiales, observación territorial y validación con actores vinculados al ámbito de estudio.

La unidad de análisis principal estará conformada por los puestos de salud rurales del distrito de Pichacani. Como unidades territoriales complementarias se considerarán los centros poblados, la población vinculada al área de influencia de los establecimientos y las vías de acceso. La población de expertos estará conformada por personal de salud, responsables de estadística o admisión, encargados de establecimientos, docentes de Ingeniería de Sistemas y profesionales vinculados a planificación territorial o gestión sanitaria. La muestra será no probabilística por conveniencia y criterio.

Las fuentes de datos serán RENIPRESS para identificar establecimientos registrados, categoría, distrito, red y microred; GeoMINSA para complementar la ubicación geográfica de establecimientos; INEI para datos poblacionales y centros poblados; DIRESA Puno y Red de Salud Puno para documentos de gestión; y OpenStreetMap u otras fuentes geográficas abiertas para vías de acceso. Los datos serán depurados, georreferenciados y organizados en una base territorial para su posterior análisis.

La investigación no utilizará historias clínicas ni datos personales de pacientes. La participación de expertos será voluntaria, con fines de validación metodológica, resguardando la confidencialidad de sus respuestas. De ser requerido por la normativa institucional, se solicitará la evaluación correspondiente al Comité Institucional de Ética en Investigación.

**Tabla 2\. Operacionalización de variables**

| Variable | Dimensiones | Indicadores | Fuente / forma de medición |
| ----- | ----- | ----- | ----- |
| Independiente: Sistema de soporte a decisiones geoespacial multicriterio | Gestión de datos | Integración de establecimientos, centros poblados, población y vías | RENIPRESS, GeoMINSA, INEI, OSM |
|  | Modelamiento multicriterio | Normalización, ponderación y cálculo del índice | MCDA, revisión bibliográfica, juicio de expertos |
|  | Visualización y soporte a decisiones | Mapas, ranking, filtros y escenarios | Prototipo web, QGIS, PostGIS |
| Dependiente: Sostenibilidad territorial de puestos de salud rurales | Demanda poblacional | Población cercana y centros poblados de influencia | INEI, análisis espacial |
|  | Accesibilidad geográfica | Distancia, tiempo estimado y cercanía a vías | SIG, red vial, OSM |
|  | Cobertura territorial | Población y centros poblados dentro/fuera del área de influencia | Buffers, rutas, mapas de cobertura |
|  | Redundancia territorial | Superposición o proximidad con otros establecimientos | RENIPRESS, GeoMINSA, análisis de proximidad |
|  | Vulnerabilidad poblacional | Ruralidad, grupos etarios dependientes u otros indicadores disponibles | INEI y fuentes oficiales |

**Tabla 3\. Técnicas de recolección de datos por objetivos específicos**

| Objetivo específico | Técnica de recolección | Instrumento / herramienta | Producto esperado |
| ----- | ----- | ----- | ----- |
| OE1 | Revisión documental y descarga de datos | RENIPRESS, GeoMINSA, INEI, OSM, QGIS | Base territorial depurada y georreferenciada |
| OE2 | Revisión bibliográfica, normativa y consulta a expertos | Ficha de validación, escala Likert, matriz de criterios | Criterios e indicadores validados |
| OE3 | Modelamiento y procesamiento de datos | Python, PostGIS, QGIS, normalización min-max | Índice de Sostenibilidad Territorial |
| OE4 | Desarrollo y validación tecnológica | Prototipo web, mapas, ranking, ficha de evaluación | Sistema funcional y resultados de validación |

El procedimiento metodológico tendrá cuatro fases. En la primera fase se caracterizará la distribución territorial de puestos de salud rurales, centros poblados, población y vías de acceso. En la segunda fase se definirán las dimensiones, criterios e indicadores de sostenibilidad territorial mediante revisión bibliográfica, criterios normativos y juicio de expertos. En la tercera fase se diseñará el modelo multicriterio ponderado para calcular el Índice de Sostenibilidad Territorial. En la cuarta fase se implementará y validará el prototipo del sistema mediante visualización cartográfica, ranking territorial, análisis de escenarios y evaluación por expertos.

El modelo multicriterio se basará en una ponderación lineal normalizada: IST \= w1D \+ w2A \+ w3C \+ w4R \+ w5V. Donde IST representa el Índice de Sostenibilidad Territorial; D, demanda poblacional; A, accesibilidad geográfica; C, cobertura territorial; R, redundancia o superposición con otros establecimientos; y V, vulnerabilidad poblacional. Cada criterio será normalizado en una escala de 0 a 100\. Los pesos serán definidos mediante revisión bibliográfica, contraste normativo y validación por expertos.

Para la validación del modelo se empleará una ficha de juicio de expertos con escala tipo Likert de 1 a 5, evaluando pertinencia, claridad, relevancia y viabilidad de los criterios e indicadores. Participarán entre tres y cinco expertos vinculados al ámbito sanitario, territorial o tecnológico. Si corresponde, se podrá aplicar el coeficiente V de Aiken para estimar la validez de contenido de los criterios e instrumentos.

Para la validación del prototipo se evaluarán dimensiones de utilidad, claridad de visualización, facilidad de uso, pertinencia de los mapas, comprensión del ranking y capacidad para apoyar escenarios de decisión. El análisis de escenarios considerará al menos tres situaciones: cobertura actual, reducción funcional de un establecimiento y fortalecimiento, reubicación o creación de un punto de atención.

Los análisis estadísticos incluirán estadística descriptiva, normalización min-max, análisis de sensibilidad y comparación de rankings o concordancia con la valoración de expertos cuando sea aplicable. También se utilizarán técnicas geoespaciales como análisis de proximidad, buffers, mapas de cobertura, mapas de calor y cálculo de distancias o rutas por red vial, según la disponibilidad y calidad de los datos.

El prototipo podrá desarrollarse con PostgreSQL/PostGIS para almacenamiento geográfico, Python para procesamiento de datos, QGIS para análisis espacial y una interfaz web con Django, React o Leaflet para visualización cartográfica.

10. **Referencias (Listar las citas bibliográficas con el estilo adecuado a su especialidad)**

	**Antecedentes Internacionales**

Aroge, S. K., Emmanuel, A. B., Babatunde, A. N., & Sola, A. J. (2023). Combination of GIS, MCDA and AHP for the Selection of Most Suitable Location for Primary Health Care Facilities. *American Journal of Geospatial Technology*, *2*(1), 01–06. https://doi.org/10.54536/ajgt.v2i1.1820

Balsa-Barreiro, J., Batista, S. F. A., Hannoun, G. J., & Menendez, M. (2025). Travel-time accessibility and adaptive spatial planning solutions for the healthcare system. *npj Health Systems*, *2*(1). https://doi.org/10.1038/s44401-025-00028-1

Carrasco-Escobar, G., Manrique, E., Tello-Lizarraga, K., & Miranda, J. J. (2020). Travel Time to Health Facilities as a Marker of Geographical Accessibility Across Heterogeneous Land Coverage in Peru. *Frontiers in Public Health*, *8*. https://doi.org/10.3389/fpubh.2020.00498

Franco, C. M., Lima, J. G., & Giovanella, L. (2021). Primary healthcare in rural areas: Access, organization, and health workforce in an integrative literature review. En *Cadernos de Saude Publica* (Vol. 37, Número 7). Fundacao Oswaldo Cruz. https://doi.org/10.1590/0102-311X00310520

Frazão, T. D. C., Camilo, D. G. G., Cabral, E. L. S., & Souza, R. P. (2018). Multicriteria decision analysis (MCDA) in health care: A systematic review of the main characteristics and methodological steps. En *BMC Medical Informatics and Decision Making* (Vol. 18, Número 1). BioMed Central Ltd. https://doi.org/10.1186/s12911-018-0663-1

Garnelo, L., Parente, R. C. P., Puchiarelli, M. L. R., Correia, P. C., Torres, M. V., & Herkrath, F. J. (2020). Barriers to access and organization of primary health care services for rural riverside populations in the Amazon. *International Journal for Equity in Health*, *19*(1). https://doi.org/10.1186/s12939-020-01171-x

Houghton, N., Bascolo, E., Cohen, R. R., Vilcarromero, N. L. C., Gonzalez, H. R., Albrecht, D., Koller, T. S., & Fitzgerald, J. (2023). Identifying access barriers faced by rural and dispersed communities to better address their needs: implications and lessons learned for rural proofing for health in the Americas and beyond. *Rural and Remote Health*, *23*(1). [https://doi.org/10.22605/RRH7822](https://doi.org/10.22605/RRH7822)

**Fuentes oficiales peruanas para contextualizar el antecedente nacional**

Instituto Nacional de Estadística e Informática. (2018). Perú: Resultados definitivos de los Censos Nacionales 2017\. En *https://www.inei.gob.pe/media/MenuRecursivo/publicaciones\_digitales/Est/Lib1544/*. https://www.inei.gob.pe/media/MenuRecursivo/publicaciones\_digitales/Est/Lib1544/

Ministerio de Salud. (s/f-a). *Categorías de establecimientos del sector salud: NT N.° 021-MINSA/DGSP V.01*. Plataforma digital única del Estado Peruano. Recuperado el 31 de mayo de 2026, de https://www.gob.pe/institucion/minsa/informes-publicaciones/352897-categorias-de-establecimientos-del-sector-salud-nt-n-021-minsa-dgsp-v-01

Ministerio de Salud. (s/f-b). *GeoMINSA*. GeoMINSA. Recuperado el 31 de mayo de 2026, de https://geo.minsa.gob.pe/

Ministerio de Salud. (2023). *Diagnóstico de brechas de infraestructura o acceso a servicios del sector salud 2024–2026*. https://www.minsa.gob.pe/Recursos/OTRANS/08Proyectos/2022/Diagnostico-Infraestructura-Sector-Salud-2024-2026.pdf

Red de Salud Puno. (2024). *Plan Operativo Institucional Anual 2025 de la Red de Salud Puno*. https://www.reddesaludpuno.gob.pe/documentos/doc\_gest/POI%202025%20-%20RED%20DE%20SALUD%20PUNO..pdf

Superintendencia Nacional de Salud. (s/f). *Obtener información de las Instituciones Prestadoras de Servicios de Salud \- RENIPRESS*. Plataforma digital única del Estado Peruano. Recuperado el 31 de mayo de 2026, de https://www.gob.pe/10202-obtener-informacion-de-las-instituciones-prestadoras-de-servicios-de-salud-renipress

Tripathi, A. K., Agrawal, S., & Gupta, R. D. (2022). Comparison of GIS-based AHP and fuzzy AHP methods for hospital site selection: a case study for Prayagraj City, India. *GeoJournal*, *87*(5), 3507–3528. https://doi.org/10.1007/S10708-021-10445-Y

Zandi, I., Pahlavani, P., Bigdeli, B., Lotfata, A., Alesheikh, A. A., & Garau, C. (2024). GIS-Enabled Multi-Criteria Assessment for Hospital Site Suitability: A Case Study of Tehran. *Sustainability (Switzerland)* , *16*(5), 2079\. https://doi.org/10.3390/SU16052079/S1

 

11. **Uso de los resultados y contribuciones del proyecto (Señalar el posible uso de los resultados y la contribución de los mismos)**

Los resultados del proyecto podrán ser utilizados como insumo técnico para apoyar la planificación territorial de establecimientos de salud del primer nivel de atención en el distrito de Pichacani, Puno. El sistema de soporte a decisiones permitirá visualizar la distribución de puestos de salud rurales, centros poblados, población y vías de acceso, así como identificar zonas con baja cobertura, posibles superposiciones territoriales y establecimientos que requieren mayor análisis para su fortalecimiento, reubicación o creación de puntos de atención.

La principal contribución del proyecto será el desarrollo de un prototipo geoespacial multicriterio que integre datos oficiales y abiertos en un Índice de Sostenibilidad Territorial. Este índice permitirá evaluar de manera estructurada criterios como demanda poblacional, accesibilidad geográfica, cobertura territorial, redundancia de establecimientos y vulnerabilidad poblacional. De esta manera, la investigación aportará una herramienta aplicada desde la Ingeniería de Sistemas para transformar datos territoriales dispersos en información útil para la toma de decisiones.

Asimismo, el proyecto contribuirá metodológicamente al proponer un modelo replicable en otros distritos rurales de la región Puno. Aunque el estudio se delimita a Pichacani, la estructura del modelo, los criterios de evaluación y el prototipo podrían adaptarse posteriormente a otros ámbitos rurales con características similares.

12. **Impactos esperados**

    1. **Impactos en Ciencia y Tecnología**

    El proyecto aportará al campo de la Ingeniería de Sistemas mediante la integración de análisis geoespacial, modelamiento multicriterio, bases de datos territoriales y visualización cartográfica en un sistema de soporte a decisiones. El desarrollo del prototipo permitirá demostrar la aplicabilidad de herramientas como PostgreSQL/PostGIS, QGIS, Python y tecnologías web para resolver problemas de planificación territorial en servicios públicos.

    

    Además, la investigación contribuirá al uso aplicado de modelos multicriterio en el análisis de sostenibilidad territorial de establecimientos de salud rurales, generando una propuesta que puede servir como antecedente para futuras investigaciones sobre sistemas de información geográfica, accesibilidad espacial, planificación de servicios de salud y toma de decisiones territoriales.

       2. **Impactos económicos**

    El proyecto puede contribuir indirectamente a una mejor priorización de recursos públicos destinados al fortalecimiento, reubicación o creación de establecimientos de salud de primer nivel. Al disponer de información organizada, mapas de cobertura e indicadores de sostenibilidad territorial, las instituciones podrían contar con mejores insumos para orientar inversiones, reducir duplicidad de esfuerzos y focalizar intervenciones en zonas con mayor necesidad territorial.

    Aunque la investigación no ejecuta inversiones ni modifica la infraestructura existente, el sistema propuesto puede apoyar procesos de análisis previo, evitando decisiones basadas únicamente en criterios administrativos o información dispersa.

       3. **Impactos sociales**

    El impacto social esperado se relaciona con la mejora del análisis territorial de acceso a servicios de salud en zonas rurales. Al identificar zonas con baja cobertura, dificultades de accesibilidad o mayor vulnerabilidad poblacional, el sistema puede apoyar decisiones orientadas a mejorar la equidad territorial en el primer nivel de atención.

    La población rural de Pichacani podría beneficiarse indirectamente si los resultados son considerados como insumo para fortalecer la planificación de servicios de salud. El proyecto no interviene directamente en la atención médica ni en decisiones institucionales, pero aporta información técnica que puede favorecer una mejor comprensión de las brechas territoriales existentes.

       4. **Impactos ambientales**

    El proyecto no generará impactos ambientales negativos directos, debido a que se desarrollará principalmente mediante análisis de datos, herramientas geoespaciales y desarrollo de software. No se realizarán obras físicas, intervención sobre ecosistemas ni modificación directa del territorio.

    Como impacto ambiental positivo indirecto, el uso de información geográfica digital puede contribuir a una planificación más ordenada del territorio, evitando desplazamientos innecesarios durante la etapa de análisis y promoviendo el uso de datos digitales para evaluar escenarios antes de realizar intervenciones físicas.

13. **Recursos necesarios (Infraestructura, equipos y principales tecnologías en uso relacionadas con la temática del proyecto,** señale medios y recursos para realizar el proyecto**)**

Para el desarrollo del proyecto se requerirán recursos tecnológicos, información oficial y recursos humanos vinculados al proceso de validación.

En infraestructura tecnológica se utilizará una computadora personal con capacidad para procesamiento de datos geográficos, conexión a internet y almacenamiento suficiente para bases de datos, capas geoespaciales y archivos de análisis. En cuanto a software, se emplearán herramientas como QGIS para análisis espacial, PostgreSQL/PostGIS para almacenamiento geográfico, Python para procesamiento y normalización de datos, y tecnologías web como Django, React o Leaflet para el desarrollo del prototipo de visualización cartográfica.

Las principales fuentes de información serán RENIPRESS, GeoMINSA, INEI, DIRESA Puno, Red de Salud Puno, OpenStreetMap y otros datos geográficos abiertos disponibles. También se requerirá información contextual obtenida mediante revisión documental, observación del ámbito de estudio y juicio de expertos.

Respecto a recursos humanos, se necesitará la participación del investigador, asesor de tesis, expertos en salud o gestión territorial, personal vinculado a establecimientos de salud rurales y, de ser necesario, docentes o profesionales de Ingeniería de Sistemas para validar el modelo y el prototipo.

**Tabla 4\. Recursos principales del proyecto**

| Tipo de recurso | Detalle | Uso previsto |
| ----- | ----- | ----- |
| Datos oficiales | RENIPRESS, GeoMINSA, INEI, Red de Salud Puno | Construcción de la base territorial |
| Software | QGIS, PostgreSQL/PostGIS, Python, Django/React/Leaflet | Análisis, modelamiento y prototipo |
| Recursos humanos | Investigador, asesor, expertos en salud, gestión territorial y sistemas | Validación metodológica y funcional |
| Equipo | Computadora personal e internet | Procesamiento, desarrollo y redacción |

14. **Localización del proyecto (indicar donde se llevará a cabo el proyecto)**

El proyecto se llevará a cabo en el distrito de Pichacani, provincia y departamento de Puno, Perú, con énfasis en puestos de salud rurales vinculados al ámbito de la Microred Laraqueri.

La localización fue seleccionada debido a sus características rurales, dispersión de centros poblados, distancias entre comunidades y presencia de establecimientos de salud de primer nivel. Estas condiciones hacen pertinente el análisis de sostenibilidad territorial mediante criterios geoespaciales y multicriterio.

El procesamiento de datos, modelamiento, desarrollo del prototipo y análisis de resultados se realizará principalmente en gabinete, utilizando fuentes oficiales y datos geográficos abiertos. La validación contextual podrá realizarse mediante consulta a expertos y actores vinculados al ámbito sanitario o territorial del distrito.

15. **Cronograma de actividades**

| Actividad | Meses |  |  |  |  |  |  |  |  |  |  |  |
| :---- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  | I | II | III | IV | V | VI | VII | VII | IX | X | XI | XII |
| Revisión bibliográfica, normativa y antecedentes | X | X |  |  |  |  |  |  |  |  |  |  |
| Delimitación del ámbito de estudio y ajuste metodológico | X | X |  |  |  |  |  |  |  |  |  |  |
| Recopilación de datos oficiales y geográficos |  | X | X |  |  |  |  |  |  |  |  |  |
| Depuración, normalización y georreferenciación de datos |  |  | X | X |  |  |  |  |  |  |  |  |
| Caracterización territorial de puestos de salud, centros poblados, población y vías |  |  |  | X | X |  |  |  |  |  |  |  |
| Definición de dimensiones, criterios e indicadores de sostenibilidad territorial |  |  |  | X | X |  |  |  |  |  |  |  |
| Validación inicial de criterios mediante juicio de expertos |  |  |  |  | X | X |  |  |  |  |  |  |
| Diseño del modelo multicriterio ponderado |  |  |  |  |  | X | X |  |  |  |  |  |
| Cálculo del Índice de Sostenibilidad Territorial |  |  |  |  |  |  | X | X |  |  |  |  |
| Diseño del prototipo del sistema de soporte a decisiones |  |  |  |  |  |  | X | X |  |  |  |  |
| Implementación del prototipo geoespacial |  |  |  |  |  |  |  | X | X |  |  |  |
| Generación de mapas, ranking territorial y escenarios de simulación |  |  |  |  |  |  |  |  | X | X |  |  |
| Validación del modelo y prototipo con expertos |  |  |  |  |  |  |  |  |  | X | X |  |
| Análisis e interpretación de resultados |  |  |  |  |  |  |  |  |  | X | X |  |
| Redacción del informe final de tesis |  |  |  |  |  |  | X | X | X | X | X |  |
| Revisión, corrección y sustentación |  |  |  |  |  |  |  |  |  |  | X | X |

    

16. **Presupuesto**

    

| Descripción | Unidad de medida | Costo Unitario (S/.) | Cantidad | Costo total (S/.) |
| :---- | :---- | :---- | :---- | :---- |
| Servicio de internet | Mes | 80.00 | 4 | 320.00 |
| Movilidad local para validación y observación | Viaje | 40.00 | 6 | 240.00 |
| Impresiones y copias de instrumentos | Paquete | 30.00 | 3 | 90.00 |
| Material de escritorio | Paquete | 50.00 | 1 | 50.00 |
| Anillado o empastado preliminar | Unidad | 25.00 | 2 | 50.00 |
| Validación de instrumentos / fichas para expertos | Paquete | 30.00 | 3 | 90.00 |
| Energía eléctrica y uso de equipo propio | Mes | 40.00 | 4 | 160.00 |
| Contingencias | Global | 100.00 | 1 | 100.00 |
| Total estimado |  |  |  | 1,100.00 |

El presupuesto será financiado con recursos propios del investigador. Se priorizará el uso de software libre y fuentes de datos oficiales o abiertas, como QGIS, PostgreSQL/PostGIS, Python, RENIPRESS, GeoMINSA, INEI y OpenStreetMap, con el fin de reducir costos de implementación.

