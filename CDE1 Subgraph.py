#!/usr/bin/env python
# coding: utf-8

# In[20]:


import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
from IPython.core.display import display, HTML


# In[21]:


network = Network(notebook = True, cdn_resources="remote",height="900px", width="90%", select_menu = True, filter_menu=True,font_color="white", bgcolor = "black")

network.show("network.html")


# In[22]:


network.add_node('Node 1 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]',  
              title = 'Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]', color = '#e07c3e')

network.show("network.html")


# In[23]:


#net.add_node('Node 50 - SPRINT: Signature for Pain Recovery IN Teens', label ='SPRINT: Signature for Pain Recovery IN Teens', title = 'SPRINT: Signature for Pain Recovery IN Teens', shape = 'text', group = 1)
network.add_nodes(['Node 2 - SPRINT: Signature for Pain Recovery IN Teens', 'Node 3 - SurgeryPal', 
               'Node 4 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma',  
               'Node 5 - Integrative Training Program for Pediatric Sickle Cell Pain',
               'Node 6 - Latinx Children and Surgery'],
    label = ['SPRINT: Signature for Pain Recovery IN Teens',
             'SurgeryPal',
             'Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma',
             'Integrative Training Program for Pediatric Sickle Cell Pain',
             'Latinx Children and Surgery'],
    title = ['SPRINT: Signature for Pain Recovery IN Teens',
             'SurgeryPal',
             'Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma',
             'Integrative Training Program for Pediatric Sickle Cell Pain',
             'Latinx Children and Surgery'],
    shape = ['text','text','text','text','text']

)

network.show("network.html")


# In[25]:


network.add_edges([
    ('Node 1 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]','Node 2 - SPRINT: Signature for Pain Recovery IN Teens'),
    ('Node 1 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]','Node 3 - SurgeryPal'),
    ('Node 1 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]','Node 4 - Culturally adapted mobile treatment of chronic pain in adolescent survivors of pediatric bone sarcoma'),
    ('Node 1 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]','Node 5 - Integrative Training Program for Pediatric Sickle Cell Pain'),
    ('Node 1 - Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]','Node 6 - Latinx Children and Surgery'),
    
]
)

network.show("edges.html")


# In[ ]:





# In[ ]:




