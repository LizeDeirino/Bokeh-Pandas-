#!/usr/bin/env python
# coding: utf-8

# In[11]:


from bokeh.plotting import figure
from bokeh.io import output_file, show

x=[1,2,3,4,5]
y=[6,7,8,9,10]

output_file("Line.html")

f=figure()

f.line(x,y)

show(f)


# In[12]:


from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas


df=pandas.read_csv('data.csv')
x=df["x"]
y=df["y"]

output_file("Line_from_csv.html")

f=figure()

f.line(x,y)

show(f)


# In[29]:


from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df=pandas.read_excel('verlegenhuken.xlsx')
x=df["Temperature"]
y=df["Pressure"]

output_file("CircleTempPressure.html")

f=figure(plot_width=500, plot_height=400, tools='pan')

f.title.text="Temperature and Air Pressure"
f.xaxis.axis_label="Temperature (°C)"
f.yaxis.axis_label="Pressure (hPa)"  

f.circle(x/10,y/10,size=0.5)

show(f)


# In[13]:


from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df=pandas.read_csv('bachelors.csv')
x=df["Year"]
y=df["Engineering"]

output_file("Line_from_bachelors.html")

f=figure()

f.line(x,y)

show(f)


# In[18]:


import pandas
from bokeh.plotting import figure, output_file, show
 
p=figure(plot_width=500, plot_height=400, tools='pan')
 
p.title.text="Cool Data"
p.title.text_color="Gray"
p.title.text_font="times"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Date"
p.yaxis.axis_label="Intensity"    
 
p.line([1,2,3],[4,5,6])
output_file("graph.html")
show(p)

