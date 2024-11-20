import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file('Python_Begginer_Projects/Amazing/ne_110m_admin_0_countries.shp')
# main function to display the map
world.plot(edgecolor='red')
plt.title('World Map with Country Borders')
plt.show()
