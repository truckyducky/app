import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
from pyvis.network import Network
from IPython.core.display import display, HTML

net = Network(notebook = True, cdn_resources="remote",height="900px", width="90%", select_menu = True, filter_menu=True,font_color="white", bgcolor = "black")


net.add_node('Node 16 - Demographics - Adult, Revised [Demographics-A Revised]',  
              title = 'Demographics - Adult, Revised [Demographics-A Revised]', color = '#e07c3e')


net.add_nodes(['Node 65 - PAINED: Project Addressing INequities in the Emergency Department'],
    label = ['PAINED: Project Addressing INequities in the Emergency Department'],
    title = ['PAINED: Project Addressing INequities in the Emergency Department'],
    shape = ['text']

)




net.add_edge('Node 16 - Demographics - Adult, Revised [Demographics-A Revised]', 'Node 65 - PAINED: Project Addressing INequities in the Emergency Department')
        

net.repulsion(spring_strength = 0)
net.show("edges.html")




# Save and read graph as HTML file (on Streamlit Sharing)
try:
    path = '/tmp'
    net.save_graph(f'{path}/pyvis_graph.html')
    HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')

# Save and read graph as HTML file (locally)
except:
    path = '/html_files'
    net.save_graph(f'{path}/pyvis_graph.html')
    HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')

# Load HTML file in HTML component for display on Streamlit page
components.html(HtmlFile.read(), height=1000, width = 1000)
