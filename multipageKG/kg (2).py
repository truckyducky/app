import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import networkx as nx
from collections import Counter
from pyvis.network import Network
from IPython.core.display import display, HTML

# Read the new CSV file
descriptors_data = pd.read_csv("BRIM Metadata.csv")

# Convert DataFrame to a list of lists with all entries as strings
project_data = descriptors_data.astype(str).values.tolist()

# Define a color mapping for each column header
color_map = {
    'Project #': '#e07c3e',           # Orange
    'Application Type': '#ff0000',    # Red
    'Project Title': '#1f77b4',       # Blue
    'Research Focus Area': '#2ca02c', # Green
    'Administering IC(s)': '#9467bd', # Purple
    'Institution': '#8c564b',         # Brown
    'Investigator': '#e377c2',        # Pink
    'Location': '#7f7f7f',            # Grey
    'Year Awarded': '#bcbd22'         # Yellow
}

# Reverse the color map to map colors to labels
color_name_map = {v: k for k, v in color_map.items()}

# Create a Network graph object
net = Network(notebook=True, width="1000px", height="600px", cdn_resources='remote', font_color='white', bgcolor="black", select_menu=True, filter_menu=True)
st.title('Knowledge Graph of BRIM Projects')

# Add description before presenting the knowledge graph
st.markdown("""
# Understanding Nodes and Edges

- **Nodes**: Aka vertices, are the fundamental units in a graph. They represent entities or objects. Nodes can have properties like size, color, label, etc., which help in identifying or categorizing them. In this context, nodes could be, "Research Focus Area," "Project Title," etc.
- **Edges**: Aka links, represent the connections or relationships between nodes. They define how nodes are related.

For more information on using the filter feature, [explanation below](#selecting-a-node).

# Map Key 

**Node Colors and Shapes:**
- `Project #`: <span style="color:#e07c3e;">&#x25CF;</span> Orange Circle
- `Application Type`: <span style="color:#ff0000;">&#x25CF;</span> Red Circle
- `Project Title`: <span style="color:#1f77b4;">&#x25B2;</span> Blue Triangle
- `Research Focus Area`: <span style="color:#2ca02c;">&#x25A0;</span> Green Circle
- `Administering IC(s)`: <span style="color:#9467bd;">&#x25CF;</span> Purple Circle
- `Institution`: <span style="color:#8c564b;">&#x25CF;</span> Brown Circle
- `Investigator`: <span style="color:#e377c2;">&#x25CF;</span> Pink Circle
- `Location`: <span style="color:#7f7f7f;">&#x25CF;</span> Grey Circle
- `Year Awarded`: <span style="color:#bcbd22;">&#x25CF;</span> Yellow Circle
        
""", unsafe_allow_html=True)

st.sidebar.success("Select a demo above.")

def create_knowledge_graph(data, columns):
    # Flatten the data to get a list of all descriptors
    all_descriptors = [descriptor for entry in data for descriptor in entry[1:]]

    # Calculate the frequency of each descriptor
    descriptor_frequency = Counter(all_descriptors)

    # Scale the size of nodes based on frequency
    max_frequency = max(descriptor_frequency.values())
    scaling_factor = 20  # Adjust the scaling factor as needed

    # Add nodes and edges to the network
    for entry in data:
        # Extract the primary nodes
        project_title = entry[columns.get_loc('Project Title')]
        research_focus_area = entry[columns.get_loc('Research Focus Area')]

        # Add the primary nodes to the network
        net.add_node(project_title, label=project_title, color=color_map['Project Title'], size=10, shape='triangle')
        frequency = descriptor_frequency[research_focus_area]
        node_size = scaling_factor * (frequency / max_frequency)
        net.add_node(research_focus_area, label=research_focus_area, color=color_map['Research Focus Area'], size=node_size, shape='square')

        # Add edges between the primary nodes
        net.add_edge(project_title, research_focus_area)

        # Extract and add the secondary nodes
        secondary_nodes = ['Application Type', 'Institution', 'Investigator', 'Administering IC(s)']
        for attribute in secondary_nodes:
            descriptor = entry[columns.get_loc(attribute)]
            node_color = color_map.get(attribute, '#982568')  # Default to purple if not found
            net.add_node(descriptor, label=descriptor, color=node_color, size=10)
            net.add_edge(project_title, descriptor)
            net.add_edge(research_focus_area, descriptor)

        # Extract and interconnect the remaining nodes with the investigator
        investigator = entry[columns.get_loc('Investigator')]
        remaining_nodes = ['Project #', 'Location', 'Year Awarded']
        for attribute in remaining_nodes:
            descriptor = entry[columns.get_loc(attribute)]
            node_color = color_map.get(attribute, '#982568')  # Default to purple if not found
            net.add_node(descriptor, label=descriptor, color=node_color, size=10)
            net.add_edge(investigator, descriptor)

        # Connect the investigator to the primary nodes
        net.add_edge(investigator, project_title)
        net.add_edge(investigator, research_focus_area)
            
    # Configure physics options
    net.set_options("""
    var options = {
        "nodes": {
            "borderWidth": 1,
            "borderWidthSelected": 2,
            "font": {
                "size": 14,
                "color": "white"
            }
        },
        "edges": {
            "color": {
                "inherit": true
            },
            "smooth": {
                "type": "continuous"
            }
        },
        "physics": {
        "enabled": true,
        "stabilization": {
          "enabled": true,
          "iterations": 2000,
          "updateInterval": 100
        },
        "barnesHut": {
          "gravitationalConstant": -65500,
          "centralGravity": 0.08,
          "springLength": 230,
          "springConstant": 0.04,
          "damping": 0.4
        }
      },
      "interaction": {
        "navigationButtons": true,
        "keyboard": true
      }
    }
    """)
    
    # Generate the HTML content as a string
    html_content = net.generate_html()

