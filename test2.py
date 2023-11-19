#setting up packages
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network


#setup network
st.title("Interactive Network of HEAL Core CDEs")  

# Set info message on initial site load
multi = '''This dynamic tool is designed to help researchers intuitively comprehend HEAL CDE use interconnectedness and pertinence, allowing users to explore and understand the intricate relationships and patterns within each HEAL CDE.  
Understanding nodes: 
  - A “node” refers to the various shapes within the graph (circles, triangles, etc.) that visually represent specific information.  
  - Each node is like a data container - akin to a folder on your computer that stores files. These nodes, or “containers”, are interconnected, illustrating the relationships between different pieces of information.
Understanding edges: 
  - An “edge” refers to the line connection to the various shapes within the graph (circles, triangles, etc.) that visually represent specific information.  
  - Each edge is like a pathway linking the nodes to each other. The edge represents a relationship between different pieces of information. Note that there can be multiple relationships between various information leading to multiple pathway connections. 
Each core CDE is depicted as orange, circular nodes, varying in sizes. The size of the CDE name corresponds to the frequency of use - i.e. bigger circle indicates greater reported intended use. 
This knowledge graph categorizes the CDEs into three primary sectors - General Health, Demographics, and Research Programs, each depicted as magenta, ellipse-shaped nodes. 
  - Selecting a primary node will unfold a new set of subcategory nodes, each depicted as deep purple nodes. These subcategories are central connecting points, serving as central links between primary nodes and the specific CDEs.
      - General Health: this node unfolds into six subcategories: Patient Health, Pain, Sleep, Substance Use, Mental Health, and Quality of Life, each depicted as purple oval nodes
      - Demographics: this node unfolds into three subcategories by age range: Adults, Adolescents, and Pediatrics, each depicted as purple oval nodes
      - Research Programs: this node unfolds into the 13 HEAL Pain Research Programs, each depicted as purple triangle nodes. 
          - Selecting a specific HEAL Pain Research Program further unfolds into specific study names, allowing users to discern CDE applications at the individual study level. 

This interactive knowledge graph is designed to let researchers highlight and explore individual nodes and their connections, even without a technical background. Users can search and navigate through the graph using simple properties like color, shape, and size, easing identification of patterns, relationships, and focal points of interest. 

The graph is continually being refined for optimized logical coherence and search efficacy, making it more accessible and intuitive for users.
 '''
st.markdown(multi)

net = Network(notebook = True, cdn_resources="remote",height="800px", width="100%", select_menu = True, filter_menu=True,font_color="white", bgcolor = "black")

