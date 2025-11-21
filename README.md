 
Sistema de Gestión de Biblioteca Universitaria
Estudiante: Mateo Arroyave
Fecha: 21/11/2025 
Métrica	Valor	Estado
Tiempo Total	1,375 min (22.9 hrs)	✅ Completado
LOC Producidas	1,000 líneas	✅ Meta cumplida
Defectos	12 encontrados	⚠️ Controlado
Productividad	43.6 LOC/hora	✅ Excelente
Calidad (Yield)	58.3%	⚠️ Mejorable

 DISTRIBUCIÓN DEL TIEMPO
Tabla: Tiempo por Fase
Fase	Planeado	Real	Diferencia	% del Total
Planificación	60 min	90 min	+50%	6.5%
Diseño	180 min	210 min	+17%	15.3%
Codificación	480 min	660 min	+38%	48.0%
Compilación	20 min	25 min	+25%	1.8%
Pruebas	240 min	360 min	+50%	26.2%
Postmortem	30 min	30 min	0%	2.2%
TOTAL	1,010 min	1,375 min	+36%	100%


Interpretación:
•	Codificación: Consumió casi la mitad del tiempo (48%), normal para desarrollo
•	Pruebas: 26.2% del tiempo, proporción adecuada
•	Error de estimación: +36% indica que subestimamos el proyecto
•	Mayor desviación: Codificación y Pruebas (ambos +38% y +50%)

REGISTRO DE DEFECTOS
Tabla: Defectos por Tipo
Tipo	Cantidad	%	Tiempo Corrección	Costo Promedio
Lógica	3	25%	80 min	26.7 min
Sintaxis	2	16.7%	8 min	4 min
Interfaz	2	16.7%	60 min	30 min
Datos	2	16.7%	45 min	22.5 min
Función	1	8.3%	45 min	45 min
Documentación	1	8.3%	10 min	10 min
Ambiente	1	8.3%	12 min	12 min
TOTAL	12	100%	260 min	21.7 min

Interpretación:
•	Defectos de lógica son los más frecuentes (25%) y costosos (80 min total)
•	Defectos de sintaxis son rápidos de corregir (4 min promedio)
•	Tiempo total en correcciones: 260 minutos (19% del tiempo total)
•	Costo promedio: 21.7 minutos por defecto

DEFECTOS POR FASE
Tabla: Dónde se Crearon y Removieron
Fase	Defectos Inyectados	Defectos Removidos	Eficiencia
Planificación	0	0	-
Diseño	4 (33%)	0	0%
Codificación	8 (67%)	0	0%
Compilación	0	2 (17%)	100%
Pruebas	0	9 (75%)	100%
Postmortem	0	1 (8%)	100%

•	67% de defectos se crearon durante la Codificación
•	75% de defectos se descubrieron en Pruebas (tarde)
•	Solo 17% se encontró en Compilación (temprano)
•	Problema: Los defectos llegan muy tarde al ciclo

 MÉTRICAS DE PRODUCTIVIDAD
Tabla: Eficiencia del Desarrollo
Métrica	Fórmula	Valor	Interpretación
LOC/Hora	1000 / (1375/60)	43.6	✅ Excelente (meta: >30)
Min/LOC	1375 / 1000	1.38	Tiempo por línea
Eficiencia Tiempo	(1010/1375)×100	73.5%	⚠️ Subestimación del 26.5%


 Interpretación:
•	Alta productividad: 43.6 líneas por hora supera estándares
•	Estimación mejorable: Proyecto tomó 36% más tiempo del estimado
•	Recomendación: En próximos proyectos, agregar 40% más tiempo

 MÉTRICAS DE CALIDAD
Tabla: Indicadores de Calidad
Métrica	Fórmula	Valor	Meta PSP	Estado
Defectos/KLOC	(12/1000)×1000	12.0	<10	⚠️ No cumple
Yield	((12-5)/12)×100	58.3%	>70%	⚠️ No cumple
Tiempo/Defecto	260/12	21.7 min	<20	⚠️ Aceptable
 Interpretación:
•	Yield bajo (58.3%): Solo 42% de defectos se encontraron antes de Pruebas
•	Densidad alta (12/KLOC): Más defectos de lo recomendado
•	Acción: Implementar revisiones de código más frecuentes
 DASHBOARD DE EVALUACIÓN
Tabla: Cumplimiento de Objetivos PSP
Indicador	Valor Actual	Meta	¿Cumple?	Acción Requerida
Defectos/KLOC	12.0	<10	❌	Mejorar revisiones de código
Yield (%)	58.3	>70	❌	Detectar defectos más temprano
LOC/Hora	43.6	>30	✅	Mantener productividad
Eficiencia	73.5%	>80	⚠️	Mejorar estimaciones (+40%)
				

