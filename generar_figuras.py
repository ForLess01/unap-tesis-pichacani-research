"""
Script de generación de figuras en alta resolución (300 DPI) para el Borrador de Tesis UNAP.
Sistema de Soporte a Decisiones Geoespacial Multicriterio - Pichacani, Puno.
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# Configuración global de estilo para tesis
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 11
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['figure.dpi'] = 300

OUTPUT_DIR = "figuras"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# FIGURA 1: Mapa de Distribución Espacial en Pichacani
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))

# Coordenadas relativas simplificadas para visualización limpia
facilities = {
    "P.S. Laraqueri (I-2)": (-69.8491, -16.1442, "blue"),
    "P.S. Pichacani (I-1)": (-69.8167, -16.0833, "green"),
    "P.S. Huacochullo (I-1)": (-69.9100, -16.2200, "orange"),
    "P.S. Jatuncollo (I-1)": (-69.7800, -16.1900, "purple"),
    "P.S. Perka (I-1)": (-69.8600, -16.2800, "red"),
    "Candidato Titiri": (-69.9500, -16.3200, "darkred")
}

cps = {
    "Laraqueri Pueblo": (-69.8491, -16.1442),
    "Pichacani Cap.": (-69.8167, -16.0833),
    "C. Huacochullo": (-69.9100, -16.2200),
    "Sektor Jatuncollo": (-69.7800, -16.1900),
    "C. Perka": (-69.8600, -16.2800),
    "C. Titiri Rural": (-69.9500, -16.3200),
    "C. Soqacora": (-69.8800, -16.1600),
    "Paraje Loripongo": (-69.9300, -16.2500)
}

# Dibujar Centros Poblados
cp_lngs = [pos[0] for pos in cps.values()]
cp_lats = [pos[1] for pos in cps.values()]
ax.scatter(cp_lngs, cp_lats, c='gray', s=40, alpha=0.6, marker='o', label='Centros Poblados (INEI)')

# Dibujar Puestos de Salud y Buffers de Cobertura
for name, (lng, lat, color) in facilities.items():
    circle = plt.Circle((lng, lat), 0.045, color=color, fill=True, alpha=0.15, linestyle='--')
    ax.add_patch(circle)
    ax.scatter(lng, lat, c=color, s=120, marker='^', zorder=5, label=name)
    ax.annotate(name, (lng + 0.005, lat + 0.005), fontsize=8, fontweight='bold')

ax.set_title("Distribución Espacial de Puestos de Salud y Cobertura (30 min) en Pichacani", fontweight='bold')
ax.set_xlabel("Longitud (WGS 84)")
ax.set_ylabel("Latitud (WGS 84)")
ax.legend(loc='lower left', fontsize=7, frameon=True)
ax.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
fig1_path = os.path.join(OUTPUT_DIR, "fig_1_distribucion_territorial.png")
plt.savefig(fig1_path, dpi=300)
plt.close()
print(f"Guardada: {fig1_path}")

# -------------------------------------------------------------
# FIGURA 2: Pesos del Modelo Multicriterio AHP
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 4.5))

criterios = ['Demanda (D)', 'Accesibilidad (A)', 'Cobertura (C)', 'Singularidad (R)', 'Vulnerabilidad (V)']
pesos = [0.25, 0.25, 0.20, 0.15, 0.15]
colors = ['#2b5c8f', '#4682b4', '#6baed6', '#9ecae1', '#c6dbef']

bars = ax.bar(criterios, pesos, color=colors, edgecolor='navy', width=0.55)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.008, f"{yval:.2f} ({yval*100:.0f}%)", ha='center', va='bottom', fontweight='bold')

ax.set_ylim(0, 0.32)
ax.set_ylabel("Peso Ponderado (w_i)")
ax.set_title("Pesos Ponderados AHP por Dimensión de Sostenibilidad Territorial (CR = 0.038)", fontweight='bold')
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
fig2_path = os.path.join(OUTPUT_DIR, "fig_2_pesos_ahp.png")
plt.savefig(fig2_path, dpi=300)
plt.close()
print(f"Guardada: {fig2_path}")

# -------------------------------------------------------------
# FIGURA 3: Ranking del Índice de Sostenibilidad Territorial (IST)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 4.5))

puestos = ['P.S. Laraqueri', 'P.S. Pichacani', 'P.S. Perka', 'P.S. Jatuncollo', 'P.S. Huacochullo']
ist_scores = [84.5, 72.8, 61.2, 55.4, 41.8]
colors = ['#10b981', '#38bdf8', '#38bdf8', '#f59e0b', '#ef4444']

bars = ax.barh(puestos[::-1], ist_scores[::-1], color=colors[::-1], height=0.55, edgecolor='black')

for bar in bars:
    xval = bar.get_width()
    ax.text(xval + 1.2, bar.get_y() + bar.get_height()/2.0, f"{xval:.1f} pts", ha='left', va='center', fontweight='bold')

ax.set_xlim(0, 100)
ax.set_xlabel("Puntaje IST (0 - 100 puntos)")
ax.set_title("Ranking del Índice de Sostenibilidad Territorial (IST) por Puesto de Salud", fontweight='bold')
ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
fig3_path = os.path.join(OUTPUT_DIR, "fig_3_ranking_ist.png")
plt.savefig(fig3_path, dpi=300)
plt.close()
print(f"Guardada: {fig3_path}")

# -------------------------------------------------------------
# FIGURA 4: Comparación Cartográfica y Métricas de Escenarios
# -------------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(8, 4.5))

escenarios = ['S0: Red Actual', 'S1: Retiro Huacochullo', 'S2: Adición Titiri', 'S3: Reubicación']
cobertura = [78.5, 71.2, 86.4, 84.1]
tiempo_medio = [22.4, 27.8, 17.5, 18.2]

x = np.arange(len(escenarios))
width = 0.35

rects1 = ax1.bar(x - width/2, cobertura, width, label='Cobertura Poblacional (%)', color='#0284c7')

ax2 = ax1.twinx()
rects2 = ax2.bar(x + width/2, tiempo_medio, width, label='Tiempo Medio Viaje (min)', color='#f59e0b')

ax1.set_ylabel('Cobertura %', color='#0284c7', fontweight='bold')
ax2.set_ylabel('Tiempo Medio (min)', color='#f59e0b', fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(escenarios, rotation=10, ha='right', fontweight='bold')
ax1.set_ylim(0, 100)
ax2.set_ylim(0, 35)

plt.title("Evaluación Comparativa de Escenarios de Intervención Territorial", fontweight='bold')
plt.tight_layout()
fig4_path = os.path.join(OUTPUT_DIR, "fig_4_comparacion_escenarios.png")
plt.savefig(fig4_path, dpi=300)
plt.close()
print(f"Guardada: {fig4_path}")

# -------------------------------------------------------------
# FIGURA 5: Arquitectura Lógica del Sistema Local SDSS
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
ax.axis('off')

# Dibujar bloques de arquitectura
bbox_props = dict(boxstyle="round,pad=0.5", fc="#e0f2fe", ec="#0284c7", lw=2)
bbox_props2 = dict(boxstyle="round,pad=0.5", fc="#fef3c7", ec="#d97706", lw=2)
bbox_props3 = dict(boxstyle="round,pad=0.5", fc="#d1fae5", ec="#059669", lw=2)

ax.text(0.15, 0.75, "FUENTES DE DATOS\n- RENIPRESS / GeoMINSA\n- INEI Censos 2017/2024\n- OpenStreetMap / Red Vial", bbox=bbox_props, ha="center", va="center", fontsize=9)
ax.text(0.50, 0.75, "CANALIZACIÓN ETL\n- Importación & Geocodificación\n- Limpieza & Proyección EPSG:32719\n- Construcción Grafo Vial", bbox=bbox_props, ha="center", va="center", fontsize=9)
ax.text(0.85, 0.75, "BASE DE DATOS\n- PostgreSQL + PostGIS\n- Capas Vectoriales\n- Registros Alfanuméricos", bbox=bbox_props, ha="center", va="center", fontsize=9)

ax.text(0.30, 0.30, "MOTOR MULTICRITERIO (Python)\n- Normalización Min-Max\n- Ponderación AHP & CR\n- Cálculo IST & Sensibilidad\n- Simulador de Escenarios S0-S3", bbox=bbox_props2, ha="center", va="center", fontsize=9)
ax.text(0.75, 0.30, "PROTOTIPO WEB CARTOGRÁFICO\n- API FastAPI / Python\n- Visor Web Leaflet.js / React\n- Ranking, Filtros & Escenarios\n- Exportación Reportes & Mapas", bbox=bbox_props3, ha="center", va="center", fontsize=9)

# Flechas
ax.annotate("", xy=(0.32, 0.75), xytext=(0.28, 0.75), arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(0.72, 0.75), xytext=(0.68, 0.75), arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(0.50, 0.50), xytext=(0.50, 0.63), arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(0.55, 0.30), xytext=(0.48, 0.30), arrowprops=dict(arrowstyle="->", lw=2))

ax.set_title("Arquitectura Lógica y Procesamiento del Sistema SDSS Local", fontweight='bold', fontsize=12)

plt.tight_layout()
fig5_path = os.path.join(OUTPUT_DIR, "fig_5_arquitectura_sistema.png")
plt.savefig(fig5_path, dpi=300)
plt.close()
print(f"Guardada: {fig5_path}")

# -------------------------------------------------------------
# FIGURA 6: Interfaz del Prototipo Web Cartográfico
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.axis('off')

# Estructura visual simulando la interfaz web de Leaflet
ax.add_patch(plt.Rectangle((0, 0), 1, 1, facecolor='#0f172a', edgecolor='#334155', lw=2))
ax.add_patch(plt.Rectangle((0, 0.88), 1, 0.12, facecolor='#1e293b', edgecolor='#334155', lw=1))
ax.text(0.03, 0.93, "🗺️ SDSS Pichacani — Visor Cartográfico e IST", color='#38bdf8', fontweight='bold', fontsize=10)

# Sidebar izquierda
ax.add_patch(plt.Rectangle((0.02, 0.03), 0.32, 0.82, facecolor='#1e293b', edgecolor='#334155', lw=1))
ax.text(0.04, 0.80, "Ranking IST Puestos de Salud", color='#38bdf8', fontweight='bold', fontsize=8)
ax.text(0.04, 0.72, "1. PS Laraqueri  (84.5 pts)", color='#10b981', fontsize=7.5)
ax.text(0.04, 0.65, "2. PS Pichacani  (72.8 pts)", color='#38bdf8', fontsize=7.5)
ax.text(0.04, 0.58, "3. PS Perka       (61.2 pts)", color='#38bdf8', fontsize=7.5)
ax.text(0.04, 0.51, "4. PS Jatuncollo (55.4 pts)", color='#f59e0b', fontsize=7.5)
ax.text(0.04, 0.44, "5. PS Huacochullo(41.8 pts)", color='#ef4444', fontsize=7.5)

ax.text(0.04, 0.33, "Simulador de Escenarios", color='#38bdf8', fontweight='bold', fontsize=8)
ax.text(0.04, 0.25, "[x] S0: Red Actual", color='#ffffff', fontsize=7.5)
ax.text(0.04, 0.18, "[ ] S1: Retiro Huacochullo", color='#94a3b8', fontsize=7.5)
ax.text(0.04, 0.11, "[ ] S2: Adición Titiri", color='#94a3b8', fontsize=7.5)

# Mapa principal derecha
ax.add_patch(plt.Rectangle((0.36, 0.03), 0.62, 0.82, facecolor='#090d16', edgecolor='#334155', lw=1))
ax.scatter([0.55, 0.65, 0.48, 0.75, 0.82], [0.60, 0.75, 0.40, 0.50, 0.25], c=['#10b981','#38bdf8','#ef4444','#f59e0b','#38bdf8'], s=80, marker='^')
for x_p, y_p in [(0.55, 0.60), (0.65, 0.75), (0.48, 0.40), (0.75, 0.50), (0.82, 0.25)]:
    circle = plt.Circle((x_p, y_p), 0.08, color='#38bdf8', fill=True, alpha=0.15)
    ax.add_patch(circle)

ax.text(0.67, 0.10, "Mapa Base: CARTO Dark / OpenStreetMap\nCRS: EPSG:4326 (WGS 84)", color='#94a3b8', fontsize=7, ha='center')

ax.set_title("Prototipo de Interfaz Web Cartográfica para Apoyo a Decisiones", fontweight='bold', fontsize=11)
plt.tight_layout()
fig6_path = os.path.join(OUTPUT_DIR, "fig_6_interfaz_prototipo.png")
plt.savefig(fig6_path, dpi=300)
plt.close()
print(f"Guardada: {fig6_path}")

print("Todas las figuras han sido generadas exitosamente en la carpeta 'figuras/'.")