#add categorical/subcategorical nodes
net.add_nodes(['Node 1 - General Health', 
               'Node 2 - Patient Health', 
               'Node 3 - Pain',  
               'Node 4 - Sleep', 
               'Node 5 - Substance Use', 
               'Node 6 - Mental Health',
               'Node 7 - Quality of Life',
               'Node 8 - Demographics', 
               'Node 9 - Adults', 
               'Node 10 - Adolescent', 
               'Node 11 - Pediatric'],
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
    title = ['General Health',
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
net.add_nodes(['Node 12 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]', 
             'Node 13 - Brief Pain Inventory - Interference [BPI-Interference]',
             'Node 14 - Brief Pain Inventory - Severity [BPI-Severity]',
             'Node 15 - Demographics - Adult [Demographics-A]',
             'Node 16 - Demographics - Adult, Revised [Demographics-A Revised]',
             'Node 17 - Demographics - Pediatric [Demographics-Peds]',
             'Node 18 - Demographics - Pediatric, revised [Demographics-Peds Revised]',
             'Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]', 
             'Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]',
             'Node 21 - NIDA Modified Assist Tool - 2 [NIDA Assist-2 Modified]',
             'Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]', 
             'Node 23 - Pain Catastrophizing Scale - Parent [PCS-Parent]',
             'Node 24 - Pain Catastrophizing Scale - Pediatric [PCS-Peds]',
             'Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]',
             'Node 26 - Pain, Enjoyment, General Activity [PEG]',
             'Node 27 - Patient Global Impression of Change [PGIC]',
             'Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]',
             'Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]',
             'Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]',
             'Node 31 - Pediatric Quality of Life Inventory [PedsQL]',
             'Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]',
             'Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]',
             'Node 34 - Sleep Duration Question [SD - Adult or Peds]',
             'Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]'],
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
     title = ['Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]', 
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
    ('Node 1 - General Health','Node 2 - Patient Health'), 
    ('Node 1 - General Health','Node 3 - Pain'),
    ('Node 1 - General Health','Node 4 - Sleep'),
    ('Node 1 - General Health','Node 5 - Substance Use'),
    ('Node 1 - General Health','Node 6 - Mental Health'),
    ('Node 1 - General Health','Node 7 - Quality of Life'),
    ('Node 2 - Patient Health','Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]'),
    ('Node 2 - Patient Health','Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]'),
    ('Node 2 - Patient Health','Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]'),
    ('Node 3 - Pain','Node 13 - Brief Pain Inventory - Interference [BPI-Interference]'),
    ('Node 3 - Pain','Node 14 - Brief Pain Inventory - Severity [BPI-Severity]'),
    ('Node 3 - Pain','Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]'),
    ('Node 3 - Pain','Node 23 - Pain Catastrophizing Scale - Parent [PCS-Parent]'),
    ('Node 3 - Pain','Node 24 - Pain Catastrophizing Scale - Pediatric [PCS-Peds]'),
    ('Node 3 - Pain','Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]'),
    ('Node 4 - Sleep','Node 12 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]'),
    ('Node 4 - Sleep','Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]'),
    ('Node 4 - Sleep','Node 34 - Sleep Duration Question [SD - Adult or Peds]'),
    ('Node 5 - Substance Use', 'Node 21 - NIDA Modified Assist Tool - 2 [NIDA Assist-2 Modified]'),
    ('Node 5 - Substance Use', 'Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]'),
    ('Node 6 - Mental Health', 'Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]'),
    ('Node 6 - Mental Health','Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]'),
    ('Node 6 - Mental Health','Node 27 - Patient Global Impression of Change [PGIC]'),
    ('Node 7 - Quality of Life', 'Node 31 - Pediatric Quality of Life Inventory [PedsQL]'),
    ('Node 7 - Quality of Life','Node 26 - Pain, Enjoyment, General Activity [PEG]'),
    ('Node 7 - Quality of Life','Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]'),
    ('Node 8 - Demographics', 'Node 9 - Adults'),('Node 8 - Demographics', 'Node 10 - Adolescent'),
    ('Node 8 - Demographics','Node 11 - Pediatric'),
    ('Node 9 - Adults', 'Node 15 - Demographics - Adult [Demographics-A]'),
    ('Node 9 - Adults', 'Node 16 - Demographics - Adult, Revised [Demographics-A Revised]'),
    ('Node 9 - Adults','Node 23 - Pain Catastrophizing Scale - Parent [PCS-Parent]'),
    ('Node 10 - Adolescent', 'Node 12 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]'),
    ('Node 11 - Pediatric', 'Node 17 - Demographics - Pediatric [Demographics-Peds]'),
    ('Node 11 - Pediatric','Node 18 - Demographics - Pediatric, revised [Demographics-Peds Revised]'),
    ('Node 12 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]','Node 4 - Sleep'),
    ('Node 11 - Pediatric','Node 24 - Pain Catastrophizing Scale - Pediatric [PCS-Peds]'),
    
]
)

#adding the research programs
net.add_node('Node 36 - Biomarkers', label='Biomarkers', color = '#532565', shape = 'triangle', size = 25)
net.add_node('Node 37 - ERN', label = 'ERN', color = '#532565', shape = 'triangle', size = 25)
net.add_node('Node 38 - Health Equity in Pain Management', label = 'Health Equity in Pain Management', color = '#532565', shape = 'triangle', size = 25)
net.add_node('Node 39 - A2CPS', label = 'A2CPS', color = '#532565', shape = 'triangle', size = 15)
net.add_node('Node 40 - BACPAC', label = 'BACPAC', color = '#532565', shape = 'triangle', size = 20)
net.add_node('Node 41 - IMPOWR', label = 'IMPOWR', color = '#532565', shape = 'triangle', size = 20)
net.add_node('Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief', label = 'Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief', color = '#532565', shape = 'triangle', size = 20)
net.add_node('Node 43 - MPS- Myofascial Pain' , label = 'MPS- Myofascial Pain', color = '#532565', shape = 'triangle', size = 20)
net.add_node('Node 44 - PRECISION Human Pain', label = 'PRECISION Human Pain', color = '#532565', shape = 'triangle', size = 15)
net.add_node('Node 45 - PRISM', label = 'PRISM', color = '#532565', shape = 'triangle', size = 20)
net.add_node('Node 46 - HOPE', label = 'HOPE', color = '#532565', shape = 'triangle', size = 15)
net.add_node('Node 47 - EPPIC Net', label = 'EPPIC Net', color = '#532565', shape = 'triangle', size = 15)
net.add_node('Node 48 - RE JOIN', label = 'RE JOIN', color = '#532565', shape = 'triangle', size = 15)
net.add_node('Node 49 - Research Programs' , label = 'Research Programs', color = '#982568', shape = 'ellipse')

# adding connections for third subcategory "research programs" to each research program
net.add_edges([
    ('Node 49 - Research Programs','Node 36 - Biomarkers'),
    ('Node 49 - Research Programs','Node 37 - ERN'),
    ('Node 49 - Research Programs','Node 38 - Health Equity in Pain Management'),
    ('Node 49 - Research Programs','Node 39 - A2CPS'),
    ('Node 49 - Research Programs','Node 40 - BACPAC'),
    ('Node 49 - Research Programs','Node 41 - IMPOWR'),
    ('Node 49 - Research Programs','Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief'),
    ('Node 49 - Research Programs','Node 43 - MPS- Myofascial Pain'),
    ('Node 49 - Research Programs','Node 44 - PRECISION Human Pain'),
    ('Node 49 - Research Programs','Node 45 - PRISM'),
    ('Node 49 - Research Programs','Node 46 - HOPE'),
    ('Node 49 - Research Programs','Node 47 - EPPIC Net'),
    ('Node 49 - Research Programs','Node 48 - RE JOIN')
    
]
)

#adding connections for the research programs to CDEs
net.add_edges([
    ('Node 12 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]','Node 36 - Biomarkers'),
    ('Node 12 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]','Node 37 - ERN'),
    ('Node 12 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]','Node 38 - Health Equity in Pain Management'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 36 - Biomarkers'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 37 - ERN'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 38 - Health Equity in Pain Management'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 39 - A2CPS'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 40 - BACPAC'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 41 - IMPOWR'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 43 - MPS- Myofascial Pain'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 44 - PRECISION Human Pain'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 45 - PRISM'),
    ('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 36 - Biomarkers'),
    ('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 37 - ERN'),
    ('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 38 - Health Equity in Pain Management'),
    ('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 39 - A2CPS'),
    ('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 40 - BACPAC'),
    ('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 41 - IMPOWR'),
    ('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief'),
    ('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 43 - MPS- Myofascial Pain'),
    ('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 44 - PRECISION Human Pain'),
    ('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 45 - PRISM'),
    ('Node 15 - Demographics - Adult [Demographics-A]','Node 36 - Biomarkers'),
    ('Node 15 - Demographics - Adult [Demographics-A]','Node 37 - ERN'),
    ('Node 15 - Demographics - Adult [Demographics-A]','Node 38 - Health Equity in Pain Management'),
    ('Node 15 - Demographics - Adult [Demographics-A]','Node 39 - A2CPS'),
    ('Node 15 - Demographics - Adult [Demographics-A]','Node 40 - BACPAC'),
    ('Node 15 - Demographics - Adult [Demographics-A]','Node 41 - IMPOWR'),
    ('Node 15 - Demographics - Adult [Demographics-A]','Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief'),
    ('Node 15 - Demographics - Adult [Demographics-A]','Node 43 - MPS- Myofascial Pain'),
    ('Node 15 - Demographics - Adult [Demographics-A]','Node 44 - PRECISION Human Pain'),
    ('Node 15 - Demographics - Adult [Demographics-A]','Node 45 - PRISM'),
    ('Node 15 - Demographics - Adult [Demographics-A]','Node 46 - HOPE'),
    ('Node 15 - Demographics - Adult [Demographics-A]','Node 47 - EPPIC Net'),
    ('Node 15 - Demographics - Adult [Demographics-A]','Node 48 - RE JOIN'),
    ('Node 16 - Demographics - Adult, Revised [Demographics-A Revised]','Node 38 - Health Equity in Pain Management'),
    ('Node 17 - Demographics - Pediatric [Demographics-Peds]','Node 36 - Biomarkers'),
    ('Node 17 - Demographics - Pediatric [Demographics-Peds]','Node 37 - ERN'),
    ('Node 17 - Demographics - Pediatric [Demographics-Peds]','Node 38 - Health Equity in Pain Management'),
    ('Node 18 - Demographics - Pediatric, revised [Demographics-Peds Revised]','Node 38 - Health Equity in Pain Management'),
    ('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 36 - Biomarkers'),
    ('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 37 - ERN'),
    ('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 38 - Health Equity in Pain Management'),
    ('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 40 - BACPAC'),
    ('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 41 - IMPOWR'),
    ('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief'),
    ('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 43 - MPS- Myofascial Pain'),
    ('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 44 - PRECISION Human Pain'),
    ('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 45 - PRISM'),
    ('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 47 - EPPIC Net'),
    ('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 48 - RE JOIN'),
    ('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 37 - ERN'),
    ('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 38 - Health Equity in Pain Management'),
    ('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 39 - A2CPS'),
    ('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 40 - BACPAC'),
    ('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 41 - IMPOWR'),
    ('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief'),
    ('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 43 - MPS- Myofascial Pain'),
    ('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 45 - PRISM'),
    ('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 46 - HOPE'),
    ('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 48 - RE JOIN'),
    ('Node 21 - NIDA Modified Assist Tool - 2 [NIDA Assist-2 Modified]','Node 36 - Biomarkers'),
    ('Node 21 - NIDA Modified Assist Tool - 2 [NIDA Assist-2 Modified]','Node 37 - ERN'),
    ('Node 21 - NIDA Modified Assist Tool - 2 [NIDA Assist-2 Modified]','Node 38 - Health Equity in Pain Management'),
    ('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 36 - Biomarkers'),
    ('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 37 - ERN'),
    ('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 38 - Health Equity in Pain Management'),
    ('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 40 - BACPAC'),
    ('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 41 - IMPOWR'),
    ('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief'),
    ('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 43 - MPS- Myofascial Pain'),
    ('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 45 - PRISM'),
    ('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 48 - RE JOIN'),
    ('Node 23 - Pain Catastrophizing Scale - Parent [PCS-Parent]','Node 36 - Biomarkers'),
    ('Node 23 - Pain Catastrophizing Scale - Parent [PCS-Parent]','Node 37 - ERN'),
    ('Node 23 - Pain Catastrophizing Scale - Parent [PCS-Parent]','Node 38 - Health Equity in Pain Management'),
    ('Node 24 - Pain Catastrophizing Scale - Pediatric [PCS-Peds]','Node 36 - Biomarkers'),
    ('Node 24 - Pain Catastrophizing Scale - Pediatric [PCS-Peds]','Node 37 - ERN'),
    ('Node 24 - Pain Catastrophizing Scale - Pediatric [PCS-Peds]','Node 38 - Health Equity in Pain Management'),
    ('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 36 - Biomarkers'),
    ('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 37 - ERN'),
    ('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 38 - Health Equity in Pain Management'),
    ('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 39 - A2CPS'),
    ('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 40 - BACPAC'),
    ('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 41 - IMPOWR'),
    ('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief'),
    ('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 43 - MPS- Myofascial Pain'),
    ('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 44 - PRECISION Human Pain'),
    ('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 45 - PRISM'),
    ('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 46 - HOPE'),
    ('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 47 - EPPIC Net'),
    ('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 48 - RE JOIN'),
    ('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 36 - Biomarkers'),
    ('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 37 - ERN'),
    ('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 38 - Health Equity in Pain Management'),
    ('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 39 - A2CPS'),
    ('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 40 - BACPAC'),
    ('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 41 - IMPOWR'),
    ('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief'),
    ('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 43 - MPS- Myofascial Pain'),
    ('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 44 - PRECISION Human Pain'),
    ('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 45 - PRISM'),
    ('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 46 - HOPE'),
    ('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 47 - EPPIC Net'),
    ('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 48 - RE JOIN'),
    ('Node 27 - Patient Global Impression of Change [PGIC]','Node 36 - Biomarkers'),
    ('Node 27 - Patient Global Impression of Change [PGIC]','Node 37 - ERN'),
    ('Node 27 - Patient Global Impression of Change [PGIC]','Node 38 - Health Equity in Pain Management'),
    ('Node 27 - Patient Global Impression of Change [PGIC]','Node 39 - A2CPS'),
    ('Node 27 - Patient Global Impression of Change [PGIC]','Node 40 - BACPAC'),
    ('Node 27 - Patient Global Impression of Change [PGIC]','Node 41 - IMPOWR'),
    ('Node 27 - Patient Global Impression of Change [PGIC]','Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief'),
    ('Node 27 - Patient Global Impression of Change [PGIC]','Node 43 - MPS- Myofascial Pain'),
    ('Node 27 - Patient Global Impression of Change [PGIC]','Node 44 - PRECISION Human Pain'),
    ('Node 27 - Patient Global Impression of Change [PGIC]','Node 45 - PRISM'),
    ('Node 27 - Patient Global Impression of Change [PGIC]','Node 46 - HOPE'),
    ('Node 27 - Patient Global Impression of Change [PGIC]','Node 47 - EPPIC Net'),
    ('Node 27 - Patient Global Impression of Change [PGIC]','Node 48 - RE JOIN'),
    ('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 36 - Biomarkers'),
    ('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 37 - ERN'),
    ('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 38 - Health Equity in Pain Management'),
    ('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 40 - BACPAC'),
    ('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 41 - IMPOWR'),
    ('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief'),
    ('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 43 - MPS- Myofascial Pain'),
    ('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 44 - PRECISION Human Pain'),
    ('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 45 - PRISM'),
    ('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 47 - EPPIC Net'),
    ('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 48 - RE JOIN'),
    ('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]','Node 37 - ERN'),
    ('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]','Node 38 - Health Equity in Pain Management'),
    ('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]','Node 39 - A2CPS'),
    ('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]','Node 43 - MPS- Myofascial Pain'),
    ('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]','Node 45 - PRISM'),
    ('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]','Node 48 - RE JOIN'),
    ('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 36 - Biomarkers'),
    ('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 37 - ERN'),
    ('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 40 - BACPAC'),
    ('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 41 - IMPOWR'),
    ('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 41 - IMPOWR'),
    ('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 43 - MPS- Myofascial Pain'),
    ('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 45 - PRISM'),
    ('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 46 - HOPE'),
    ('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 48 - RE JOIN'),
    ('Node 31 - Pediatric Quality of Life Inventory [PedsQL]','Node 36 - Biomarkers'),
    ('Node 31 - Pediatric Quality of Life Inventory [PedsQL]','Node 37 - ERN'),
    ('Node 31 - Pediatric Quality of Life Inventory [PedsQL]','Node 38 - Health Equity in Pain Management'),
    ('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 36 - Biomarkers'),
    ('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 37 - ERN'),
    ('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 38 - Health Equity in Pain Management'),
    ('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 39 - A2CPS'),
    ('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 40 - BACPAC'),
    ('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 41 - IMPOWR'),
    ('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief'),
    ('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 43 - MPS- Myofascial Pain'),
    ('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 44 - PRECISION Human Pain'),
    ('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 45 - PRISM'),
    ('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 46 - HOPE'),
    ('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 47 - EPPIC Net'),
    ('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 48 - RE JOIN'),
    ('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 36 - Biomarkers'),
    ('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 37 - ERN'),
    ('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 38 - Health Equity in Pain Management'),
    ('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 39 - A2CPS'),
    ('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 40 - BACPAC'),
    ('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 41 - IMPOWR'),
    ('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief'),
    ('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 43 - MPS- Myofascial Pain'),
    ('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 44 - PRECISION Human Pain'),
    ('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 45 - PRISM'),
    ('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 46 - HOPE'),
    ('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 47 - EPPIC Net'),
    ('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 48 - RE JOIN'),
    ('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 36 - Biomarkers'),
    ('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 37 - ERN'),
    ('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 38 - Health Equity in Pain Management'),
    ('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 39 - A2CPS'),
    ('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 40 - BACPAC'),
    ('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 41 - IMPOWR'),
    ('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief'),
    ('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 43 - MPS- Myofascial Pain'),
    ('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 44 - PRECISION Human Pain'),
    ('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 45 - PRISM'),
    ('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 46 - HOPE'),
    ('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 47 - EPPIC Net'),
    ('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 48 - RE JOIN'),   
    ('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 36 - Biomarkers'),
    ('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 37 - ERN'),
    ('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 38 - Health Equity in Pain Management'),
    ('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 39 - A2CPS'),
    ('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 40 - BACPAC'),
    ('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 41 - IMPOWR'),
    ('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief'),
    ('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 43 - MPS- Myofascial Pain'),
    ('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 44 - PRECISION Human Pain'),
    ('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 45 - PRISM'),
    ('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 46 - HOPE'),
    ('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 47 - EPPIC Net'),
    ('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 48 - RE JOIN')   
]
)

## add study names for Node 12 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]

net.add_nodes(['Node 50 - SPRINT: Signature for Pain Recovery IN Teens', 
               'Node 51 - SurgeryPal', 
               'Node 52 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma',  
               'Node 53 - Integrative Training Program for Pediatric Sickle Cell Pain',
               'Node 54 - Latinx Children and Surgery'],
    label = ['SPRINT: Signature for Pain Recovery IN Teens',
             'SurgeryPal',
             'Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma',
             'Integrative Training Program for Pediatric Sickle Cell Pain',
             'Latinx Children and Surgery'],
    title = ['SPRINT: Signature for Pain Recovery IN Teens',
             'SurgeryPal',
             'Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma',
             'Integrative Training Program for Pediatric Sickle Cell Pain',
             'Latinx Children and Surgery'],
    shape = ['text','text','text','text','text']

)

## add edge connection for Node 12 to Study Names
net.add_edges([
    ('Node 12 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]','Node 50 - SPRINT: Signature for Pain Recovery IN Teens'),
    ('Node 12 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]','Node 51 - SurgeryPal'),
    ('Node 12 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]','Node 52 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma'),
    ('Node 12 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]','Node 53 - Integrative Training Program for Pediatric Sickle Cell Pain'),
    ('Node 12 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]','Node 54 - Latinx Children and Surgery'),
    
]
)

## add study names for Node 13 - Brief Pain Inventory - Interference [BPI-Interference]

net.add_nodes(['Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery', 
               'Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain', 
               'Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache',  
               'Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience',
               'Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy',
               'Node 60 - Validation of a novel cortical biomarker signature for pain', 
               'Node 61 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)',
               'Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial',
               'Node 63 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma', 
               'Node 64 - Integrative Training Program for Pediatric Sickle Cell Pain',
               'Node 65 - PAINED: Project Addressing INequities in the Emergency Department',
               'Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder',
               'Node 67 - RM1 Project 1: Evaluating the specific role of endogenous opioids as the mechanism underlying tAN-based analgesia in healthy individuals',
               'Node 68 - RM1 Project 2: Determining the independent and synergistic effects of transcutaneous auricular neurostimulation (tAN) on direct brain activation in healthy individuals',
               'Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management',
               'Node 70 - INTERCEPT: Integrated Research Center for human Pain Tissues',
               'Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial'],
    label = ['Transition from Acute to Chronic Pain After Thoracic Surgery',
             'Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain',
             'Biomarker Signature to Predict the Persistence of Post-Traumatic Headache',
             'Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience',
             'Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy',
             'Validation of a novel cortical biomarker signature for pain',
             'Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)',
             'Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial',
             'Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma',
             'Integrative Training Program for Pediatric Sickle Cell Pain',
             'PAINED: Project Addressing INequities in the Emergency Department',
             'Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder',
             'RM1 Project 1: Evaluating the specific role of endogenous opioids as the mechanism underlying tAN-based analgesia in healthy individuals',
             'RM1 Project 2: Determining the independent and synergistic effects of transcutaneous auricular neurostimulation (tAN) on direct brain activation in healthy individuals',
             'HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management',
             'INTERCEPT: Integrated Research Center for human Pain Tissues',
             'Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial'],
    title = ['Transition from Acute to Chronic Pain After Thoracic Surgery',
             'Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain',
             'Biomarker Signature to Predict the Persistence of Post-Traumatic Headache',
             'Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience',
             'Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy',
             'Validation of a novel cortical biomarker signature for pain',
             'Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)',
             'Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial',
             'Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma',
             'Integrative Training Program for Pediatric Sickle Cell Pain',
             'PAINED: Project Addressing INequities in the Emergency Department',
             'Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder',
             'RM1 Project 1: Evaluating the specific role of endogenous opioids as the mechanism underlying tAN-based analgesia in healthy individuals',
             'RM1 Project 2: Determining the independent and synergistic effects of transcutaneous auricular neurostimulation (tAN) on direct brain activation in healthy individuals',
             'HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management',
             'INTERCEPT: Integrated Research Center for human Pain Tissues',
             'Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial'],
    shape = ['text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text']

)

## add edge connection for Node 13 to Study Names
    
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery')
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain') 
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache')
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience')
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy')
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 60 - Validation of a novel cortical biomarker signature for pain') 
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 61 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)')
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial')
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 63 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma')
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 64 - Integrative Training Program for Pediatric Sickle Cell Pain')
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 65 - PAINED: Project Addressing INequities in the Emergency Department')
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder')
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 67 - RM1 Project 1: Evaluating the specific role of endogenous opioids as the mechanism underlying tAN-based analgesia in healthy individuals')
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 68 - RM1 Project 2: Determining the independent and synergistic effects of transcutaneous auricular neurostimulation (tAN) on direct brain activation in healthy individuals')
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management')
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 70 - INTERCEPT: Integrated Research Center for human Pain Tissues')
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial')
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 50 - SPRINT: Signature for Pain Recovery IN Teens')
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 51 - SurgeryPal')
net.add_edge('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 54 - Latinx Children and Surgery')


# adding connections for 'Node 14 - Brief Pain Inventory - Severity [BPI-Severity]'
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery')
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain') 
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache')
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience')
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy')
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 60 - Validation of a novel cortical biomarker signature for pain') 
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 61 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)')
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial')
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 63 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma')
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 64 - Integrative Training Program for Pediatric Sickle Cell Pain')
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 65 - PAINED: Project Addressing INequities in the Emergency Department')
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder')
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 67 - RM1 Project 1: Evaluating the specific role of endogenous opioids as the mechanism underlying tAN-based analgesia in healthy individuals')
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 68 - RM1 Project 2: Determining the independent and synergistic effects of transcutaneous auricular neurostimulation (tAN) on direct brain activation in healthy individuals')
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management')
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 70 - INTERCEPT: Integrated Research Center for human Pain Tissues')
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial')
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 50 - SPRINT: Signature for Pain Recovery IN Teens')
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 51 - SurgeryPal')
net.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 54 - Latinx Children and Surgery')

#create study names to connect to node 15

net.add_nodes(['Node 72 - COMEBACK',
             'Node 73 - Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain',
             'Node 74 - HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes',
             'Node 75 - Imaging Epigenetic Dysregulation in Patients with Low Back Pain',
             'Node 76 - Nonpharmacologic Pain Management for Lumbar Surgery',
             'Node 77 - Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain',
             'Node 78 - Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain',
             'Node 79 - Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity',
             'Node 80 - Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC',
             'Node 81 - The Spine Phenome Project: Enabling Technology for Personalized Medicine',
             'Node 82 - UM MRC BACPAC',
             'Node 83 - Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation',
             'Node 84 - Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury',
             'Node 85 - Discovery of the Biomarker Signature for Neuropathic Corneal Pain',
             'Node 86 - Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers',
             'Node 87 - A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain',
             'Node 88 - EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)',
             'Node 89 - EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy',
             'Node 90 - A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain',
             'Node 91 - Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder',
             'Node 92 - Optimizing the use of ketamine to reduce chronic postsurgical pain',
             'Node 93 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)',
             'Node 94 - RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches',
             'Node 95 - Wake Forest NCORP Research Base',
             'Node 96 - Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study',
             'Node 97 - Equity Using Interventions for Pain and Depression (EQUIPD)',
             'Node 98 - Group-based Integrative Pain Management: A multi-level approach to address intersectional stigma and social isolation in diverse primary care safety net patients with chronic pain',
             'Node 99 - Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination',
             'Node 100 - Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain',
             'Node 101 - A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis',
             'Node 102 - Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial',
             'Node 103 - Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)',
             'Node 104 - Pain Care At Home to Amplify Function (Pain CHAMP)',
             'Node 105 - Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder',
             'Node 106 - Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)',
             'Node 107 - Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)',
             'Node 108 - From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects',
             'Node 109 - Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain',
             'Node 110 - Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain',
             'Node 111 - Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain',
             'Node 112 - MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome',
             'Node 113 - Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain',
             'Node 114 - Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain',
             'Node 115 - Total-body PET for assessing myofascial pain',
             'Node 116 - Harvard PRECISION Human Pain Center',
             'Node 117 - Human Nociceptor and Spinal Cord Molecular Signature Center',
             'Node 118 - Group-Based Mindfulness for Patients with Chronic Low Back Pain in the Primary Care',
             'Node 119 - Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain',
             'Node 120 - Nonpharmacologic Pain Management for Lumbar Surgery',
             'Node 121 - Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial',
             'Node 122 - Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adult',
             'Node 123 - Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)',
             'Node 124 - Innervation of the knee and TMJ',
             'Node 125 - Mapping the joint-nerve interactome of the knee',
             'Node 126 - Neural architecture of the murine and human temporomandibular joint'],
    label = ['COMEBACK',
             'Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain',
             'HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes',
             'Imaging Epigenetic Dysregulation in Patients with Low Back Pain',
             'Nonpharmacologic Pain Management for Lumbar Surgery',
             'Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain',
             'Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain',
             'Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity',
             'Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC',
             'The Spine Phenome Project: Enabling Technology for Personalized Medicine',
             'UM MRC BACPAC',
             'Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation',
             'Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury',
             'Discovery of the Biomarker Signature for Neuropathic Corneal Pain',
             'Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers',
             'A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain',
             'EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)',
             'EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy',
             'A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain',
             'Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder',
             'Optimizing the use of ketamine to reduce chronic postsurgical pain',
             'Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)',
             'RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches',
             'Wake Forest NCORP Research Base',
             'Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study',
             'Equity Using Interventions for Pain and Depression (EQUIPD)',
             'Group-based Integrative Pain Management: A multi-level approach to address intersectional stigma and social isolation in diverse primary care safety net patients with chronic pain',
             'Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination',
             'Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain',
             'A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis',
             'Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial',
             'Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)',
             'Pain Care At Home to Amplify Function (Pain CHAMP)',
             'Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder',
             'Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)',
             'Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)',
             'From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects',
             'Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain',
             'Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain',
             'Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain',
             'MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome',
             'Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain',
             'Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain',
             'Total-body PET for assessing myofascial pain',
             'Harvard PRECISION Human Pain Center',
             'Human Nociceptor and Spinal Cord Molecular Signature Center',
             'Group-Based Mindfulness for Patients with Chronic Low Back Pain in the Primary Care',
             'Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain',
             'Nonpharmacologic Pain Management for Lumbar Surgery',
             'Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial',
             'Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adult',
             'Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)',
             'Innervation of the knee and TMJ',
             'Mapping the joint-nerve interactome of the knee',
             'Neural architecture of the murine and human temporomandibular joint'],
    title = ['COMEBACK',
             'Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain',
             'HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes',
             'Imaging Epigenetic Dysregulation in Patients with Low Back Pain',
             'Nonpharmacologic Pain Management for Lumbar Surgery',
             'Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain',
             'Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain',
             'Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity',
             'Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC',
             'The Spine Phenome Project: Enabling Technology for Personalized Medicine',
             'UM MRC BACPAC',
             'Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation',
             'Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury',
             'Discovery of the Biomarker Signature for Neuropathic Corneal Pain',
             'Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers',
             'A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain',
             'EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)',
             'EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy',
             'A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain',
             'Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder',
             'Optimizing the use of ketamine to reduce chronic postsurgical pain',
             'Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)',
             'RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches',
             'Wake Forest NCORP Research Base',
             'Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study',
             'Equity Using Interventions for Pain and Depression (EQUIPD)',
             'Group-based Integrative Pain Management: A multi-level approach to address intersectional stigma and social isolation in diverse primary care safety net patients with chronic pain',
             'Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination',
             'Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain',
             'A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis',
             'Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial',
             'Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)',
             'Pain Care At Home to Amplify Function (Pain CHAMP)',
             'Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder',
             'Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)',
             'Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)',
             'From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects',
             'Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain',
             'Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain',
             'Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain',
             'MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome',
             'Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain',
             'Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain',
             'Total-body PET for assessing myofascial pain',
             'Harvard PRECISION Human Pain Center',
             'Human Nociceptor and Spinal Cord Molecular Signature Center',
             'Group-Based Mindfulness for Patients with Chronic Low Back Pain in the Primary Care',
             'Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain',
             'Nonpharmacologic Pain Management for Lumbar Surgery',
             'Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial',
             'Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adult',
             'Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)',
             'Innervation of the knee and TMJ',
             'Mapping the joint-nerve interactome of the knee',
             'Neural architecture of the murine and human temporomandibular joint'],
    shape = ['text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text']

)

## add edge connection for Node 15 to Study Names

net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]', 'Node 72 - COMEBACK')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 73 - Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 74 - HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 75 - Imaging Epigenetic Dysregulation in Patients with Low Back Pain')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 76 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]', 'Node 77 - Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 78 - Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]', 'Node 79 - Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 80 - Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 81 - The Spine Phenome Project: Enabling Technology for Personalized Medicine')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 82 - UM MRC BACPAC')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]', 'Node 83 - Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 84 - Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 85 - Discovery of the Biomarker Signature for Neuropathic Corneal Pain')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 86 - Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]', 'Node 87 - A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 88 - EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 89 - EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 90 - A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 91 - Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 92 - Optimizing the use of ketamine to reduce chronic postsurgical pain')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 93 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 94 - RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 95 - Wake Forest NCORP Research Base')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 96 - Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 97 - Equity Using Interventions for Pain and Depression (EQUIPD)')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 98 - Group-based Integrative Pain Management: A multi-level approach to address intersectional stigma and social isolation in diverse primary care safety net patients with chronic pain')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 99 - Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 100 - Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]', 'Node 101 - A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 102 - Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 103 - Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 104 - Pain Care At Home to Amplify Function (Pain CHAMP)')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 105 - Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 106 - Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 107 - Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]', 'Node 108 - From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]', 'Node 109 - Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 110 - Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]', 'Node 111 - Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]', 'Node 112 - MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 113 - Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 114 - Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 115 - Total-body PET for assessing myofascial pain')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 116 - Harvard PRECISION Human Pain Center')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 117 - Human Nociceptor and Spinal Cord Molecular Signature Center')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 118 - Group-Based Mindfulness for Patients with Chronic Low Back Pain in the Primary Care')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 119 - Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 120 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 121 - Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 122 - Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adult')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 123 - Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 124 - Innervation of the knee and TMJ')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 125 - Mapping the joint-nerve interactome of the knee')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 126 - Neural architecture of the murine and human temporomandibular joint')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain') 
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 60 - Validation of a novel cortical biomarker signature for pain') 
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]', 'Node 61 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]', 'Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]','Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]', 'Node 67 - RM1 Project 1: Evaluating the specific role of endogenous opioids as the mechanism underlying tAN-based analgesia in healthy individuals')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]', 'Node 68 - RM1 Project 2: Determining the independent and synergistic effects of transcutaneous auricular neurostimulation (tAN) on direct brain activation in healthy individuals')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]', 'Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]', 'Node 70 - INTERCEPT: Integrated Research Center for human Pain Tissues')
net.add_edge('Node 15 - Demographics - Adult [Demographics-A]', 'Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial')
        
