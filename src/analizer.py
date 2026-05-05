import loader as lo


def ganancia_x_transaccion(df2):
    df2["ganancia_total"] = (df2["precio_unitario"] - df2["costo"]) * df2["cantidad"]
    print(df2)
    return df2


def ranking_vendedores(df2):
    print("Este es el ranking de vendedores")
    vendedores = (
        df2.groupby("nombre")["ganancia_total"].sum().sort_values(ascending=False)
    )
    print(vendedores)
    return vendedores


def mejor_vendedor_por_region(df2):
    mejor_por_region = df2.groupby(["region", "nombre"])["ganancia_total"].sum()
    idx = mejor_por_region.groupby("region").idxmax()
    print(mejor_por_region.loc[idx])
    return mejor_por_region


if __name__ == "__main__":
    df2 = lo.carga_de_datos()
    df2 = ganancia_x_transaccion(df2)
    ranking_vendedores(df2)
    mejor_vendedor_por_region(df2)
