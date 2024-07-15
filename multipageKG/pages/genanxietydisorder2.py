import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
from pyvis.network import Network
from IPython.core.display import display, HTML

net = Network(notebook = True, cdn_resources="remote",height="900px", width="90%", select_menu = True, filter_menu=True,font_color="white", bgcolor = "black")


net.add_node('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]',  
              title = 'Generalized Anxiety Disorder - 2 Items [GAD-2]', color = '#e07c3e')


net.add_nodes(['COMEBACK', 'Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain',
               'HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes',
               'Nonpharmacologic Pain Management for Lumbar Surgery',
               'Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain',
               'Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain',
               'Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity',
               'Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC',
               'The Spine Phenome Project: Enabling Technology for Personalized Medicine',
               'UM MRC BACPAC', "Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation",
               "Biomarker Signature to Predict the Persistence of Post-Traumatic Headache", 
               "Discovery of the Biomarker Signature for Neuropathic Corneal Pain",
               "Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers",
               "Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy",
               "SPRINT: Signature for Pain Recovery IN Teens",
               "Validation of a novel cortical biomarker signature for pain",
               "A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain",
               "EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)",
               "EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy",
               "Optimizing the use of ketamine to reduce chronic postsurgical pain",
               "SurgeryPal",
               "Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma",
               "Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination",
               "Integrative Training Program for Pediatric Sickle Cell Pain",
               "Latinx Children and Surgery",
               "Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain",
               "Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)",
               "Pain Care At Home to Amplify Function (Pain CHAMP)",
               "Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder",
               "Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)",
               "From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects",
               "Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain",
               "Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain",
               "HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management",
               "Total-body PET for assessing myofascial pain",
               "Harvard PRECISION Human Pain Center",
               "Human Nociceptor and Spinal Cord Molecular Signature Center",
               "INTERCEPT: Integrated Research Center for human Pain Tissues",
               "Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain",
               "Nonpharmacologic Pain Management for Lumbar Surgery",
               "Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial",
               "Mapping the joint-nerve interactome of the knee",
               "Neural architecture of the murine and human temporomandibular joint"],
    label = ['COMEBACK', 'Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain',
               'HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes',
               'Nonpharmacologic Pain Management for Lumbar Surgery',
               'Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain',
               'Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain',
               'Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity',
               'Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC',
               'The Spine Phenome Project: Enabling Technology for Personalized Medicine',
               'UM MRC BACPAC', "Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation",
               "Biomarker Signature to Predict the Persistence of Post-Traumatic Headache", 
               "Discovery of the Biomarker Signature for Neuropathic Corneal Pain",
               "Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers",
               "Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy",
               "SPRINT: Signature for Pain Recovery IN Teens",
               "Validation of a novel cortical biomarker signature for pain",
               "A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain",
               "EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)",
               "EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy",
               "Optimizing the use of ketamine to reduce chronic postsurgical pain",
               "SurgeryPal",
               "Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma",
               "Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination",
               "Integrative Training Program for Pediatric Sickle Cell Pain",
               "Latinx Children and Surgery",
               "Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain",
               "Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)",
               "Pain Care At Home to Amplify Function (Pain CHAMP)",
               "Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder",
               "Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)",
               "From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects",
               "Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain",
               "Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain",
               "HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management",
               "Total-body PET for assessing myofascial pain",
               "Harvard PRECISION Human Pain Center",
               "Human Nociceptor and Spinal Cord Molecular Signature Center",
               "INTERCEPT: Integrated Research Center for human Pain Tissues",
               "Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain",
               "Nonpharmacologic Pain Management for Lumbar Surgery",
               "Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial",
               "Mapping the joint-nerve interactome of the knee",
               "Neural architecture of the murine and human temporomandibular joint"],
    title = ['COMEBACK', 'Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain',
               'HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes',
               'Nonpharmacologic Pain Management for Lumbar Surgery',
               'Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain',
               'Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain',
               'Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity',
               'Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC',
               'The Spine Phenome Project: Enabling Technology for Personalized Medicine',
               'UM MRC BACPAC', "Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation",
               "Biomarker Signature to Predict the Persistence of Post-Traumatic Headache", 
               "Discovery of the Biomarker Signature for Neuropathic Corneal Pain",
               "Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers",
               "Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy",
               "SPRINT: Signature for Pain Recovery IN Teens",
               "Validation of a novel cortical biomarker signature for pain",
               "A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain",
               "EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)",
               "EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy",
               "Optimizing the use of ketamine to reduce chronic postsurgical pain",
               "SurgeryPal",
               "Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma",
               "Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination",
               "Integrative Training Program for Pediatric Sickle Cell Pain",
               "Latinx Children and Surgery",
               "Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain",
               "Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)",
               "Pain Care At Home to Amplify Function (Pain CHAMP)",
               "Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder",
               "Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)",
               "From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects",
               "Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain",
               "Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain",
               "HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management",
               "Total-body PET for assessing myofascial pain",
               "Harvard PRECISION Human Pain Center",
               "Human Nociceptor and Spinal Cord Molecular Signature Center",
               "INTERCEPT: Integrated Research Center for human Pain Tissues",
               "Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain",
               "Nonpharmacologic Pain Management for Lumbar Surgery",
               "Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial",
               "Mapping the joint-nerve interactome of the knee",
               "Neural architecture of the murine and human temporomandibular joint"],
    shape = ['text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text',
            'text','text','text','text','text','text','text','text','text','text','text','text','text','text','text']

)