net.add_edge('Node 16 - Demographics - Adult, Revised [Demographics-A Revised]', 'Node 65 - PAINED: Project Addressing INequities in the Emergency Department')
net.add_edge('Node 17 - Demographics - Pediatric [Demographics-Peds]','Node 50 - SPRINT: Signature for Pain Recovery IN Teens') 
net.add_edge('Node 17 - Demographics - Pediatric [Demographics-Peds]','Node 51 - SurgeryPal')
net.add_edge('Node 17 - Demographics - Pediatric [Demographics-Peds]','Node 52 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma')  
net.add_edge('Node 17 - Demographics - Pediatric [Demographics-Peds]','Node 53 - Integrative Training Program for Pediatric Sickle Cell Pain')
net.add_edge('Node 17 - Demographics - Pediatric [Demographics-Peds]','Node 54 - Latinx Children and Surgery')
net.add_edge('Node 18 - Demographics - Pediatric, revised [Demographics-Peds Revised]','Node 65 - PAINED: Project Addressing INequities in the Emergency Department')


## add edge connection for 'Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]'

net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]', 'Node 72 - COMEBACK')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain') 
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 74 - HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 76 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]', 'Node 77 - Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 78 - Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]', 'Node 79 - Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 80 - Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 81 - The Spine Phenome Project: Enabling Technology for Personalized Medicine')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 82 - UM MRC BACPAC')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]', 'Node 83 - Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 85 - Discovery of the Biomarker Signature for Neuropathic Corneal Pain')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 86 - Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]', 'Node 50 - SPRINT: Signature for Pain Recovery IN Teens')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 60 - Validation of a novel cortical biomarker signature for pain') 
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]', 'Node 87 - A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 88 - EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 89 - EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 92 - Optimizing the use of ketamine to reduce chronic postsurgical pain')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]', 'Node 51 - SurgeryPal')

