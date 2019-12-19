# PLOTLY

# BAHAN BELAJAR : http://plot.ly/python
# install plotly : py -m pip install plotly

import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = 'browser'
import numpy as np 
import pandas as pd 

x = np.array([1,2,3,4,5])
y = np.array([2,1,4,1,3])

myFig = go.Figure(
    data = go.Bar(x=x, y=y)
)

# myFig.show()

#buat nembak ke html
myFig.write_html('PlotlyTes.html', auto_open=True)
myFig.show()