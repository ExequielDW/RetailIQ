import pandas as pd


def carga_de_datos():
    try:
        df = pd.read_csv("data/vendedores.csv")
        df1 = pd.read_csv("data/productos.csv")
        df2 = pd.read_csv("data/ventas.csv")
        df2 = pd.merge(df2, df, left_on="id_vendedor", right_on="id")
        df2 = pd.merge(df2, df1, on="producto")
        print(df2.to_string())
        return df2
    except FileNotFoundError:
        print("Archivo no encontrado o ruta invalida")