net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 52 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma')  
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 53 - Integrative Training Program for Pediatric Sickle Cell Pain')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 54 - Latinx Children and Surgery')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 99 - Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 100 - Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 103 - Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 104 - Pain Care At Home to Amplify Function (Pain CHAMP)')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 105 - Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder')

net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 107 - Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]', 'Node 108 - From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects')

net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 110 - Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]', 'Node 111 - Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]', 'Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 115 - Total-body PET for assessing myofascial pain')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 116 - Harvard PRECISION Human Pain Center')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 117 - Human Nociceptor and Spinal Cord Molecular Signature Center')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]', 'Node 70 - INTERCEPT: Integrated Research Center for human Pain Tissues')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 119 - Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 120 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 121 - Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 125 - Mapping the joint-nerve interactome of the knee')
net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]','Node 126 - Neural architecture of the murine and human temporomandibular joint')

        
#Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]'
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 73 - Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 84 - Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 90 - A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 91 - Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 93 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 94 - RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 95 - Wake Forest NCORP Research Base')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 96 - Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 97 - Equity Using Interventions for Pain and Depression (EQUIPD)')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 98 - Group-based Integrative Pain Management: A multi-level approach to address intersectional stigma and social isolation in diverse primary care safety net patients with chronic pain')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 102 - Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 106 - Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 109 - Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]', 'Node 112 - MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 113 - Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 114 - Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]', 'Node 122 - Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adult')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 123 - Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)')
net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]','Node 124 - Innervation of the knee and TMJ')


