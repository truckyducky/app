import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
from IPython.core.display import display, HTML

net = Network(notebook = True, cdn_resources="remote",height="900px", width="90%", select_menu = True, filter_menu=True,font_color="white", bgcolor = "black")

net.add_node('Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]',
              title='Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]', color='#e07c3e')

net.add_nodes(['Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery',
               'Node 72 - COMEBACK',
               'Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain',
               'Node 73 - Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain',
               'Node 74 - HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes',
               'Node 76 - Nonpharmacologic Pain Management for Lumbar Surgery',
               'Node 77 - Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain',
               'Node 78 - Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain',
               'Node 79 - Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity',
               'Node 80 - Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC',
               'Node 81 - The Spine Phenome Project: Enabling Technology for Personalized Medicine',
               'Node 82 - UM MRC BACPAC',
               'Node 83 - Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation',
               'Node 85 - Discovery of the Biomarker Signature for Neuropathic Corneal Pain',
               'Node 87 - A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain',
               'Node 88 - EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)',
               'Node 89 - EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy',
               'Node 94 - RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches',
               'Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial',
               'Node 98 - Group-based Integrative Pain Management: A multi-level approach to address intersectional stigma and social isolation in diverse primary care safety net patients with chronic pain',
               'Node 100 - Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain',
               'Node 101 - A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis',
               'Node 102 - Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial',
               'Node 103 - Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)',
               'Node 104 - Pain Care At Home to Amplify Function (Pain CHAMP)',
               'Node 106 - Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)',
               'Node 107 - Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)',
               'Node 109 - Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain',
               'Node 110 - Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain',
               'Node 111 - Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain',
               'Node 113 - Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain',
               'Node 114 - Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain',
               'Node 115 - Total-body PET for assessing myofascial pain',
               'Node 116 - Harvard PRECISION Human Pain Center',
               'Node 117 - Human Nociceptor and Spinal Cord Molecular Signature Center',
               'Node 118 - Group-Based Mindfulness for Patients with Chronic Low Back Pain in the Primary Care',
               'Node 119 - Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain',
               'Node 120 - Nonpharmacologic Pain Management for Lumbar Surgery',
               'Node 121 - Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial',
               'Node 123 - Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)',
               'Node 126 - Neural architecture of the murine and human temporomandibular joint'],
              title = ['Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery',
               'Node 72 - COMEBACK',
               'Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain',
               'Node 73 - Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain',
               'Node 74 - HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes',
               'Node 76 - Nonpharmacologic Pain Management for Lumbar Surgery',
               'Node 77 - Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain',
               'Node 78 - Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain',
               'Node 79 - Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity',
               'Node 80 - Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC',
               'Node 81 - The Spine Phenome Project: Enabling Technology for Personalized Medicine',
               'Node 82 - UM MRC BACPAC',
               'Node 83 - Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation',
               'Node 85 - Discovery of the Biomarker Signature for Neuropathic Corneal Pain',
               'Node 87 - A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain',
               'Node 88 - EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)',
               'Node 89 - EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy',
               'Node 94 - RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches',
               'Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial',
               'Node 98 - Group-based Integrative Pain Management: A multi-level approach to address intersectional stigma and social isolation in diverse primary care safety net patients with chronic pain',
               'Node 100 - Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain',
               'Node 101 - A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis',
               'Node 102 - Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial',
               'Node 103 - Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)',
               'Node 104 - Pain Care At Home to Amplify Function (Pain CHAMP)',
               'Node 106 - Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)',
               'Node 107 - Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)',
               'Node 109 - Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain',
               'Node 110 - Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain',
               'Node 111 - Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain',
               'Node 113 - Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain',
               'Node 114 - Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain',
               'Node 115 - Total-body PET for assessing myofascial pain',
               'Node 116 - Harvard PRECISION Human Pain Center',
               'Node 117 - Human Nociceptor and Spinal Cord Molecular Signature Center',
               'Node 118 - Group-Based Mindfulness for Patients with Chronic Low Back Pain in the Primary Care',
               'Node 119 - Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain',
               'Node 120 - Nonpharmacologic Pain Management for Lumbar Surgery',
               'Node 121 - Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial',
               'Node 123 - Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)',
               'Node 126 - Neural architecture of the murine and human temporomandibular joint'],
              label = ['Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery',
               'Node 72 - COMEBACK',
               'Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain',
               'Node 73 - Focused Ultrasound Neuromodulation of Dorsal Root Ganglion for Noninvasive Mitigation of Low Back Pain',
               'Node 74 - HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes',
               'Node 76 - Nonpharmacologic Pain Management for Lumbar Surgery',
               'Node 77 - Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain',
               'Node 78 - Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain',
               'Node 79 - Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity',
               'Node 80 - Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC',
               'Node 81 - The Spine Phenome Project: Enabling Technology for Personalized Medicine',
               'Node 82 - UM MRC BACPAC',
               'Node 83 - Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation',
               'Node 85 - Discovery of the Biomarker Signature for Neuropathic Corneal Pain',
               'Node 87 - A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain',
               'Node 88 - EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)',
               'Node 89 - EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy',
               'Node 94 - RESOLVE- Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches',
               'Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial',
               'Node 98 - Group-based Integrative Pain Management: A multi-level approach to address intersectional stigma and social isolation in diverse primary care safety net patients with chronic pain',
               'Node 100 - Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain',
               'Node 101 - A Randomized Clinical Trial to Evaluate Non-Pharmacologic and Pharmacologic Approaches for Reducing Pain and Opioid Use Among Patients Treated with Maintenance Hemodialysis',
               'Node 102 - Healing Opioid Misuse and Pain Through Engagement (HOPE) Trial',
               'Node 103 - Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)',
               'Node 104 - Pain Care At Home to Amplify Function (Pain CHAMP)',
               'Node 106 - Stepped Care for Patients to Optimize Whole Recovery (SC-POWR)',
               'Node 107 - Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)',
               'Node 109 - Understanding the Mechanistic, Neurophysiological, and Antinociceptive Effects of Transcutaneous Auricular Neurostimulation for Treatment of Chronic Pain',
               'Node 110 - Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain',
               'Node 111 - Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain',
               'Node 113 - Multimodal imaging biomarkers for investigating fascia, muscle and vasculature in myofascial pain',
               'Node 114 - Quantifying and Treating Myofascial Dysfunction in Post Stroke Shoulder Pain',
               'Node 115 - Total-body PET for assessing myofascial pain',
               'Node 116 - Harvard PRECISION Human Pain Center',
               'Node 117 - Human Nociceptor and Spinal Cord Molecular Signature Center',
               'Node 118 - Group-Based Mindfulness for Patients with Chronic Low Back Pain in the Primary Care',
               'Node 119 - Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain',
               'Node 120 - Nonpharmacologic Pain Management for Lumbar Surgery',
               'Node 121 - Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial',
               'Node 123 - Comprehensive functional phenotyping of trigeminal neurons innervating temporomandibular joint (TMJ) tissues in male, female and aged mice, primates, and humans with and without TMJ disorders (TMJD)',
               'Node 126 - Neural architecture of the murine and human temporomandibular joint'],
              shape = ['text', 'text','text','text','text','text',
            'text','text','text','text','text',
            'text','text','text','text','text',
            'text','text','text','text','text',
            'text','text','text','text', 'text','text','text','text','text',
            'text','text','text','text','text',
            'text','text','text','text','text','text']
              
              
              
)


#'Node 25 - Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]',

## add edge connection for Node 15 to Study Names

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
        
