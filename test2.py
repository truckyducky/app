#setting up packages
import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
from pyvis.network import Network


#setup network
net = Network(notebook = True, cdn_resources="remote",height="900px", width="90%", select_menu = True, filter_menu=True,font_color="white", bgcolor = "#373a3c", heading = "Interactive Network of HEAL Core CDEs")


#add categorical/subcategorical nodes
net.add_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    label = ['General Health',
             'Patient Health',
             'Pain',
             'Sleep',
             'Substance Use',
             'Mental Health',
             'Quality of Life',
             'Demographics', 
             'Adults', 
             'Adolescent', 
             'Pediatric'],
    color = ['#982568', '#532565','#532565', '#532565', '#532565', '#532565', '#532565','#982568','#532565', '#532565','#532565'],
    size = [60, 30, 30 ,30, 30, 30, 60, 30, 30, 30, 30],
    shape = ['ellipse','ellipse','ellipse','ellipse','ellipse','ellipse','ellipse','ellipse','ellipse','ellipse','ellipse']

)

#adding nodes about common CDEs

net.add_nodes([12, 13, 14, 15, 16, 17, 18, 19, 20, 21,22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35],
    label = ['Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]', 
             'Brief Pain Inventory - Interference [BPI-Interference]',
             'Brief Pain Inventory - Severity [BPI-Severity]',
             'Demographics - Adult [Demographics-A]',
             'Demographics - Adult, Revised [Demographics-A Revised]',
             'Demographics - Pediatric [Demographics-Peds]',
             'Demographics - Pediatric, revised [Demographics-Peds Revised]',
             'Generalized Anxiety Disorder - 2 Items [GAD-2]', 
             'Generalized Anxiety Disorder - 7 Items [GAD-7]',
             'NIDA Modified Assist Tool - 2 [NIDA Assist-2 Modified]',
             'Pain Catastrophizing Questionnaire - 13 Items [PCS-13]', 
             'Pain Catastrophizing Scale - Parent [PCS-Parent]',
             'Pain Catastrophizing Scale - Pediatric [PCS-Peds]',
             'Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]',
             'Pain, Enjoyment, General Activity [PEG]',
             'Patient Global Impression of Change [PGIC]',
             'Patient Health Questionnaire - 2 items [PHQ-2]',
             'Patient Health Questionnaire - 8 Items [PHQ-8]',
             'Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]',
             'Pediatric Quality of Life Inventory [PedsQL]',
             'PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]',
             'PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]',
             'Sleep Duration Question [SD - Adult or Peds]',
             'Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]'],
    color = ['#e07c3e', '#e07c3e','#e07c3e', '#e07c3e', '#e07c3e', '#e07c3e', '#e07c3e','#e07c3e','#e07c3e', '#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e'],
    size = [20, 40, 40, 60, 20, 20, 20, 40, 40, 20, 40, 20, 20, 40, 60, 60, 40, 20, 20, 20, 60, 60, 60, 60]
)

#adding connections

net.add_edges([
    (1,2),(1,3),(1,4),(1,5),(1,6),(1,7),
    (2,28),(2,29),(2,30),
    (3,13),(3,14),(3,22),(3,23),(3,24),(3,25),
    (4,12),(4,33),(4,34),
    (5, 21),(5, 35),
    (6, 19),(6,20),(6,27),
    (7, 31),(7,26),
    (8, 9),(8, 10),(8,11),
    (9, 15),(9, 16),(9,23),
    (10, 12),
    (11, 17),(11,18),
    (12,4),(11,24),
    
]
)

#adding the research programs
net.add_node(36, label='Biomarkers', color = '#532565', shape = 'triangle', size = 25)
net.add_node(37, label = 'ERN', color = '#532565', shape = 'triangle', size = 25)
net.add_node(38, label = 'Health Equity in Pain Management', color = '#532565', shape = 'triangle', size = 25)
net.add_node(39, label = 'A2CPS', color = '#532565', shape = 'triangle', size = 15)
net.add_node(40, label = 'BACPAC', color = '#532565', shape = 'triangle', size = 20)
net.add_node(41, label = 'IMPOWR', color = '#532565', shape = 'triangle', size = 20)
net.add_node(42, label = 'Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief', color = '#532565', shape = 'triangle', size = 20)
net.add_node(43, label = 'MPS- Myofascial Pain', color = '#532565', shape = 'triangle', size = 20)
net.add_node(44, label = 'PRECISION Human Pain', color = '#532565', shape = 'triangle', size = 15)
net.add_node(45, label = 'PRISM', color = '#532565', shape = 'triangle', size = 20)
net.add_node(46, label = 'HOPE', color = '#532565', shape = 'triangle', size = 15)
net.add_node(47, label = 'EPPIC Net', color = '#532565', shape = 'triangle', size = 15)
net.add_node(48, label = 'RE JOIN', color = '#532565', shape = 'triangle', size = 15)
net.add_node(49, label = 'Research Programs', color = '#982568', shape = 'ellipse')


net.show("edges.html")

# Save and read graph as HTML file (on Streamlit Sharing)
try:
    path = '/tmp'
    drug_net.save_graph(f'{path}/pyvis_graph.html')
    HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')

# Save and read graph as HTML file (locally)
except:
    path = '/html_files'
    drug_net.save_graph(f'{path}/pyvis_graph.html')
    HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')

# Load HTML file in HTML component for display on Streamlit page
components.html(HtmlFile.read(), height=435)