## add edge connection for 'Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]'




edge_list = ['COMEBACK', 'Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain',
               'HEALing LB3P: Profiling Biomechanical, Biological and Behavioral Phenotypes',
               'Nonpharmacologic Pain Management for Lumbar Surgery',
               'Novel Imaging of Endplate Biomarkers in Chronic Low Back Pain',
               'Proof of Concept Study to Treat Negative Affect in Chronic Low Back Pain',
               'Randomized-controlled trial of virtual reality for chronic lower back pain to improve patient-reported outcomes and physical activity',
               'Technology Research Site for Advanced, Faster Quantitative Imaging for BACPAC',
               'The Spine Phenome Project: Enabling Technology for Personalized Medicine',
               'UM MRC BACPAC', "Wearable nanocomposite sensor system for diagnosing mechanical sources of low back pain and guiding rehabilitation",
               "Biomarker Signature to Predict the Persistence of Post-Traumatic Headache", 
               "Discovery of the Biomarker Signature for Neuropathic Corneal Pain",
               "Mentoring in Discovery and Validation of Clinical Chronic Pain Biomarkers",
               "Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy",
               "SPRINT: Signature for Pain Recovery IN Teens",
               "Validation of a novel cortical biomarker signature for pain",
               "A Study to Evaluate the Safety and Efficacy of CNTX-6970 in Subjects With Knee Osteoarthritis Pain",
               "EPPIC-Net: Novaremed Painful Diabetic Peripheral Neuropathy ISA (EN21-01)",
               "EPPIC-Net: Platform Protocol to Assess Treatments for Painful Diabetic Peripheral Neuropathy",
               "Optimizing the use of ketamine to reduce chronic postsurgical pain",
               "SurgeryPal",
               "Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma",
               "Integrating Nonpharmacologic Strategies for Pain with Inclusion, Respect, and Equity (INSPIRE): Tailored digital tools, telehealth coaching, and primary care coordination",
               "Integrative Training Program for Pediatric Sickle Cell Pain",
               "Latinx Children and Surgery",
               "Partners for Pain & Wellbeing Equity: A Randomized Trial of Community Supported Complementary and Integrative Health Self Management for Back Pain",
               "Intergrated Care for Chronic Pain and Opioid Use Disorder: The IMPOWR Research Center at Montefiore/Einstein (IMPOWR-ME)",
               "Pain Care At Home to Amplify Function (Pain CHAMP)",
               "Randomized Clinical Trial Intervention to Treat Chronic Pain Among Persons Maintained on Methadone for Opioid Use Disorder",
               "Tailored Retention and Engagement for Equitable Treatment of OUD and Pain (TREETOP)",
               "From Nerve to Brain: Toward a Mechanistic Understanding of Spinal Cord Stimulation in Human Subjects",
               "Development and identification of magnetic resonance, electrophysiological, and fiber-optic imaging biomarkers of myofascial pain",
               "Development and Validation of a Noninvasive Multimodal Ultrasound-Based Imaging Biomarker for Myofascial Pain",
               "HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management",
               "Total-body PET for assessing myofascial pain",
               "Harvard PRECISION Human Pain Center",
               "Human Nociceptor and Spinal Cord Molecular Signature Center",
               "INTERCEPT: Integrated Research Center for human Pain Tissues",
               "Hybrid Effectiveness-Implementation Trial of Guided Relaxation and Acupuncture for Chronic Sickle Cell Disease Pain",
               "Nonpharmacologic Pain Management for Lumbar Surgery",
               "Non-pharmacological Options in postoperative Hospital-based And Rehabilitation pain Management (NOHARM) pragmatic clinical trial",
               "Mapping the joint-nerve interactome of the knee",
               "Neural architecture of the murine and human temporomandibular joint"]

for item in edge_list:
    net.add_edge('Node 19 - Generalized Anxiety Disorder - 2 Items [GAD-2]', item)


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

