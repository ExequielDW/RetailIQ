import sys

sys.path.append("C:\\Users\\Exequiel\\Desktop\\RetailIQ\\src")

import loader as lo
import analizer as an
import reporter as repor

df2 = lo.carga_de_datos()
df2 = an.ganancia_x_transaccion(df2)
vendedores = an.ranking_vendedores(df2)
mejor_region = an.mejor_vendedor_por_region(df2)
repor.generar_reporte(df2, vendedores, mejor_region)
