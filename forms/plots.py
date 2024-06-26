import plotly.graph_objs as go
from plotly.offline import plot


def plot_piechart(names, values):
    """

    :param names: param values:
    :param title: param values:
    :param values:

    """
    fig = go.Figure(data=go.Pie(name="PieChart", values=values, labels=names))

    fig.update_layout(
        autosize=False,
        width=1000,
        height=400,
        title_text="",
        template="seaborn",
        margin=dict(l=40, r=20, t=30, b=40),
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white"),
        title=dict(font=dict(size=30),
                   x=0.47,
                   y=0.95,
                   xanchor="center",
                   yanchor="middle"),
    )

    piechart = plot({"data": fig}, output_type="div")
    return piechart
