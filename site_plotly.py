import plotly.express as px

dados_x = ["2020", "2021", "2022", "2023"]
dados_y = [10, 20, 5, 35]

fig = px.line(x=dados_x, y=dados_y, title="Primeiro gráfico usando plotly", width=600, height=400, line_shape="spline")

fig.show()