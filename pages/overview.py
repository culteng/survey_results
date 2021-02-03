import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib
import glob

from . import analysis

filenames = glob.glob("/wd/pages/data/cleaned/*.csv")
df = analysis.populate_df(filenames)

########### GROUP HIST
x0 = df[df['ethnicity']=='b']['scl_happy']
x1 = df[df['ethnicity']=='l']['scl_happy']

figgy_hist = go.Figure()
figgy_hist.add_trace(go.Histogram(
    x=x0,
    histnorm='percent',
    name='black', # name used in legend and hover labels
    marker_color='#dddddd',
    opacity=0.75
))
figgy_hist.add_trace(go.Histogram(
    x=x1,
    histnorm='percent',
    name='latina',
    marker_color='#97151c',
    opacity=0.75
))

figgy_hist.update_layout(
    title_text='Q 1.3 - Happiness?', # title of plot
    plot_bgcolor= "#fff", 
    xaxis_title_text='', # xaxis label
    yaxis_title_text='', # yaxis label
    bargap=0.2, # gap between bars of adjacent location coordinates
    bargroupgap=0.1, # gap between bars of the same location coordinates
    autosize=False,
    font={"family": "Raleway", "size": 10},
    height=200,
    hovermode="closest",
    legend={
        "x": -0.0228945952895,
        "y": -0.189563896463,
        "orientation": "h",
        "yanchor": "top",
    },
    margin={
        "r": 0,
        "t": 20,
        "b": 10,
        "l": 10,
    },
    showlegend=True,
    title="",
    width=330
)

############# group whisker
x0 = df[df['i_am_a']=='student']['scl_happy']
x1 = df[df['i_am_a']=='parent']['scl_happy']
x2 = df[df['i_am_a']=='teacher']['scl_happy']
x3 = df[df['i_am_a']=='staff']['scl_happy']

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_fund_facts = pd.read_csv(DATA_PATH.joinpath("df_fund_facts.csv"))
df_price_perf = pd.read_csv(DATA_PATH.joinpath("df_price_perf.csv"))


trace1 = {
          "uid": "676d10", 
          "line": {"color": "rgb(214, 39, 40)"}, 
          "name": "Students", 
          "type": "box", 
          "y": x0,
          "fillcolor": "rgba(214, 39, 40, 0.47)"
        }
trace2 = {
          "uid": "67abba", 
          "line": {"color": "rgb(100, 39, 40)"}, 
          "name": "Parents", 
          "type": "box", 
          "y": x1
        }
trace3 = {
          "uid": "88c7cc", 
          "line": {"color": "rgb(0, 39, 40)"}, 
          "name": "Teachers", 
          "type": "box", 
          "y": x2 
        }
trace4 = {
          "uid": "39976f", 
          "line": {"color": "rgb(31, 119, 180)"}, 
          "name": "Staff", 
          "type": "box", 
          "y": x3
        }
data_a = [trace1, trace2, trace3, trace4]
layout_a = {
          "font": {
            "size": 12, 
            "color": "rgb(0, 0, 0)", 
            "family": "'Open sans', verdana, arial, sans-serif"
          }, 
          "width": 300, 
          "xaxis": {
            "type": "category", 
            "dtick": 1, 
            "range": [-0.5, 4.5], 
            "tick0": 0, 
            "ticks": "", 
            "anchor": "y", 
            "domain": [0, 1], 
            "mirror": False, 
            "nticks": 0, 
            "ticklen": 5, 
            "position": 0, 
            "showgrid": False, 
            "showline": False, 
            "tickfont": {
              "size": 12, 
              "color": "rgb(255, 255, 255)"
            }, 
            "zeroline": False, 
            "autorange": True, 
            "gridcolor": "#eee", 
            "gridwidth": 1, 
            "linecolor": "#444", 
            "linewidth": 1, 
            "rangemode": "normal", 
            "tickangle": 90, 
            "tickcolor": "#444", 
            "tickwidth": 1, 
            "titlefont": {
              "size": 12, 
              "color": "rgb(255, 255, 255)"
            }, 
            "showexponent": "all", 
            "zerolinecolor": "#444", 
            "zerolinewidth": 1, 
            "exponentformat": "B", 
            "showticklabels": True
          }, 
          "yaxis": {
            "type": "linear", 
            "dtick": 10, 
            "range": [13.444444444444443, 104.55555555555556], 
            "tick0": 0, 
            "ticks": "", 
            "anchor": "x", 
            "domain": [0, 1], 
            "mirror": False, 
            "nticks": 0, 
            "ticklen": 5, 
            "position": 0, 
            "showgrid": True, 
            "showline": False, 
            "tickfont": {
              "size": 12, 
              "color": "rgb(255, 255, 255)"
            }, 
            "zeroline": True, 
            "autorange": True, 
            "gridcolor": "#eee", 
            "gridwidth": 1, 
            "linecolor": "#444", 
            "linewidth": 1, 
            "rangemode": "normal", 
            "tickangle": 90, 
            "tickcolor": "#444", 
            "tickwidth": 1, 
            "titlefont": {
              "size": 12, 
              "color": "rgb(255, 255, 255)"
            }, 
            "showexponent": "all", 
            "zerolinecolor": "#444", 
            "zerolinewidth": 1, 
            "exponentformat": "B", 
            "showticklabels": True
          }, 
          "bargap": 0.2, 
          "boxgap": 0.3, 
          "height": 200, 
          "legend": {
            "x": 1.02, 
            "y": 1, 
            "font": {
              "size": 12, 
              "color": "rgb(0, 0, 0)"
            }, 
            "bgcolor": "#fff", 
            "xanchor": "left", 
            "yanchor": "top", 
            "traceorder": "normal", 
            "bordercolor": "#444", 
            "borderwidth": 0
          }, 
          "margin": {
            "b": 8, 
            "l": 8, 
            "r": 8, 
            "t": 10, 
            "pad": 0, 
            "autoexpand": True
          }, 
          "barmode": "group", 
          "boxmode": "overlay", 
          "autosize": True, 
          "dragmode": "zoom", 
          "hovermode": "x", 
          "titlefont": {
            "size": 12, 
            "color": "rgb(255, 255, 255)"
          }, 
          "separators": ".,", 
          "showlegend": True, 
          "bargroupgap": 0, 
          "boxgroupgap": 0.3, 
          "hidesources": False, 
          "plot_bgcolor": "#fff"
        }
figgy = go.Figure(data=data_a, layout=layout_a)


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Product Summary"),
                                    html.Br([]),
                                    html.P(
                                        "\
                                    As the industry’s first index fund for individual investors, \
                                    the Calibre Index Fund is a low-cost way to gain diversified exposure \
                                    to the U.S. equity market. The fund offers exposure to 500 of the \
                                    largest U.S. companies, which span many different industries and \
                                    account for about three-fourths of the U.S. stock market’s value. \
                                    The key risk for the fund is the volatility that comes with its full \
                                    exposure to the stock market. Because the Calibre Index Fund is broadly \
                                    diversified within the large-capitalization market, it may be \
                                    considered a core equity holding in a portfolio.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Fund Facts"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_fund_facts)),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Response to Q3.2 by Ethnicity",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-1",
                                        figure=figgy_hist,
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Distribution of Responses by Demographic",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-2",
                                        figure=figgy,
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Price & Performance (%)",
                                        className="subtitle padded",
                                    ),
                                    html.Table(make_dash_table(df_price_perf)),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Risk Potential", className="subtitle padded"
                                    ),
                                    html.Img(
                                        src=app.get_asset_url("risk_reward.png"),
                                        className="risk-reward",
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
