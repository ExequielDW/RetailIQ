import src.loader as lo
import src.analizer as an
import src.reporter as repor

df2 = lo.carga_de_datos()
df2 = an.ganancia_x_transaccion(df2)
vendedores = an.ranking_vendedores(df2)
mejor_region = an.mejor_vendedor_por_region(df2)
repor.generar_reporte(df2, vendedores, mejor_region)