#'Node 21 - NIDA Modified Assist Tool - 2 [NIDA Assist-2 Modified]'
net.add_edge('Node 21 - NIDA Modified Assist Tool - 2 [NIDA Assist-2 Modified]','Node 50 - SPRINT: Signature for Pain Recovery IN Teens')
net.add_edge('Node 21 - NIDA Modified Assist Tool - 2 [NIDA Assist-2 Modified]','Node 51 - SurgeryPal')
net.add_edge('Node 21 - NIDA Modified Assist Tool - 2 [NIDA Assist-2 Modified]','Node 52 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma')
net.add_edge('Node 21 - NIDA Modified Assist Tool - 2 [NIDA Assist-2 Modified]','Node 53 - Integrative Training Program for Pediatric Sickle Cell Pain')
net.add_edge('Node 21 - NIDA Modified Assist Tool - 2 [NIDA Assist-2 Modified]','Node 54 - Latinx Children and Surgery')


#'Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]',
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 75 - Imaging Epigenetic Dysregulation in Patients with Low Back Pain')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 84 - Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 86 - Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 60 - Validation of a novel cortical biomarker signature for pain') 
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 90 - A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 91 - Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 92 - Optimizing the use of ketamine to reduce chronic postsurgical pain')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 93 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 95 - Wake Forest NCORP Research Base')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 96 - Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 97 - Equity Using Interventions for Pain and Depression (EQUIPD)')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 99 - Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 105 - Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 108 - From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 112 - MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 122 - Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adult')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 124 - Innervation of the knee and TMJ')
net.add_edge('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]','Node 125 - Mapping the joint-nerve interactome of the knee')


##'Node 23 - Pain Catastrophizing Scale - Parent [PCS-Parent]'

net.add_edge('Node 23 - Pain Catastrophizing Scale - Parent [PCS-Parent]','Node 50 - SPRINT: Signature for Pain Recovery IN Teens')
net.add_edge('Node 23 - Pain Catastrophizing Scale - Parent [PCS-Parent]','Node 51 - SurgeryPal')
net.add_edge('Node 23 - Pain Catastrophizing Scale - Parent [PCS-Parent]','Node 52 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma')
net.add_edge('Node 23 - Pain Catastrophizing Scale - Parent [PCS-Parent]','Node 53 - Integrative Training Program for Pediatric Sickle Cell Pain')
net.add_edge('Node 23 - Pain Catastrophizing Scale - Parent [PCS-Parent]','Node 54 - Latinx Children and Surgery')

#'Node 24 - Pain Catastrophizing Scale - Pediatric [PCS-Peds]'
net.add_edge('Node 24 - Pain Catastrophizing Scale - Pediatric [PCS-Peds]','Node 50 - SPRINT: Signature for Pain Recovery IN Teens')
net.add_edge('Node 24 - Pain Catastrophizing Scale - Pediatric [PCS-Peds]','Node 51 - SurgeryPal')
net.add_edge('Node 24 - Pain Catastrophizing Scale - Pediatric [PCS-Peds]','Node 52 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma')
net.add_edge('Node 24 - Pain Catastrophizing Scale - Pediatric [PCS-Peds]','Node 53 - Integrative Training Program for Pediatric Sickle Cell Pain')
net.add_edge('Node 24 - Pain Catastrophizing Scale - Pediatric [PCS-Peds]','Node 54 - Latinx Children and Surgery')


#'Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]',

