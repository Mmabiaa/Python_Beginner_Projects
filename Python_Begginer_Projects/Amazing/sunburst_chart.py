import plotly.graph_objects as go

labels = ["Root", "Branch 1","Branch 2", "Leaf 1", "Leaf 2", "Leaf 3"]

parents = ['', "Root","Root", "Branch 1", "Branch 1", "Branch 2"]

values = [10, 5, 5, 2, 3, 5]

fig = go.Figure(go.Sunburst(labels=labels, 
parents=parents, 
values=values, 
branchvalues="total" ))

fig. update_layout(
title="Sunburst Chart in Python", 
margin=dict (t=30, l=0, r=0, b=0))

fig. show()
