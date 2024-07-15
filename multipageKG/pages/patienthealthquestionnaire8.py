import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
from IPython.core.display import display, HTML

net = Network(notebook = True, cdn_resources="remote",height="900px", width="90%", select_menu = True, filter_menu=True,font_color="white", bgcolor = "black")


net.add_node('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]',
              title='Patient Health Questionnaire - 8 Items [PHQ-8]', color='#e07c3e')

net.add_nodes(["Transition from Acute to Chronic Pain After Thoracic Surgery",
"A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain",
"Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)",
"RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches",
'Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial',
"Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study",
"Equity Using Interventions for Pain and Depression (EQUIPD)",
"Integrative Training Program for Pediatric Sickle Cell Pain",
"Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial",
"Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain",
"Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)",
"Mapping the joint-nerve interactome of the knee"],
              label = ["Transition from Acute to Chronic Pain After Thoracic Surgery",
"A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain",
"Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)",
"RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches",
'Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial',
"Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study",
"Equity Using Interventions for Pain and Depression (EQUIPD)",
"Integrative Training Program for Pediatric Sickle Cell Pain",
"Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial",
"Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain",
"Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)",
"Mapping the joint-nerve interactome of the knee"],
              title = ["Transition from Acute to Chronic Pain After Thoracic Surgery",
"A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain",
"Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)",
"RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches",
'Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial',
"Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study",
"Equity Using Interventions for Pain and Depression (EQUIPD)",
"Integrative Training Program for Pediatric Sickle Cell Pain",
"Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial",
"Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain",
"Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)",
"Mapping the joint-nerve interactome of the knee"],
              shape = ['text', 'text','text','text','text','text',
            'text','text','text','text','text','text']
             )

#'Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]',
edge_list = ["Transition from Acute to Chronic Pain After Thoracic Surgery",
"A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain",
"Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)",
"RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches",
'Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial',
"Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study",
"Equity Using Interventions for Pain and Depression (EQUIPD)",
"Integrative Training Program for Pediatric Sickle Cell Pain",
"Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial",
"Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain",
"Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)",
"Mapping the joint-nerve interactome of the knee"]

for item in edge_list:
    net.add_edge('Node 29 - Patient Health Questionnaire - 8 Items [PHQ-8]', item)
    
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
