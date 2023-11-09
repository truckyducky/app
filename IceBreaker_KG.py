import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import networkx as nx
from collections import Counter
from pyvis.network import Network
from IPython.core.display import display, HTML


descriptors_data = pd.read_csv("HEAL icebreaker kg 11_04_23.csv")
df = pd.DataFrame(descriptors_data, columns = ["Text"])


array_of_descriptors = np.array(df)
list_of_ppl_descriptors = array_of_descriptors.tolist()


formatted_data = []

for i in range(0, len(list_of_ppl_descriptors), 6):
    person_and_descriptors = list_of_ppl_descriptors[i:i+6]
    person_and_descriptors = [item[0] if len(item) == 1 else item for item in person_and_descriptors]
    formatted_data.append(person_and_descriptors)

# Print the formatted data
# for entry in formatted_data:
#     print(entry)

net = Network(notebook=True, width="1000px", height="600px", cdn_resources='remote', font_color='white', bgcolor="black")

def create_knowledge_graph(data):

    # Flatten the data to get a list of all descriptors
    all_descriptors = [descriptor for entry in data for descriptor in entry[1:]]

    # Calculate the frequency of each descriptor
    descriptor_frequency = Counter(all_descriptors)

    # Scale the size of nodes based on frequency
    max_frequency = max(descriptor_frequency.values())
    scaling_factor = 20  # Adjust the scaling factor as needed

    # Add nodes and edges to the network
    for entry in data:
        person = entry[0]
        net.add_node(person, color='#e07c3e')

        for descriptor in entry[1:]:
            frequency = descriptor_frequency[descriptor]
            node_size = scaling_factor * (frequency / max_frequency)
            net.add_node(descriptor, color='#982568', size=node_size)
            net.add_edge(person, descriptor)

    # Save and show the network
    return net.show('ice_breaker.html', local=False)

create_knowledge_graph(formatted_data)


# Save and read graph as HTML file (on Streamlit Sharing)
try:
    path = '/tmp'
    net.save_graph(f'{path}/ice_breaker.html')
    HtmlFile = open(f'{path}/ice_breaker.html', 'r', encoding='utf-8')

    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=1000, width=1000)

except FileNotFoundError:
    st.warning("HTML file not found.")
except Exception as e:
    st.error(f"An error occurred: {e}")
finally:
    HtmlFile.close()



# # Save and read graph as HTML file (on Streamlit Sharing)
# try:
#     path = '/tmp'
#     net.save_graph(f'{path}/ice_breaker.html')
#     HtmlFile = open(f'{path}/ice_breaker.html', 'r', encoding='utf-8')

# Save and read graph as HTML file (locally)
# except:
#     path = '/html_files'
#     net.save_graph(f'{path}/ice_breaker.html')
#     HtmlFile = open(f'{path}/ice_breaker.html', 'r', encoding='utf-8')

# Load HTML file in HTML component for display on Streamlit page
components.html(HtmlFile.read(), height=1000, width = 1000)

# # Load HTML into HTML component for display on Streamlit
# components.html(HtmlFile.read(), height=800, width=800)
