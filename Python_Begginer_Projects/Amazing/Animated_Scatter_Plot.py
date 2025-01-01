import plotly.express as px

data = px.data.gapminder()

fig = px.scatter(
    data,
    x='gdpPercap',
    y='lifeExp',
    animation_frame='year',
    animation_group='country',
    size='pop',
    color='continent',
    hover_name='country',
    log_x=True,
    size_max=60,
    range_x=[200,600],
    range_y=[20, 90],
    title='Animated Scatter Plot: Life Expectancy vs GDP Per Capita'
)
fig.show()
# Author - Mmabiaa
