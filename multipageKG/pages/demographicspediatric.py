import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
from pyvis.network import Network
from IPython.core.display import display, HTML

net = Network(notebook = True, cdn_resources="remote",height="900px", width="90%", select_menu = True, filter_menu=True,font_color="white", bgcolor = "black")


net.add_node('Node 17 - Demographics - Pediatric [Demographics-Peds]',  
              title = 'Demographics - Pediatric [Demographics-Peds]', color = '#e07c3e')


net.add_nodes(['Node 50 - SPRINT: Signature for Pain Recovery IN Teens','Node 51 - SurgeryPal', 
               'Node 52 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma', 'Node 53 - Integrative Training Program for Pediatric Sickle Cell Pain',
               'Node 54 - Latinx Children and Surgery'],
    label = ['SPRINT: Signature for Pain Recovery IN Teens', 'SurgeryPal', 'Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma', 
             'Integrative Training Program for Pediatric Sickle Cell Pain', 'Latinx Children and Surgery'],
    title = ['SPRINT: Signature for Pain Recovery IN Teens', 'SurgeryPal', 'Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma', 
             'Integrative Training Program for Pediatric Sickle Cell Pain', 'Latinx Children and Surgery'],
    shape = ['text', 'text', 'text', 'text','text']

)


net.add_edge('Node 17 - Demographics - Pediatric [Demographics-Peds]','Node 50 - SPRINT: Signature for Pain Recovery IN Teens') 
net.add_edge('Node 17 - Demographics - Pediatric [Demographics-Peds]','Node 51 - SurgeryPal')
net.add_edge('Node 17 - Demographics - Pediatric [Demographics-Peds]','Node 52 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma')  
net.add_edge('Node 17 - Demographics - Pediatric [Demographics-Peds]','Node 53 - Integrative Training Program for Pediatric Sickle Cell Pain')
net.add_edge('Node 17 - Demographics - Pediatric [Demographics-Peds]','Node 54 - Latinx Children and Surgery')
        

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
