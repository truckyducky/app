import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
from IPython.core.display import display, HTML

net = Network(notebook = True, cdn_resources="remote",height="900px", width="90%", select_menu = True, filter_menu=True,font_color="white", bgcolor = "black")


net.add_node('Node 15 - Demographics - Adult [Demographics-A]',  
              title = 'Demographics - Adult [Demographics-A]', color = '#e07c3e')

net.add_nodes(['Node 55 - Transition from Acute to Chronic Pain After Thoracic Surgery', 
               'Node 56 - Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain', 
               'Node 57 - Biomarker Signature to Predict the Persistence of Post-Traumatic Headache',  
               'Node 58 - Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience',
               'Node 59 - Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy',
               'Node 60 - Validation of a novel cortical biomarker signature for pain', 
               'Node 61 - Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)',
               'Node 62 - Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial',
               'Node 66 - Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder',
               'Node 67 - RM1 Project 1: Evaluating the specific role of endogenous opioids as the mechanism underlying tAN-based analgesia in healthy individuals',
               'Node 68 - RM1 Project 2: Determining the independent and synergistic effects of transcutaneous auricular neurostimulation (tAN) on direct brain activation in healthy individuals',
               'Node 69 - HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management',
               'Node 70 - INTERCEPT: Integrated Research Center for human Pain Tissues',
               'Node 71 - Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial',
               'Node 72 - COMEBACK',
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
    label = ['Transition from Acute to Chronic Pain After Thoracic Surgery', 
               'Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain', 
               'Biomarker Signature to Predict the Persistence of Post-Traumatic Headache',  
               'Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience',
               'Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy',
               'Validation of a novel cortical biomarker signature for pain', 
               'Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)',
               'Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial',
               'Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder',
               'RM1 Project 1: Evaluating the specific role of endogenous opioids as the mechanism underlying tAN-based analgesia in healthy individuals',
               'RM1 Project 2: Determining the independent and synergistic effects of transcutaneous auricular neurostimulation (tAN) on direct brain activation in healthy individuals',
               'HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management',
               'INTERCEPT: Integrated Research Center for human Pain Tissues',
               'Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial','COMEBACK',
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
    title = ['Transition from Acute to Chronic Pain After Thoracic Surgery', 
               'Development, Evaluation and Translation of Robotic Apparel for Alleviating Low Back Pain', 
               'Biomarker Signature to Predict the Persistence of Post-Traumatic Headache',  
               'Discovery and Analytical Validation of Inflammatory Bio-Signatures of the Human Pain Experience',
               'Multi-Omic Biomarkers for Neuropathic Pain Secondary to Chemotherapy',
               'Validation of a novel cortical biomarker signature for pain', 
               'Pain Response Evaluation of a Combined Intervention to Cope Effectively (PRECICE)',
               'Achieving Equity through SocioCulturally-informed, Digitally-Enabled Cancer Pain managemeNT" (ASCENT) Clinical Trial',
               'Implementation and Effectiveness of Mindfulness Oriented Recovery Enhancement as an Adjunct to Methadone Treatment for Opioid Use Disorder',
               'RM1 Project 1: Evaluating the specific role of endogenous opioids as the mechanism underlying tAN-based analgesia in healthy individuals',
               'RM1 Project 2: Determining the independent and synergistic effects of transcutaneous auricular neurostimulation (tAN) on direct brain activation in healthy individuals',
               'HEAL Initiative: Developing Quantitative Imaging and Other Relevant Biomarkers of Myofascial Tissues for Clinical Pain Management',
               'INTERCEPT: Integrated Research Center for human Pain Tissues',
               'Fibromyalgia TENS in Physical Therapy Study (TIPS):an embedded pragmatic clinical trial','COMEBACK',
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
    shape = ['text','text','text','text','text','text','text','text',
             'text','text','text','text','text','text','text','text','text','text','text','text','text','text',
             'text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text','text',
             'text','text','text','text','text','text','text','text','text','text','text','text','text','text',
            'text','text','text','text','text','text','text','text','text','text','text','text','text', 'text']

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
