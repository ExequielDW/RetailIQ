import src.analizer as an


def generar_reporte(df2, vendedores, mejor_region):
    df2.to_csv("output/reporte_final.csv", index=False)
    with open("output/resumen.txt", "w") as arch:
        arch.writelines(
            [
                "=== RESUMEN DE PERFOMANCE ===\n",
                f"Mejor vendedor general: {vendedores.idxmax()}\n",
                "Mejor por region:\n",
                f"{mejor_region}",
            ]
        )