# Inject JavaScript to map color codes to descriptive names in dropdown
    html_content = html_content.replace("</body>", """
    <script type="text/javascript">
        var color_name_map = {
            "#e07c3e": "Project #",
            "#ff0000": "Application Type",
            "#1f77b4": "Project Title",
            "#2ca02c": "Research Focus Area",
            "#9467bd": "Administering IC(s)",
            "#8c564b": "Institution",
            "#e377c2": "Investigator",
            "#7f7f7f": "Location",
            "#bcbd22": "Year Awarded"
        };

        function populateColorDropdown() {
            var dropdowns = document.querySelectorAll('select[data-id="filter"]');
            dropdowns.forEach(function(dropdown) {
                for (var i = 0; i < dropdown.options.length; i++) {
                    var option = dropdown.options[i];
                    if (color_name_map[option.value]) {
                        option.text = color_name_map[option.value];
                    }
                }
            });
        }

        window.onload = function() {
            populateColorDropdown();
        };
    </script>
    </body>""")

    # Write the HTML content to a file with utf-8 encoding
    with open('knowledge_graph.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

# Call the function to create the knowledge graph
create_knowledge_graph(project_data, descriptors_data.columns)

# Display the graph in the Streamlit app
html_path = 'knowledge_graph.html'
try:
    with open(html_path, 'r', encoding='utf-8') as HtmlFile:
        html_content = HtmlFile.read()

    components.html(html_content, height=800, width=1000)

except FileNotFoundError:
    st.warning(f"HTML file not found at {html_path}.")
except Exception as e:
    st.error(f"An error occurred while reading the HTML file: {e}")

# Details about filtering 
st.markdown("""
### Selecting a Node

- **Select a Node by ID**:
  - You can use the dropdown menu labeled "Select a Node by ID" to choose a specific node. This will highlight the node and its connections, helping you focus on a particular part of the graph. 
  - See [Guide to Possible Selection Choices below](#guide-to-possible-selection-choices)

- **Select a Network Item (Node)**:
  - When you select "node" from the "Select a network item" dropdown, you can then choose a property and value(s) to filter nodes based on those properties. For example, you might filter nodes to only show those with a specific label or color.

- **Node Properties**:
  - Properties you might filter on include label, color, size, etc.
  - Example: To highlight nodes with a specific research focus area, you can select label and type the specific focus area you're interested in.

### Selecting an Edge

- **Select a Network Item (Edge)**:
  - When you select "edge" from the "Select a network item" dropdown, you can choose properties related to the edges. This is useful for highlighting or filtering specific relationships in the graph.

- **Edge Properties**:
  - Properties for edges might include from (starting node), to (ending node), color, width, etc.
  - Example: You might filter edges to show only those connected to a particular node or of a specific color.

### Filtering and Resetting

- **Filter**:
  - After selecting the node or edge and specifying the properties, clicking the "Filter" button will apply the filter to the graph, highlighting the nodes or edges that match your criteria.

- **Reset Selection**:
  - Clicking "Reset Selection" will clear the current filter, returning the graph to its default state where all nodes and edges are visible.

### Practical Use Case

- Highlight Specific **Nodes**: Let's say you want to highlight nodes related to a specific institution. You would:
  - Select "node" from "Select a network item".
  - Choose label from "Select a property".
  - Enter the institution name in "Select value(s)" and click "Filter".

- Highlight Specific **Edges**: to highlight edges to focus on the pathway:
  - Select "edge" from "Select a network item".
  - Choose 'from' or 'to' in "Select a property".
  - As a general rule-of-thumb, selecting:
    - '**to**' allows you to see the nodes connected to a primary node. For example, selecting a specific "Research Focus Area" in the 'Select value(s)' section shows all nodes connected to this research area.
    - '**from**' allows you to see the connections starting from a primary node (e.g., "Project Title" or "Research Focus Area"). For example, selecting a specific "Project Title" in the 'Select value(s)' section shows all nodes connected from this project. 
""")

# Generate and display the guide table for possible selection choices
st.title('Guide to Possible Selection Choices')

unique_values = {column: descriptors_data[column].unique().tolist() for column in descriptors_data.columns}

for column, values in unique_values.items():
    st.subheader(column)
    for value in values:
        st.write(f"- {value}")
