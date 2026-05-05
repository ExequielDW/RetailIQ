# RetailIQ — Sales Performance Analyzer

> Análisis de performance de ventas, rentabilidad por producto y ranking de vendedores por región.  
> Sales performance analysis, product profitability and vendor ranking by region.

---

## 🇦🇷 Español

### Descripción

RetailIQ es una herramienta de análisis de datos de ventas desarrollada en Python. Procesa datos de vendedores, productos y transacciones para generar reportes de rentabilidad, rankings de performance y resúmenes exportables.

### Tecnologías

- Python 3.x
- Pandas
- CSV / TXT (persistencia de datos y reportes)
- Arquitectura modular (src/)

### Estructura del proyecto

```
RetailIQ/
├── data/
│   ├── vendedores.csv
│   ├── productos.csv
│   └── ventas.csv
├── output/
│   ├── reporte_final.csv
│   └── resumen.txt
├── src/
│   ├── loader.py       # Carga y merge de datos
│   ├── analyzer.py     # Cálculo de ganancias y rankings
│   └── reporter.py     # Generación de reportes
├── main.py
└── README.md
```

### Cómo ejecutarlo

```bash
# Clonar el repositorio
git clone https://github.com/ExequielDW/RetailIQ.git
cd RetailIQ

# Instalar dependencias
pip install pandas

# Ejecutar
python main.py
```

### Output generado

- `output/reporte_final.csv` — Dataset completo con ganancia por transacción
- `output/resumen.txt` — Highlights: mejor vendedor general y mejor vendedor por región

### Funcionalidades

- Merge de tres fuentes de datos (vendedores, ventas, productos)
- Cálculo de ganancia por transacción `(precio_unitario - costo) * cantidad`
- Ranking de vendedores por ganancia total
- Mejor vendedor por región
- Exportación de reporte en CSV y resumen en TXT
- Manejo de errores para archivos inexistentes

---

## 🇺🇸 English

### Description

RetailIQ is a sales data analysis tool built in Python. It processes vendor, product and transaction data to generate profitability reports, performance rankings and exportable summaries.

### Tech Stack

- Python 3.x
- Pandas
- CSV / TXT (data persistence and reporting)
- Modular architecture (src/)

### How to Run

```bash
# Clone the repository
git clone https://github.com/ExequielDW/RetailIQ.git
cd RetailIQ

# Install dependencies
pip install pandas

# Run
python main.py
```

### Output

- `output/reporte_final.csv` — Full dataset with profit per transaction
- `output/resumen.txt` — Highlights: top vendor overall and top vendor per region

### Features

- Merge of three data sources (vendors, sales, products)
- Profit per transaction calculation `(unit_price - cost) * quantity`
- Vendor ranking by total profit
- Top vendor per region
- CSV report and TXT summary export
- Error handling for missing files

---

## Autor / Author

**Exequiel** — [@ExequielDW](https://github.com/ExequielDW)