net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]', 'Node 72 - COMEBACK')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain') 
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 73 - Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 74 - HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 76 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]', 'Node 77 - Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 78 - Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]', 'Node 79 - Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 80 - Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 81 - The Spine Phenome Project: Enabling Technology for Personalized Medicine')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 82 - UM MRC BACPAC')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]', 'Node 83 - Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 85 - Discovery of the Biomarker Signature for Neuropathic Corneal Pain')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]', 'Node 87 - A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 88 - EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 89 - EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 94 - RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 98 - Group-based Integrative Pain Management: A multi-level approach to address intersectional stigma and social isolation in diverse primary care safety net patients with chronic pain')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 100 - Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 101 - A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 102 - Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 103 - Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 104 - Pain Care At Home to Amplify Function (Pain CHAMP)')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 106 - Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 107 - Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 109 - Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 110 - Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]', 'Node 111 - Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 113 - Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 114 - Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 115 - Total-body PET for assessing myofascial pain')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 116 - Harvard PRECISION Human Pain Center')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 117 - Human Nociceptor and Spinal Cord Molecular Signature Center')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 118 - Group-Based Mindfulness for Patients with Chronic Low Back Pain in the Primary Care')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 119 - Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 120 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 121 - Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 123 - Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)')
net.add_edge('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]','Node 126 - Neural architecture of the murine and human temporomandibular joint')

#add edge connection to 'Node 26 - Pain, Enjoyment, General Activity [PEG]',

net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]', 'Node 72 - COMEBACK')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain') 
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 73 - Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 74 - HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 76 - Nonpharmacologic Pain Management for Lumbar Surgery')

net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]', 'Node 77 - Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 78 - Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]', 'Node 79 - Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 80 - Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 81 - The Spine Phenome Project: Enabling Technology for Personalized Medicine')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 82 - UM MRC BACPAC')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]', 'Node 83 - Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation')

net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 84 - Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 86 - Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 85 - Discovery of the Biomarker Signature for Neuropathic Corneal Pain')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]', 'Node 87 - A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 88 - EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 89 - EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 90 - A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 91 - Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 92 - Optimizing the use of ketamine to reduce chronic postsurgical pain')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 94 - RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 95 - Wake Forest NCORP Research Base')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 96 - Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 97 - Equity Using Interventions for Pain and Depression (EQUIPD)')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 98 - Group-based Integrative Pain Management: A multi-level approach to address intersectional stigma and social isolation in diverse primary care safety net patients with chronic pain')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 99 - Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 100 - Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 101 - A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 102 - Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 103 - Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 104 - Pain Care At Home to Amplify Function (Pain CHAMP)')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 105 - Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 106 - Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 107 - Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)')            
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 108 - From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 109 - Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 110 - Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]', 'Node 111 - Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 112 - MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 113 - Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 114 - Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 115 - Total-body PET for assessing myofascial pain')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 116 - Harvard PRECISION Human Pain Center')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 117 - Human Nociceptor and Spinal Cord Molecular Signature Center')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 70 - INTERCEPT: Integrated Research Center for human Pain Tissues')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]', 'Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 118 - Group-Based Mindfulness for Patients with Chronic Low Back Pain in the Primary Care')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 119 - Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 120 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 121 - Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 122 - Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adult')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 123 - Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 124 - Innervation of the knee and TMJ')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 125 - Mapping the joint-nerve interactome of the knee')
net.add_edge('Node 26 - Pain, Enjoyment, General Activity [PEG]','Node 126 - Neural architecture of the murine and human temporomandibular joint')

#add edge connection to 'Node 27 - Patient Global Impression of Change [PGIC]',


net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]', 'Node 72 - COMEBACK')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain') 
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 73 - Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 74 - HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 75 - Imaging Epigenetic Dysregulation in Patients with Low Back Pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 76 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 77 - Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 78 - Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 79 - Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 80 - Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 81 - The Spine Phenome Project: Enabling Technology for Personalized Medicine')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 82 - UM MRC BACPAC')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 83 - Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 84 - Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 86 - Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 50 - SPRINT: Signature for Pain Recovery IN Teens')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 51 - SurgeryPal')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 60 - Validation of a novel cortical biomarker signature for pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 87 - A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 88 - EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 89 - EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 90 - A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 91 - Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 92 - Optimizing the use of ketamine to reduce chronic postsurgical pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 93 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 94 - RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 95 - Wake Forest NCORP Research Base')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 96 - Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 52 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 97 - Equity Using Interventions for Pain and Depression (EQUIPD)')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 98 - Group-based Integrative Pain Management: A multi-level approach to address intersectional stigma and social isolation in diverse primary care safety net patients with chronic pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 99 - Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 53 - Integrative Training Program for Pediatric Sickle Cell Pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 54 - Latinx Children and Surgery')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 100 - Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 101 - A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 102 - Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 103 - Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 104 - Pain Care At Home to Amplify Function (Pain CHAMP)')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 105 - Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 106 - Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 107 - Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 108 - From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 67 - RM1 Project 1: Evaluating the specific role of endogenous opioids as the mechanism underlying tAN-based analgesia in healthy individuals')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 68 - RM1 Project 2: Determining the independent and synergistic effects of transcutaneous auricular neurostimulation (tAN) on direct brain activation in healthy individuals')          
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 109 - Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 110 - Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 111 - Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 112 - MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 113 - Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 114 - Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 115 - Total-body PET for assessing myofascial pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 116 - Harvard PRECISION Human Pain Center')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 117 - Human Nociceptor and Spinal Cord Molecular Signature Center')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 70 - INTERCEPT: Integrated Research Center for human Pain Tissues')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]', 'Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial')        
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 118 - Group-Based Mindfulness for Patients with Chronic Low Back Pain in the Primary Care')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 119 - Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 120 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 121 - Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 122 - Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adult')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 123 - Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 124 - Innervation of the knee and TMJ')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 125 - Mapping the joint-nerve interactome of the knee')
net.add_edge('Node 27 - Patient Global Impression of Change [PGIC]','Node 126 - Neural architecture of the murine and human temporomandibular joint')

#'Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]',

net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]', 'Node 72 - COMEBACK')

net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 74 - HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes')

net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 76 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 77 - Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain')

net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 79 - Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 80 - Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 81 - The Spine Phenome Project: Enabling Technology for Personalized Medicine')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 82 - UM MRC BACPAC')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 83 - Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 84 - Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 86 - Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 50 - SPRINT: Signature for Pain Recovery IN Teens')

net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 60 - Validation of a novel cortical biomarker signature for pain')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 87 - A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 88 - EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 89 - EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy')

net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 92 - Optimizing the use of ketamine to reduce chronic postsurgical pain')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 51 - SurgeryPal')

net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 52 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma')

net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 98 - Group-based Integrative Pain Management: A multi-level approach to address intersectional stigma and social isolation in diverse primary care safety net patients with chronic pain')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 99 - Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination')

net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 54 - Latinx Children and Surgery')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 100 - Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain')

net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 103 - Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 104 - Pain Care At Home to Amplify Function (Pain CHAMP)')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 105 - Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder')

net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 107 - Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 108 - From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects')


net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 110 - Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 111 - Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management')

net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 115 - Total-body PET for assessing myofascial pain')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 116 - Harvard PRECISION Human Pain Center')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 117 - Human Nociceptor and Spinal Cord Molecular Signature Center')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 70 - INTERCEPT: Integrated Research Center for human Pain Tissues')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]', 'Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial')        
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 118 - Group-Based Mindfulness for Patients with Chronic Low Back Pain in the Primary Care')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 119 - Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 120 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 121 - Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial')

net.add_edge('Node 28 - Patient Health Questionnaire - 2 items [PHQ-2]','Node 126 - Neural architecture of the murine and human temporomandibular joint')

#'Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]',

net.add_edge('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]','Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery')
net.add_edge('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]','Node 90 - A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain')
net.add_edge('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]','Node 61 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)')
net.add_edge('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]','Node 94 - RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches')

net.add_edge('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]','Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial')
net.add_edge('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]','Node 96 - Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study')
net.add_edge('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]','Node 97 - Equity Using Interventions for Pain and Depression (EQUIPD)')
net.add_edge('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]','Node 53 - Integrative Training Program for Pediatric Sickle Cell Pain')
net.add_edge('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]', 'Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial')
net.add_edge('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]','Node 114 - Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain')
net.add_edge('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]','Node 123 - Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)')

net.add_edge('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]','Node 125 - Mapping the joint-nerve interactome of the knee')

#'Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]',
net.add_edge('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain')

net.add_edge('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 73 - Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain')

net.add_edge('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 78 - Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain')
          
net.add_edge('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 84 - Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury')
net.add_edge('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 91 - Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder')
             
net.add_edge('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 95 - Wake Forest NCORP Research Base')
             
net.add_edge('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 101 - A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis')
net.add_edge('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 102 - Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial')
net.add_edge('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder')
net.add_edge('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 106 - Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)')
             