ANÁLISIS DE CAUSAS
¿Por qué el Yield es bajo?
Causa	Impacto	Solución
No hay revisiones de diseño	Alto	Implementar checklists de diseño
No se compila frecuentemente	Medio	Compilar cada 50 LOC
Falta revisión de código	Alto	Revisar antes de cada commit
Pruebas al final	Alto	Hacer pruebas unitarias continuas

 LECCIONES APRENDIDAS
Lo que funcionó 
1.	Alta productividad: 43.6 LOC/hora
2.	Buena proporción de pruebas: 26% del tiempo
3.	Documentación completa: Postmortem realizado
4.	Proyecto completado: Todas las funcionalidades
Lo que debe mejorar ⚠️
1.	Yield bajo: Solo 58.3% vs meta 70%
2.	Estimaciones: Subestimamos 36%
3.	Defectos de lógica: 25% del total
4.	Detección tardía: 75% en pruebas




 PLAN DE ACCIÓN PARA PRÓXIMO PROYECTO
Mejoras Específicas
#	Acción	Objetivo	Métrica a Mejorar
1	Compilar cada 50 LOC	Encontrar errores sintaxis temprano	Yield +10%
2	Revisar diseño con checklist	Reducir defectos lógicos	Defectos -3
3	Estimar +40% en Codificación	Mejorar precisión	Eficiencia >80%
4	Pruebas unitarias continuas	Detectar defectos antes	Yield >70%
5	Revisión de código antes de commit	Reducir defectos/KLOC	<10 defectos

COMPARACIÓN CON ESTÁNDARES
Tabla: Tu Desempeño vs Industria
Métrica	Tu Valor	Junior	Intermedio	Senior	Tu Nivel
LOC/Hora	43.6	20-30	30-50	50-70	Senior ✅
Defectos/KLOC	12.0	15-25	10-15	5-10	Intermedio ⚠️
Yield	58.3%	40-50%	50-70%	70-85%	Intermedio ⚠️
 Conclusión:
•	Productividad: Nivel Senior
•	Calidad: Nivel Intermedio
•	Objetivo: Mantener productividad y subir calidad a Senior
________________________________________
 DATOS DEL PROYECTO
Información General
Proyecto:      Sistema de Gestión de Biblioteca Universitaria
Estudiante:    Mateo Arroyave
Metodología:   PSP 0.1 (Personal Software Process)
Lenguaje:      Python 3 + Flask
Base de Datos: SQLite
Líneas:        1,000 LOC
Duración:      7 días (05/11 - 12/11/2025)
Tiempo:        1,375 minutos (22.9 horas)
Defectos:      12 encontrados y corregidos
________________________________________
1️⃣2️⃣ VALOR DEL PROYECTO
Métricas de Valor
Concepto	Valor
Funcionalidades completas	6 módulos
Código producido	1,000 LOC
Documentación	Completa (PSP)
Calidad del código	88% sin defectos
Tiempo invertido	23 horas
Valor educativo	Alto (aprendizaje PSP)
________________________________________
📈 CONCLUSIONES FINALES
Resumen en 3 Puntos
1.	✅ Productividad Excelente
o	43.6 LOC/hora supera estándares profesionales
o	Desarrollo eficiente y rápido
2.	⚠️ Calidad Mejorable
o	Yield 58.3% indica detección tardía de defectos
o	Necesita más revisiones tempranas
3.	📊 Estimación por Mejorar
o	Error del 36% en tiempo estimado
o	Próximos proyectos: agregar 40% buffer
Calificación General: 7.5/10
________________________________________
🎯 OBJETIVOS PARA SIGUIENTE PROYECTO
Métrica	Valor Actual	Meta Próxima	Mejora
Yield	58.3%	70%	+11.7%
Defectos/KLOC	12.0	<10	-2 defectos
Eficiencia	73.5%	>85%	+11.5%
LOC/Hora	43.6	>40	Mantener
________________________________________
📝 RECOMENDACIÓN FINAL
Este proyecto demuestra alta capacidad técnica (productividad senior) pero necesita mejorar procesos de calidad (revisiones tempranas).
Siguiente paso: Implementar revisiones de código y compilaciones frecuentes para elevar el Yield al 70%+.
________________________________________
Informe generado: 15/11/2025
Metodología: PSP 0.1
Estudiante: Mateo Arroyave
Estado: ✅ Proyecto Exitoso

