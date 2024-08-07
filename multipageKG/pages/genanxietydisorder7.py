import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
from pyvis.network import Network
from IPython.core.display import display, HTML

net = Network(notebook = True, cdn_resources="remote",height="900px", width="90%", select_menu = True, filter_menu=True,font_color="white", bgcolor = "black")


net.add_node('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]',  
              title = 'Generalized Anxiety Disorder - 7 Items [GAD-7]', color = '#e07c3e')


net.add_nodes([ "Transition from Acute to Chronic Pain After Thoracic Surgery", 
               "Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain",
               "Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience",
               "Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury",
               "A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain",
               "Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder",
               "Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)",
               "RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches",
               "Wake Forest NCORP Research Base",
               "Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT (ASCENT) Clinical Trial",
               "Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study",
               "Equity Using Interventions for Pain and Depression (EQUIPD)",
               "Group-based Integrative Pain Management: A multi-level approach to address A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis",
               "Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial",
               "Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder",
               "Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)",
               "Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain",
               "MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome",
               "Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain",
               "Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain",
               "Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial",
               "Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adults",
               "Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)",
               "Innervation of the knee and TMJ"],
        label = ["Transition from Acute to Chronic Pain After Thoracic Surgery", 
               "Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain",
               "Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience",
               "Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury",
               "A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain",
               "Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder",
               "Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)",
               "RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches",
               "Wake Forest NCORP Research Base",
               "Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT (ASCENT) Clinical Trial",
               "Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study",
               "Equity Using Interventions for Pain and Depression (EQUIPD)",
               "Group-based Integrative Pain Management: A multi-level approach to address A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis",
               "Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial",
               "Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder",
               "Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)",
               "Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain",
               "MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome",
               "Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain",
               "Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain",
               "Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial",
               "Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adults",
               "Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)",
               "Innervation of the knee and TMJ"],
    title = ["Transition from Acute to Chronic Pain After Thoracic Surgery", 
               "Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain",
               "Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience",
               "Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury",
               "A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain",
               "Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder",
               "Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)",
               "RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches",
               "Wake Forest NCORP Research Base",
               "Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT (ASCENT) Clinical Trial",
               "Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study",
               "Equity Using Interventions for Pain and Depression (EQUIPD)",
               "Group-based Integrative Pain Management: A multi-level approach to address A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis",
               "Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial",
               "Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder",
               "Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)",
               "Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain",
               "MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome",
               "Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain",
               "Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain",
               "Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial",
               "Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adults",
               "Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)",
               "Innervation of the knee and TMJ"],
    shape = ['text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text', 'text','text','text','text']


)

edge_list = ["Transition from Acute to Chronic Pain After Thoracic Surgery", 
               "Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain",
               "Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience",
               "Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury",
               "A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain",
               "Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder",
               "Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)",
               "RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches",
               "Wake Forest NCORP Research Base",
               "Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT (ASCENT) Clinical Trial",
               "Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study",
               "Equity Using Interventions for Pain and Depression (EQUIPD)",
               "Group-based Integrative Pain Management: A multi-level approach to address A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis",
               "Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial",
               "Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder",
               "Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)",
               "Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain",
               "MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome",
               "Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain",
               "Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain",
               "Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial",
               "Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adults",
               "Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)",
               "Innervation of the knee and TMJ"]



for item in edge_list:
    net.add_edge('Node 20 - Generalized Anxiety Disorder - 7 Items [GAD-7]', item)
    
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
        
              