net.add_edge('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 109 - Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain')
        
net.add_edge('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 112 - MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome')
net.add_edge('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 113 - Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain')
          
net.add_edge('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]','Node 122 - Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adult')
             
net.add_edge('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]', 'Node 124 - Innervation of the knee and TMJ')

#'Node 31 - Pediatric Quality of Life Inventory [PedsQL]',

net.add_edge('Node 31 - Pediatric Quality of Life Inventory [PedsQL]','Node 50 - SPRINT: Signature for Pain Recovery IN Teens')
net.add_edge('Node 31 - Pediatric Quality of Life Inventory [PedsQL]','Node 51 - SurgeryPal')
net.add_edge('Node 31 - Pediatric Quality of Life Inventory [PedsQL]','Node 52 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma')
net.add_edge('Node 31 - Pediatric Quality of Life Inventory [PedsQL]','Node 53 - Integrative Training Program for Pediatric Sickle Cell Pain')
net.add_edge('Node 31 - Pediatric Quality of Life Inventory [PedsQL]','Node 54 - Latinx Children and Surgery')


# 'Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]',

net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]', 'Node 72 - COMEBACK')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain') 
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 73 - Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 74 - HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 75 - Imaging Epigenetic Dysregulation in Patients with Low Back Pain')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 76 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 77 - Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 78 - Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 79 - Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 80 - Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 81 - The Spine Phenome Project: Enabling Technology for Personalized Medicine')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 82 - UM MRC BACPAC')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 83 - Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 84 - Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 86 - Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy')

net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 60 - Validation of a novel cortical biomarker signature for pain')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 87 - A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 88 - EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 89 - EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 90 - A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 91 - Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 92 - Optimizing the use of ketamine to reduce chronic postsurgical pain')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 93 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 94 - RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 95 - Wake Forest NCORP Research Base')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 96 - Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study')

net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 97 - Equity Using Interventions for Pain and Depression (EQUIPD)')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 98 - Group-based Integrative Pain Management: A multi-level approach to address intersectional stigma and social isolation in diverse primary care safety net patients with chronic pain')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 99 - Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination')

net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 100 - Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 101 - A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 102 - Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 103 - Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 104 - Pain Care At Home to Amplify Function (Pain CHAMP)')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 105 - Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 106 - Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 107 - Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 108 - From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 67 - RM1 Project 1: Evaluating the specific role of endogenous opioids as the mechanism underlying tAN-based analgesia in healthy individuals')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 68 - RM1 Project 2: Determining the independent and synergistic effects of transcutaneous auricular neurostimulation (tAN) on direct brain activation in healthy individuals')          
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 109 - Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 110 - Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 111 - Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 112 - MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 113 - Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 114 - Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 115 - Total-body PET for assessing myofascial pain')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 116 - Harvard PRECISION Human Pain Center')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 117 - Human Nociceptor and Spinal Cord Molecular Signature Center')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 70 - INTERCEPT: Integrated Research Center for human Pain Tissues')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]', 'Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial')        
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 118 - Group-Based Mindfulness for Patients with Chronic Low Back Pain in the Primary Care')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 119 - Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 120 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 121 - Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 122 - Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adult')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 123 - Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 124 - Innervation of the knee and TMJ')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 125 - Mapping the joint-nerve interactome of the knee')
net.add_edge('Node 32 - PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]','Node 126 - Neural architecture of the murine and human temporomandibular joint')

#'Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]',

net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]', 'Node 72 - COMEBACK')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain') 
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 73 - Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 74 - HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 75 - Imaging Epigenetic Dysregulation in Patients with Low Back Pain')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 76 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 77 - Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 78 - Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 79 - Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 80 - Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 81 - The Spine Phenome Project: Enabling Technology for Personalized Medicine')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 82 - UM MRC BACPAC')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 83 - Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 84 - Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 86 - Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy')

net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 60 - Validation of a novel cortical biomarker signature for pain')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 87 - A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 88 - EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 89 - EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 90 - A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 91 - Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 92 - Optimizing the use of ketamine to reduce chronic postsurgical pain')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 93 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 94 - RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 95 - Wake Forest NCORP Research Base')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 96 - Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study')

net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 97 - Equity Using Interventions for Pain and Depression (EQUIPD)')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 98 - Group-based Integrative Pain Management: A multi-level approach to address intersectional stigma and social isolation in diverse primary care safety net patients with chronic pain')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 99 - Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination')

net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 100 - Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 101 - A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 102 - Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 103 - Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 104 - Pain Care At Home to Amplify Function (Pain CHAMP)')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 105 - Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 106 - Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 107 - Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 108 - From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 67 - RM1 Project 1: Evaluating the specific role of endogenous opioids as the mechanism underlying tAN-based analgesia in healthy individuals')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 68 - RM1 Project 2: Determining the independent and synergistic effects of transcutaneous auricular neurostimulation (tAN) on direct brain activation in healthy individuals')          
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 109 - Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 110 - Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 111 - Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 112 - MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 113 - Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 114 - Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 115 - Total-body PET for assessing myofascial pain')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 116 - Harvard PRECISION Human Pain Center')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 117 - Human Nociceptor and Spinal Cord Molecular Signature Center')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 70 - INTERCEPT: Integrated Research Center for human Pain Tissues')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial')        
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 118 - Group-Based Mindfulness for Patients with Chronic Low Back Pain in the Primary Care')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 119 - Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 120 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 121 - Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 122 - Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adult')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 123 - Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 124 - Innervation of the knee and TMJ')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 125 - Mapping the joint-nerve interactome of the knee')
net.add_edge('Node 33 - PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]','Node 126 - Neural architecture of the murine and human temporomandibular joint')

#'Node 34 - Sleep Duration Question [SD - Adult or Peds]',

net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 72 - COMEBACK')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain') 
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 73 - Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 74 - HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 75 - Imaging Epigenetic Dysregulation in Patients with Low Back Pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 76 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 77 - Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 78 - Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 79 - Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 80 - Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 81 - The Spine Phenome Project: Enabling Technology for Personalized Medicine')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 82 - UM MRC BACPAC')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 83 - Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 84 - Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 85 - Discovery of the Biomarker Signature for Neuropathic Corneal Pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 86 - Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy')

net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 60 - Validation of a novel cortical biomarker signature for pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 87 - A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 88 - EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 89 - EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 90 - A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 91 - Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 92 - Optimizing the use of ketamine to reduce chronic postsurgical pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 93 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 94 - RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 95 - Wake Forest NCORP Research Base')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 96 - Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 52 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 97 - Equity Using Interventions for Pain and Depression (EQUIPD)')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 98 - Group-based Integrative Pain Management: A multi-level approach to address intersectional stigma and social isolation in diverse primary care safety net patients with chronic pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 99 - Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination')

net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 100 - Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 101 - A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 102 - Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 103 - Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 104 - Pain Care At Home to Amplify Function (Pain CHAMP)')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 105 - Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 106 - Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 107 - Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 108 - From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 67 - RM1 Project 1: Evaluating the specific role of endogenous opioids as the mechanism underlying tAN-based analgesia in healthy individuals')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 68 - RM1 Project 2: Determining the independent and synergistic effects of transcutaneous auricular neurostimulation (tAN) on direct brain activation in healthy individuals')          
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 109 - Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 110 - Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 111 - Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 112 - MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 113 - Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 114 - Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 115 - Total-body PET for assessing myofascial pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 116 - Harvard PRECISION Human Pain Center')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 117 - Human Nociceptor and Spinal Cord Molecular Signature Center')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 70 - INTERCEPT: Integrated Research Center for human Pain Tissues')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]', 'Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial')        
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 118 - Group-Based Mindfulness for Patients with Chronic Low Back Pain in the Primary Care')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 119 - Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 120 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 121 - Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 122 - Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adult')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 123 - Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 124 - Innervation of the knee and TMJ')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 125 - Mapping the joint-nerve interactome of the knee')
net.add_edge('Node 34 - Sleep Duration Question [SD - Adult or Peds]','Node 126 - Neural architecture of the murine and human temporomandibular joint')


#'Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]'

net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 72 - COMEBACK')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain') 
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 73 - Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 74 - HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 75 - Imaging Epigenetic Dysregulation in Patients with Low Back Pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 76 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 77 - Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 78 - Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 79 - Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 80 - Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 81 - The Spine Phenome Project: Enabling Technology for Personalized Medicine')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 82 - UM MRC BACPAC')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 83 - Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 84 - Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 85 - Discovery of the Biomarker Signature for Neuropathic Corneal Pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 86 - Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy')

net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 60 - Validation of a novel cortical biomarker signature for pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 87 - A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 88 - EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 89 - EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 90 - A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 91 - Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 92 - Optimizing the use of ketamine to reduce chronic postsurgical pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 93 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 94 - RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 95 - Wake Forest NCORP Research Base')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 96 - Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study')

