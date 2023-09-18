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
net = Network(notebook = True, cdn_resources="remote",height="900px", width="90%", select_menu = True, filter_menu=True,font_color="white", bgcolor = "#373a3c") #, heading = "Interactive Network of HEAL Core CDEs")


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

# cde_list = ['Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]', 
#              'Brief Pain Inventory - Interference [BPI-Interference]',
#              'Brief Pain Inventory - Severity [BPI-Severity]',
#              'Demographics - Adult [Demographics-A]',
#              'Demographics - Adult, Revised [Demographics-A Revised]',
#              'Demographics - Pediatric [Demographics-Peds]',
#              'Demographics - Pediatric, revised [Demographics-Peds Revised]',
#              'Generalized Anxiety Disorder - 2 Items [GAD-2]', 
#              'Generalized Anxiety Disorder - 7 Items [GAD-7]',
#              'NIDA Modified Assist Tool - 2 [NIDA Assist-2 Modified]',
#              'Pain Catastrophizing Questionnaire - 13 Items [PCS-13]', 
#              'Pain Catastrophizing Scale - Parent [PCS-Parent]',
#              'Pain Catastrophizing Scale - Pediatric [PCS-Peds]',
#              'Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]',
#              'Pain, Enjoyment, General Activity [PEG]',
#              'Patient Global Impression of Change [PGIC]',
#              'Patient Health Questionnaire - 2 items [PHQ-2]',
#              'Patient Health Questionnaire - 8 Items [PHQ-8]',
#              'Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]',
#              'Pediatric Quality of Life Inventory [PedsQL]',
#              'PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]',
#              'PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]',
#              'Sleep Duration Question [SD - Adult or Peds]',
#              'Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]']

# # Implement multiselect dropdown menu for option selection (returns a list)
# selected_cdes = st.multiselect('Select HEAL Common Core CDEs to visualize', cde_list)


# # Set info message on initial site load
multi = ''Interactive Knowledge Graph illustrates the CDEs into three main categories: General Health, Demographics, and Research Programs. 
These nodes are magenta and ellipsed-shaped. General Health divides up into six subcategories: Patient Health, Pain, Sleep, Substance Use, Mental Health, and Quality of Life. 
Demographics are separated based on age range: Adults, Adolescent, and Pediatric. These subcategories are purple ellipsed-shaped nodes. 
Each CDE is connected to a single or multiple subcategories depending on their purpose/application. The orange circle nodes represent each Core CDE. 
The size of the nodes depicts the count of the Core CDEs used.
The size gradients contain four ranges from least to most: 0-19, 20-49, 50-79, and 80-100 counts. 
As for the Research Programs, they are purple and triangle-shaped nodes. Respectively, each research program is connected to multiple Core CDEs.
With this interactive knowledge graph, you can click on individual nodes to highlight specific ones or search a node using its ID. 
If ID is unknown, you can search by node/edge and color/font/id/label/shape/size. 
As a final note, the interactive knowledge graph is still being refined to improve efficient searches and logic. '''
st.markdown(multi)


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
