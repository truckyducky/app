import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
from IPython.core.display import display, HTML

network = Network(notebook = True, cdn_resources="remote",height="900px", width="90%", select_menu = True, filter_menu=True,font_color="white", bgcolor = "black")

network.add_node('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]',  
              title = 'Brief Pain Inventory - Interference [BPI-Interference]', color = '#e07c3e')

## add study names for Node 13 - Brief Pain Inventory - Interference [BPI-Interference]

network.add_nodes(['Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery', 
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



network.add_edges([
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 60 - Validation of a novel cortical biomarker signature for pain'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 61 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 63 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 64 - Integrative Training Program for Pediatric Sickle Cell Pain'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 65 - PAINED: Project Addressing INequities in the Emergency Department'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 67 - RM1 Project 1: Evaluating the specific role of endogenous opioids as the mechanism underlying tAN-based analgesia in healthy individuals'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 68 - RM1 Project 2: Determining the independent and synergistic effects of transcutaneous auricular neurostimulation (tAN) on direct brain activation in healthy individuals'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 70 - INTERCEPT: Integrated Research Center for human Pain Tissues'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 50 - SPRINT: Signature for Pain Recovery IN Teens'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]','Node 51 - SurgeryPal'),
    ('Node 13 - Brief Pain Inventory - Interference [BPI-Interference]', 'Node 54 - Latinx Children and Surgery')
    
]
)



network.show("edges.html")


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
