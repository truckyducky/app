import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
from IPython.core.display import display, HTML

network = Network(notebook = True, cdn_resources="remote",height="900px", width="90%", select_menu = True, filter_menu=True,font_color="white", bgcolor = "black")


network.add_node('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]',  
              title = 'Brief Pain Inventory - Severity [BPI-Severity]', color = '#e07c3e')

network.add_nodes(['Node 50 - SPRINT: Signature for Pain Recovery IN Teens', 'Node 51 - SurgeryPal', 'Node 54 - Latinx Children and Surgery',
                   'Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery', 
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
    label = ['SPRINT: Signature for Pain Recovery IN Teens', 'SurgeryPal', 'Latinx Children and Surgery', 'Transition from Acute to Chronic Pain After Thoracic Surgery',
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
    title = ['SPRINT: Signature for Pain Recovery IN Teens', 'SurgeryPal', 'Latinx Children and Surgery', 'Transition from Acute to Chronic Pain After Thoracic Surgery',
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
    shape = ['text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text', 'text','text','text']

)

# adding connections for 'Node 14 - Brief Pain Inventory - Severity [BPI-Severity]'
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery')
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain') 
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache')
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience')
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy')
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 60 - Validation of a novel cortical biomarker signature for pain') 
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 61 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)')
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial')
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 63 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma')
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 64 - Integrative Training Program for Pediatric Sickle Cell Pain')
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 65 - PAINED: Project Addressing INequities in the Emergency Department')
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder')
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 67 - RM1 Project 1: Evaluating the specific role of endogenous opioids as the mechanism underlying tAN-based analgesia in healthy individuals')
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 68 - RM1 Project 2: Determining the independent and synergistic effects of transcutaneous auricular neurostimulation (tAN) on direct brain activation in healthy individuals')
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management')
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 70 - INTERCEPT: Integrated Research Center for human Pain Tissues')
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial')
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 50 - SPRINT: Signature for Pain Recovery IN Teens')
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]','Node 51 - SurgeryPal')
network.add_edge('Node 14 - Brief Pain Inventory - Severity [BPI-Severity]', 'Node 54 - Latinx Children and Surgery')
        
network.show("edges.html")


# Save and read graph as HTML file (on Streamlit Sharing)
try:
    path = '/tmp'
    network.save_graph(f'{path}/pyvis_graph.html')
    HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')

# Save and read graph as HTML file (locally)
except:
    path = '/html_files'
    network.save_graph(f'{path}/pyvis_graph.html')
    HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')

# Load HTML file in HTML component for display on Streamlit page
components.html(HtmlFile.read(), height=1000, width = 1000)
