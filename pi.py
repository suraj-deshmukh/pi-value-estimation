from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from bokeh.plotting import figure
import numpy as np

p = figure(plot_height=400, plot_width=400, tools="pan,reset,save",x_range=[-1,1], y_range=[-1,1])
p.circle([0], [0], radius=1.0,radius_dimension = 'x', radius_units='screen',alpha=0.5)
x = np.random.uniform(-1,1,size=100)
y = np.random.uniform(-1,1,size=100)
tmp = x**2 + y**2
index = np.where(tmp <= 1.0)[0]
n_zero = len(index)
pi = str((4 * n_zero)/100.0)
color = np.array(['green' if i in index else 'red' for i in range(100)])
source = ColumnDataSource(data=dict(x=x, y=y,color=color))
p.scatter('x', 'y', source=source,color='color')

N = Slider(title="Sample Points", value=100, start=100, end=10000, step=10)
PI = TextInput(title="Estimated Pi Value", value=pi)

def estimate_pi(attrname, old, new):
    n = N.value
    x = np.random.uniform(-1,1,size=n)
    y = np.random.uniform(-1,1,size=n)
    tmp = x**2 + y**2
    index = np.where(tmp <= 1.0)[0]
    color = np.array(['green' if i in index else 'red' for i in range(n)])
    source.data = dict(x=x, y=y,color=color)
    n_zero = len(index)
    pi = str((4.0 * n_zero)/n)
    PI.value = pi


N.on_change('value',estimate_pi)

inputs = widgetbox(PI, N)

curdoc().add_root(row(inputs, p))
curdoc().title = "Pi Value Estimation"