import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd
st.header('Homework 1')
st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)
st.code(
'''
x_limit =
# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange()
# Create a random array of data that we will use for our y values
y_data = []
df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)''',language='python')
x_limit=100
x_axis=np.arange(start=0, stop=x_limit, step=1)
y_data = [random.random() for value in x_axis]
df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)
st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)
st.code(
'''
scatter = alt.Chart().mark_point().encode()
st.altair_chart(scatter, use_container_width=True)''',language='python')
scatter = alt.Chart(data=df).mark_point().encode(x='x',y='y')
st.altair_chart(scatter, use_container_width=True)
st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)
scatter1 = alt.Chart(data=df).mark_point(size=60,opacity=0.5, color='red').encode(x='x',y='y',
    tooltip=['x', 'y'])
scatter1.configure_header(
    titleColor='green',
    titleFontSize=14,
    labelColor='red',
    labelFontSize=14
)
st.altair_chart(scatter1, use_container_width=True)
st.markdown("The five changes I made were.....")
st.markdown("""
The 5 changes I made were:
- Changed the size of the point
- Added a tool tip
- made the color red
- changed the opacity to 50%
- title
""")
st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)
st.markdown("""
The 2 changes I made were:
- Change 1
- Change 2
"""
)
