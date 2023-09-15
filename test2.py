#setting up packages
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network


#setup network
st.title("Interactive Network of HEAL Core CDEs")  
net = Network(notebook = True, cdn_resources="remote",height="800px", width="100%", select_menu = True, filter_menu=True,font_color="white", bgcolor = "#373a3c")


#add categorical/subcategorical nodes
net.add_nodes(['1 - General Health', 
               '2 - Patient Health', 
               '3 - Pain',  
               '4 - Sleep', 
               '5 - Substance Use', 
               '6 - Mental Health',
               '7 - Quality of Life',
               '8 - Demographics', 
               '9 - Adults', 
               '10 - Adolescent', 
               '11 - Pediatric'],
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

#adding nodes about common CDEs 12-35
net.add_nodes(['12 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]', 
             '13 - Brief Pain Inventory - Interference [BPI-Interference]',
             '14 - Brief Pain Inventory - Severity [BPI-Severity]',
             '15 - Demographics - Adult [Demographics-A]',
             '16 - Demographics - Adult, Revised [Demographics-A Revised]',
             '17 - Demographics - Pediatric [Demographics-Peds]',
             '18 - Demographics - Pediatric, revised [Demographics-Peds Revised]',
             '19 - Generalized Anxiety Disorder - 2 Items [GAD-2]', 
             '20 - Generalized Anxiety Disorder - 7 Items [GAD-7]',
             '21 - NIDA Modified Assist Tool - 2 [NIDA Assist-2 Modified]',
             '22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]', 
             '23 - Pain Catastrophizing Scale - Parent [PCS-Parent]',
             '24 - Pain Catastrophizing Scale - Pediatric [PCS-Peds]',
             '25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]',
             '26 - Pain, Enjoyment, General Activity [PEG]',
             '27 - Patient Global Impression of Change [PGIC]',
             '28 - Patient Health Questionnaire - 2 items [PHQ-2]',
             '29 - Patient Health Questionnaire - 8 Items [PHQ-8]',
             '30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]',
             '31 - Pediatric Quality of Life Inventory [PedsQL]',
             '32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]',
             '33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]',
             '34 - Sleep Duration Question [SD - Adult or Peds]',
             '35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]'],
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
    ('1 - General Health','2 - Patient Health'), 
    ('1 - General Health','3 - Pain'),
    ('1 - General Health','4 - Sleep'),
    ('1 - General Health','5 - Substance Use'),
    ('1 - General Health','6 - Mental Health'),
    ('1 - General Health','7 - Quality of Life'),
    ('2 - Patient Health', '28 - Patient Health Questionnaire - 2 items [PHQ-2]'),
    ('2 - Patient Health','29 - Patient Health Questionnaire - 8 Items [PHQ-8]'),
    ('2 - Patient Health','30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]'),
    ('3 - Pain','13 - Brief Pain Inventory - Interference [BPI-Interference]'),
    ('3 - Pain','14 - Brief Pain Inventory - Severity [BPI-Severity]'),
    ('3 - Pain','22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]'),
    ('3 - Pain','23 - Pain Catastrophizing Scale - Parent [PCS-Parent]'),
    ('3 - Pain','24 - Pain Catastrophizing Scale - Pediatric [PCS-Peds]'),
    ('3 - Pain','25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]'),
    ('4 - Sleep','12 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]'),
    ('4 - Sleep','33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]'),
    ('4 - Sleep','34 - Sleep Duration Question [SD - Adult or Peds]'),
    ('5 - Substance Use', '21 - NIDA Modified Assist Tool - 2 [NIDA Assist-2 Modified]'),('5 - Substance Use', '35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]'),
    ('6 - Mental Health', '19 - Generalized Anxiety Disorder - 2 Items [GAD-2]'),('6 - Mental Health','20 - Generalized Anxiety Disorder - 7 Items [GAD-7]'),('6 - Mental Health','27 - Patient Global Impression of Change [PGIC]'),
    ('7 - Quality of Life', '31 - Pediatric Quality of Life Inventory [PedsQL]'),('7 - Quality of Life','26 - Pain, Enjoyment, General Activity [PEG]'),
    ('8 - Demographics', '9 - Adults'),('8 - Demographics', '10 - Adolescent'),('8 - Demographics','11 - Pediatric'),
    ('9 - Adults', '15 - Demographics - Adult [Demographics-A]'),('9 - Adults', '16 - Demographics - Adult, Revised [Demographics-A Revised]'),('9 - Adults','23 - Pain Catastrophizing Scale - Parent [PCS-Parent]'),
    ('10 - Adolescent', '12 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]'),
    ('11 - Pediatric', '17 - Demographics - Pediatric [Demographics-Peds]'),('11 - Pediatric','18 - Demographics - Pediatric, revised [Demographics-Peds Revised]'),
    ('12 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]','4 - Sleep'),('11 - Pediatric','24 - Pain Catastrophizing Scale - Pediatric [PCS-Peds]'),
    
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

# adding connections for third subcategory "research programs" to each research program
net.add_edges([
    (49,36),(49,37),(49,38),(49,39),(49,40),(49,41),(49,42),(49,43),(49,44),(49,45),(49,46),(49,47),(49,48),])



#adding connections for the research programs to CDEs

net.add_edges([
    (12,36),(12,37),(12,38),
    (13,36),(13,37),(13,38),(13,39),(13,40),(13,41),(13,42),(13,43),(13,44),(13,45),
    (14,36),(14,37),(14,38),(14,39),(14,40),(14,41),(14,42),(14,43),(14,44),(14,45),
    (15,36),(15,37),(15,38),(15,39),(15,40),(15,41),(15,42),(15,43),(15,44),(15,45),(15,46),(15,47),(15,48),
    (16,38),
    (17,36),(17,37),(17,38),
    (18,38),
    (19,36),(19,37),(19,38),(19,40),(19,41),(19,42),(19,43),(19,44),(19,45),(19,47),(19,48),
    (20,36),(20,37),(20,38),(20,39),(20,40),(20,41),(20,42),(20,43),(20,45),(20,46),(20,48),
    (21,36),(21,37),(21,38),
    (22,36),(22,37),(22,38),(22,40),(22,41),(22,42),(22,43),(22,45),(22,48),
    (23,36),(23,37),(23,38),
    (24,36),(24,37),(24,38),
    (25,36),(25,37),(25,38),(25,39),(25,40),(25,41),(25,42),(25,43),(25,44),(25,45),(25,46),(25,47),(25,48),
    (26,36),(26,37),(26,38),(26,39),(26,40),(26,41),(26,42),(26,43),(26,44),(26,45),(26,46),(26,47),(26,48),
    (27,36),(27,37),(27,38),(27,39),(27,40),(27,41),(27,42),(27,43),(27,44),(27,45),(27,46),(27,47),(27,48),
    (28,36),(28,37),(28,38),(28,40),(28,41),(28,42),(28,43),(28,44),(28,45),(28,47),(28,48),
    (29,37),(29,38),(29,39),(29,43),(29,45),(29,48),
    (30,36),(30,37),(30,40),(30,41),(30,42),(30,43),(30,45),(30,46),(30,48),
    (31,36),(31,37),(31,38),
    (32,36),(32,37),(32,38),(32,39),(32,40),(32,41),(32,42),(32,43),(32,44),(32,45),(32,46),(32,47),(32,48),
    (33,36),(33,37),(33,38),(33,39),(33,40),(33,41),(33,42),(33,43),(33,44),(33,45),(33,46),(33,47),(33,48),
    (34,36),(34,37),(34,38),(34,39),(34,40),(34,41),(34,42),(34,43),(34,44),(34,45),(34,46),(34,47),(34,48),   
    (35,36),(35,37),(35,38),(35,39),(35,40),(35,41),(35,42),(35,43),(35,44),(35,45),(35,46),(35,47),(35,48),   
]
)
cde_list = ['Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]', 
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
             'Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]']

# Implement multiselect dropdown menu for option selection (returns a list)
selected_cdes = st.multiselect('Select HEAL Common Core CDEs to visualize', cde_list)


# Set info message on initial site load
if len(selected_cdes) == 0:
    st.text('Choose at least 1 drug to start')


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
