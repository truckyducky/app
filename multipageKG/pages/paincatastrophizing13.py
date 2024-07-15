import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
from pyvis.network import Network
from IPython.core.display import display, HTML

net = Network(notebook = True, cdn_resources="remote",height="900px", width="90%", select_menu = True, filter_menu=True,font_color="white", bgcolor = "black")

net.add_node('Node 22 - Pain Catastrophizing Questionnaire - 13 Items [PCS-13]',
              title = 'Pain Catastrophizing Questionnaire - 13 Items [PCS-13]', color = '#e07c3e')

net.add_nodes(['Node 75 - Imaging Epigenetic Dysregulation in Patients with Low Back Pain',
               'Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache',
    'Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience',
    'Node 84 - Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury',
    'Node 86 - Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers',
    'Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy',
    'Node 60 - Validation of a novel cortical biomarker signature for pain',
    'Node 90 - A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain',
    'Node 91 - Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder',
    'Node 92 - Optimizing the use of ketamine to reduce chronic postsurgical pain',
    'Node 93 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)',
    'Node 95 - Wake Forest NCORP Research Base',
    'Node 96 - Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study',
    'Node 97 - Equity Using Interventions for Pain and Depression (EQUIPD)',
    'Node 99 - Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination',
    'Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder',
    'Node 105 - Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder',
    'Node 108 - From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects',
    'Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management',
    'Node 112 - MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome',
    'Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial',
    'Node 122 - Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adult',
    'Node 124 - Innervation of the knee and TMJ',
    'Node 125 - Mapping the joint-nerve interactome of the knee'],
              title = ['Node 75 - Imaging Epigenetic Dysregulation in Patients with Low Back Pain',
                       'Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache',
    'Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience',
    'Node 84 - Discovery of Biomarker Signatures Prognostic for Neuropathic Pain after Acute Spinal Cord Injury',
    'Node 86 - Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers',
    'Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy',
    'Node 60 - Validation of a novel cortical biomarker signature for pain',
    'Node 90 - A sequenced-strategy for improving outcomes in patients with knee osteoarthritis pain',
    'Node 91 - Integrated Treatment for Veterans with Co-Occurring Chronic Pain and Opioid Use Disorder',
    'Node 92 - Optimizing the use of ketamine to reduce chronic postsurgical pain',
    'Node 93 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)',
    'Node 95 - Wake Forest NCORP Research Base',
    'Node 96 - Addressing the chronic pain epidemic among older adults in underserved community center; The GetActive+ study',
    'Node 97 - Equity Using Interventions for Pain and Depression (EQUIPD)',
    'Node 99 - Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination',
    'Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder',
    'Node 105 - Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder',
    'Node 108 - From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects',
    'Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management',
    'Node 112 - MRI-based quantitative characterization of impaired myofascial interface properties in myofascial pain syndrome',
    'Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial',
    'Node 122 - Pragmatic Trial of Acupuncture for Chronic Low Back Pain in Older Adult',
    'Node 124 - Innervation of the knee and TMJ',
    'Node 125 - Mapping the joint-nerve interactome of the knee'],
    shape = ['text','text','text','text','text',
            'text','text','text','text','text',
            'text','text','text','text','text',
            'text','text','text','text','text',
            'text','text','text','text']

)

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

net.repulsion(spring_strength = 0)       

net.show("network.html")

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
        
