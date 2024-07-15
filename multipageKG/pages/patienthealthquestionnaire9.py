import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
from IPython.core.display import display, HTML

net = Network(notebook = True, cdn_resources="remote",height="900px", width="90%", select_menu = True, filter_menu=True,font_color="white", bgcolor = "black")

net.add_node('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]',
              title='Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]', color='#e07c3e')

net.add_nodes(["Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain",
"Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain",
"Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain",
"Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury",
"Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder",
"Wake Forest NCORP Research Base",
"A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis",
"Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial",
"Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder",
"Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)",
"Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain",
"MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome",
"Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain",
"Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adults",
"Innervation of the knee and TMJ"],
              title = ["Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain",
"Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain",
"Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain",
"Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury",
"Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder",
"Wake Forest NCORP Research Base",
"A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis",
"Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial",
"Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder",
"Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)",
"Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain",
"MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome",
"Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain",
"Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adults",
"Innervation of the knee and TMJ"],
              label = ["Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain",
"Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain",
"Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain",
"Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury",
"Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder",
"Wake Forest NCORP Research Base",
"A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis",
"Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial",
"Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder",
"Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)",
"Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain",
"MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome",
"Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain",
"Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adults",
"Innervation of the knee and TMJ"],
              shape = ['text', 'text','text','text','text','text',
            'text','text','text','text','text','text','text','text','text']
             )
edge_list = ["Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain",
"Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain",
"Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain",
"Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury",
"Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder",
"Wake Forest NCORP Research Base",
"A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis",
"Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial",
"Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder",
"Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)",
"Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain",
"MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome",
"Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain",
"Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adults",
"Innervation of the knee and TMJ"]

for item in edge_list:
    net.add_edge('Node 30 - Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]', item)

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