net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 97 - Equity Using Interventions for Pain and Depression (EQUIPD)')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 98 - Group-based Integrative Pain Management: A multi-level approach to address intersectional stigma and social isolation in diverse primary care safety net patients with chronic pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 99 - Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination')

net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 100 - Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 101 - A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 102 - Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 103 - Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 104 - Pain Care At Home to Amplify Function (Pain CHAMP)')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 105 - Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 106 - Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 107 - Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 108 - From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 67 - RM1 Project 1: Evaluating the specific role of endogenous opioids as the mechanism underlying tAN-based analgesia in healthy individuals')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 68 - RM1 Project 2: Determining the independent and synergistic effects of transcutaneous auricular neurostimulation (tAN) on direct brain activation in healthy individuals')          
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 109 - Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 110 - Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 111 - Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 112 - MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 113 - Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 114 - Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 115 - Total-body PET for assessing myofascial pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 116 - Harvard PRECISION Human Pain Center')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 117 - Human Nociceptor and Spinal Cord Molecular Signature Center')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 70 - INTERCEPT: Integrated Research Center for human Pain Tissues')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]', 'Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial')        
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 118 - Group-Based Mindfulness for Patients with Chronic Low Back Pain in the Primary Care')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 119 - Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 120 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 121 - Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 122 - Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adult')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 123 - Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 124 - Innervation of the knee and TMJ')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 125 - Mapping the joint-nerve interactome of the knee')
net.add_edge('Node 35 - Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]','Node 126 - Neural architecture of the murine and human temporomandibular joint')

# connecting study names to their respective research programs

net.add_edge('Node 36 - Biomarkers','Node 50 - SPRINT: Signature for Pain Recovery IN Teens')
net.add_edge('Node 36 - Biomarkers','Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache')  
net.add_edge('Node 36 - Biomarkers','Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience')
net.add_edge('Node 36 - Biomarkers','Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy')
net.add_edge('Node 36 - Biomarkers','Node 60 - Validation of a novel cortical biomarker signature for pain')
net.add_edge('Node 36 - Biomarkers','Node 84 - Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury')
net.add_edge('Node 36 - Biomarkers','Node 85 - Discovery of the Biomarker Signature for Neuropathic Corneal Pain')
net.add_edge('Node 36 - Biomarkers','Node 86 - Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers')


              
net.add_edge('Node 37 - ERN','Node 51 - SurgeryPal')
net.add_edge('Node 37 - ERN','Node 61 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)')
net.add_edge('Node 37 - ERN','Node 90 - A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain')
net.add_edge('Node 37 - ERN', 'Node 91 - Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder')
net.add_edge('Node 37 - ERN', 'Node 92 - Optimizing the use of ketamine to reduce chronic postsurgical pain')
net.add_edge('Node 37 - ERN', 'Node 93 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)')
net.add_edge('Node 37 - ERN', 'Node 94 - RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches')
net.add_edge('Node 37 - ERN', 'Node 95 - Wake Forest NCORP Research Base')
              
              
              
net.add_edge('Node 38 - Health Equity in Pain Management','Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial')
net.add_edge('Node 38 - Health Equity in Pain Management','Node 52 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma') 
net.add_edge('Node 38 - Health Equity in Pain Management','Node 53 - Integrative Training Program for Pediatric Sickle Cell Pain')
net.add_edge('Node 38 - Health Equity in Pain Management','Node 54 - Latinx Children and Surgery')
net.add_edge('Node 38 - Health Equity in Pain Management','Node 65 - PAINED: Project Addressing INequities in the Emergency Department')
net.add_edge('Node 38 - Health Equity in Pain Management','Node 96 - Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study')
net.add_edge('Node 38 - Health Equity in Pain Management','Node 97 - Equity Using Interventions for Pain and Depression (EQUIPD)')
net.add_edge('Node 38 - Health Equity in Pain Management','Node 98 - Group-based Integrative Pain Management: A multi-level approach to address intersectional stigma and social isolation in diverse primary care safety net patients with chronic pain')
net.add_edge('Node 38 - Health Equity in Pain Management','Node 99 - Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination')
net.add_edge('Node 38 - Health Equity in Pain Management','Node 100 - Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain')
              
net.add_edge('Node 39 - A2CPS','Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery')
              
              
net.add_edge('Node 40 - BACPAC','Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain')
net.add_edge('Node 40 - BACPAC','Node 72 - COMEBACK')
net.add_edge('Node 40 - BACPAC','Node 73 - Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain')
net.add_edge('Node 40 - BACPAC','Node 74 - HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes')
net.add_edge('Node 40 - BACPAC','Node 75 - Imaging Epigenetic Dysregulation in Patients with Low Back Pain')
net.add_edge('Node 40 - BACPAC','Node 76 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 40 - BACPAC','Node 77 - Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain')
net.add_edge('Node 40 - BACPAC','Node 78 - Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain')
net.add_edge('Node 40 - BACPAC','Node 79 - Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity')
net.add_edge('Node 40 - BACPAC','Node 80 - Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC')
net.add_edge('Node 40 - BACPAC','Node 81 - The Spine Phenome Project: Enabling Technology for Personalized Medicine')
net.add_edge('Node 40 - BACPAC','Node 82 - UM MRC BACPAC')
net.add_edge('Node 40 - BACPAC','Node 83 - Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation')
              

              
net.add_edge('Node 41 - IMPOWR','Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder')
net.add_edge('Node 41 - IMPOWR','Node 102 - Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial')
net.add_edge('Node 41 - IMPOWR','Node 103 - Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)')
net.add_edge('Node 41 - IMPOWR','Node 104 - Pain Care At Home to Amplify Function (Pain CHAMP)')
net.add_edge('Node 41 - IMPOWR','Node 105 - Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder')
net.add_edge('Node 41 - IMPOWR','Node 106 - Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)')
net.add_edge('Node 41 - IMPOWR','Node 107 - Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)')
              


net.add_edge('Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief', 'Node 67 - RM1 Project 1: Evaluating the specific role of endogenous opioids as the mechanism underlying tAN-based analgesia in healthy individuals')
net.add_edge('Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief','Node 68 - RM1 Project 2: Determining the independent and synergistic effects of transcutaneous auricular neurostimulation (tAN) on direct brain activation in healthy individuals')
net.add_edge('Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief','Node 108 - From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects')
net.add_edge('Node 42 - Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief','Node 109 - Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain')
              
              
net.add_edge('Node 43 - MPS- Myofascial Pain','Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management')
net.add_edge('Node 43 - MPS- Myofascial Pain','Node 110 - Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain')
net.add_edge('Node 43 - MPS- Myofascial Pain','Node 111 - Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain')
net.add_edge('Node 43 - MPS- Myofascial Pain','Node 112 - MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome')
net.add_edge('Node 43 - MPS- Myofascial Pain','Node 113 - Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain')
net.add_edge('Node 43 - MPS- Myofascial Pain','Node 114 - Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain')
net.add_edge('Node 43 - MPS- Myofascial Pain','Node 115 - Total-body PET for assessing myofascial pain')
              
              
              
              
net.add_edge('Node 44 - PRECISION Human Pain', 'Node 70 - INTERCEPT: Integrated Research Center for human Pain Tissues')
net.add_edge('Node 44 - PRECISION Human Pain','Node 116 - Harvard PRECISION Human Pain Center')
net.add_edge('Node 44 - PRECISION Human Pain','Node 117 - Human Nociceptor and Spinal Cord Molecular Signature Center')
              
              
net.add_edge('Node 45 - PRISM', 'Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial')
net.add_edge('Node 45 - PRISM','Node 118 - Group-Based Mindfulness for Patients with Chronic Low Back Pain in the Primary Care')
net.add_edge('Node 45 - PRISM','Node 119 - Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain')
net.add_edge('Node 45 - PRISM','Node 120 - Nonpharmacologic Pain Management for Lumbar Surgery')
net.add_edge('Node 45 - PRISM','Node 121 - Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial')
net.add_edge('Node 45 - PRISM','Node 122 - Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adult')
              
              
              
net.add_edge('Node 46 - HOPE', 'Node 101 - A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis')

              
              
net.add_edge('Node 47 - EPPIC Net', 'Node 87 - A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain')
net.add_edge('Node 47 - EPPIC Net','Node 88 - EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)')
net.add_edge('Node 47 - EPPIC Net','Node 89 - EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy')
              
              
net.add_edge('Node 48 - RE JOIN','Node 123 - Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)')
net.add_edge('Node 48 - RE JOIN','Node 124 - Innervation of the knee and TMJ')
net.add_edge('Node 48 - RE JOIN','Node 125 - Mapping the joint-nerve interactome of the knee')
net.add_edge('Node 48 - RE JOIN','Node 126 - Neural architecture of the murine and human temporomandibular joint')




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
