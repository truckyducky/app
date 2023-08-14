{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 240,
   "id": "9149a703-3fa6-42ce-b4f5-bcc39a1949a5",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import streamlit.components.v1 as components\n",
    "import pandas as pd\n",
    "import networkx as nx\n",
    "from pyvis.network import Network\n",
    "from IPython.core.display import display, HTML"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 241,
   "id": "831f7677-163c-4d7b-aebc-a89bbaee273c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "edges.html\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"95%\"\n",
       "            height=\"900px\"\n",
       "            src=\"edges.html\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x7f96a97dde20>"
      ]
     },
     "execution_count": 241,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "net = Network(notebook = True, cdn_resources=\"remote\",height=\"900px\", width=\"95%\", select_menu = True, filter_menu=True,font_color=\"white\", bgcolor = \"#373a3c\", heading = \"Interactive Network of the HEAL Core CDEs\")\n",
    "\n",
    "\n",
    "#add categorical/subcategorical nodes\n",
    "net.add_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],\n",
    "    label = ['General Health',\n",
    "             'Patient Health',\n",
    "             'Pain',\n",
    "             'Sleep',\n",
    "             'Substance Use',\n",
    "             'Mental Health',\n",
    "             'Quality of Life',\n",
    "             'Demographics', \n",
    "             'Adults', \n",
    "             'Adolescent', \n",
    "             'Pediatric'],\n",
    "    color = ['#982568', '#532565','#532565', '#532565', '#532565', '#532565', '#532565','#982568','#532565', '#532565','#532565'],\n",
    "    size = [60, 30, 30 ,30, 30, 30, 60, 30, 30, 30, 30],\n",
    "    shape = ['ellipse','ellipse','ellipse','ellipse','ellipse','ellipse','ellipse','ellipse','ellipse','ellipse','ellipse']\n",
    "\n",
    ")\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "#net.show_buttons(filter_ = ['physics','nodes','edges','layout','interaction'])\n",
    "\n",
    "\n",
    "net.show('edges.html',local = False)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 242,
   "id": "c2c3d38a-284a-4f94-a833-90a4fb206322",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "edges.html\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"95%\"\n",
       "            height=\"900px\"\n",
       "            src=\"edges.html\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x7f96a958aaf0>"
      ]
     },
     "execution_count": 242,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#adding nodes about common CDEs\n",
    "\n",
    "net.add_nodes([12, 13, 14, 15, 16, 17, 18, 19, 20, 21,22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35],\n",
    "    label = ['Adolescent Sleep Wake Scale - Short Form + Sleep Pattern/Duration [ASWS-SF + Sleep Duration]', \n",
    "             'Brief Pain Inventory - Interference [BPI-Interference]',\n",
    "             'Brief Pain Inventory - Severity [BPI-Severity]',\n",
    "             'Demographics - Adult [Demographics-A]',\n",
    "             'Demographics - Adult, Revised [Demographics-A Revised]',\n",
    "             'Demographics - Pediatric [Demographics-Peds]',\n",
    "             'Demographics - Pediatric, revised [Demographics-Peds Revised]',\n",
    "             'Generalized Anxiety Disorder - 2 Items [GAD-2]', \n",
    "             'Generalized Anxiety Disorder - 7 Items [GAD-7]',\n",
    "             'NIDA Modified Assist Tool - 2 [NIDA Assist-2 Modified]',\n",
    "             'Pain Catastrophizing Questionnaire - 13 Items [PCS-13]', \n",
    "             'Pain Catastrophizing Scale - Parent [PCS-Parent]',\n",
    "             'Pain Catastrophizing Scale - Pediatric [PCS-Peds]',\n",
    "             'Pain Catastrophizing Scale - Short Form 6 [PCS-SF6]',\n",
    "             'Pain, Enjoyment, General Activity [PEG]',\n",
    "             'Patient Global Impression of Change [PGIC]',\n",
    "             'Patient Health Questionnaire - 2 items [PHQ-2]',\n",
    "             'Patient Health Questionnaire - 8 Items [PHQ-8]',\n",
    "             'Patient Health Questionnaire - Full Assessment 9 Items [PHQ-9]',\n",
    "             'Pediatric Quality of Life Inventory [PedsQL]',\n",
    "             'PROMIS Physical Function - Short Form 6b [PROMIS PF-SF6b]',\n",
    "             'PROMIS Sleep Disturbance 6a + Sleep Duration [PROMIS SD-6a + Sleep Duration]',\n",
    "             'Sleep Duration Question [SD - Adult or Peds]',\n",
    "             'Tobacco, Alcohol, Prescription Medication, and Other Substance Use Tool [TAPS-1]'],\n",
    "    color = ['#e07c3e', '#e07c3e','#e07c3e', '#e07c3e', '#e07c3e', '#e07c3e', '#e07c3e','#e07c3e','#e07c3e', '#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e','#e07c3e'],\n",
    "    size = [20, 40, 40, 60, 20, 20, 20, 40, 40, 20, 40, 20, 20, 40, 60, 60, 40, 20, 20, 20, 60, 60, 60, 60]\n",
    ")\n",
    "\n",
    "\n",
    "net.show('edges.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 243,
   "id": "b1c2c3e3-0e37-498b-b755-9d9aab44010c",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "edges.html\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"95%\"\n",
       "            height=\"900px\"\n",
       "            src=\"edges.html\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x7f96a96187c0>"
      ]
     },
     "execution_count": 243,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#adding connections\n",
    "\n",
    "net.add_edges([\n",
    "    (1,2),(1,3),(1,4),(1,5),(1,6),(1,7),\n",
    "    (2,28),(2,29),(2,30),\n",
    "    (3,13),(3,14),(3,22),(3,23),(3,24),(3,25),\n",
    "    (4,12),(4,33),(4,34),\n",
    "    (5, 21),(5, 35),\n",
    "    (6, 19),(6,20),(6,27),\n",
    "    (7, 31),(7,26),\n",
    "    (8, 9),(8, 10),(8,11),\n",
    "    (9, 15),(9, 16),(9,23),\n",
    "    (10, 12),\n",
    "    (11, 17),(11,18),\n",
    "    (12,4),(11,24),\n",
    "    \n",
    "]\n",
    ")\n",
    "\n",
    "\n",
    "net.show_buttons(filter_ = ['physics','nodes','edges','layout','interaction'])\n",
    "net.show(\"edges.html\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 244,
   "id": "74ecf931-4b84-4104-8f3c-775172d32f0f",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Add Legend Nodes --- pyvis doesn't have node legend function available, continue to insert fixed nodes in different shape to create a legend\n",
    "#net.add_node(35, label='Less than 50', color = 'yellow', shape = 'triangle', physics = False)\n",
    "#net.add_node(36, label = 'More than 50', color = 'orange', shape = 'triangle',physics = False)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "#net.show('edges.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 245,
   "id": "87d6b513-d2a7-42ce-a227-c411f420af9e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "edges.html\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"95%\"\n",
       "            height=\"900px\"\n",
       "            src=\"edges.html\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x7f96a97ba9a0>"
      ]
     },
     "execution_count": 245,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#adding the research programs\n",
    "net.add_node(36, label='Biomarkers', color = '#532565', shape = 'triangle', size = 25)\n",
    "net.add_node(37, label = 'ERN', color = '#532565', shape = 'triangle', size = 25)\n",
    "net.add_node(38, label = 'Health Equity in Pain Management', color = '#532565', shape = 'triangle', size = 25)\n",
    "net.add_node(39, label = 'A2CPS', color = '#532565', shape = 'triangle', size = 15)\n",
    "net.add_node(40, label = 'BACPAC', color = '#532565', shape = 'triangle', size = 20)\n",
    "net.add_node(41, label = 'IMPOWR', color = '#532565', shape = 'triangle', size = 20)\n",
    "net.add_node(42, label = 'Interdisciplinary Teams to Elucidate the Mechanisms of Device-Based Pain Relief', color = '#532565', shape = 'triangle', size = 20)\n",
    "net.add_node(43, label = 'MPS- Myofascial Pain', color = '#532565', shape = 'triangle', size = 20)\n",
    "net.add_node(44, label = 'PRECISION Human Pain', color = '#532565', shape = 'triangle', size = 15)\n",
    "net.add_node(45, label = 'PRISM', color = '#532565', shape = 'triangle', size = 20)\n",
    "net.add_node(46, label = 'HOPE', color = '#532565', shape = 'triangle', size = 15)\n",
    "net.add_node(47, label = 'EPPIC Net', color = '#532565', shape = 'triangle', size = 15)\n",
    "net.add_node(48, label = 'RE JOIN', color = '#532565', shape = 'triangle', size = 15)\n",
    "net.add_node(49, label = 'Research Programs', color = '#982568', shape = 'ellipse')\n",
    "\n",
    "\n",
    "net.show(\"edges.html\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 246,
   "id": "137fe64e-b5e1-4d6d-bbf7-b461dbc711a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "edges.html\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"95%\"\n",
       "            height=\"900px\"\n",
       "            src=\"edges.html\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x7f96a9534dc0>"
      ]
     },
     "execution_count": 246,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# adding connections for third subcategory \"research programs\" to each research program\n",
    "net.add_edges([\n",
    "    (49,36),(49,37),(49,38),(49,39),(49,40),(49,41),(49,42),(49,43),(49,44),(49,45),(49,46),(49,47),(49,48)\n",
    "    \n",
    "]\n",
    ")\n",
    "\n",
    "\n",
    "net.show_buttons(filter_ = ['physics','nodes','edges','layout','interaction'])\n",
    "net.show(\"edges.html\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 247,
   "id": "bf72abb8-23c2-428a-8432-d1b8adc5828b",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "edges.html\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"95%\"\n",
       "            height=\"900px\"\n",
       "            src=\"edges.html\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x7f96a656b370>"
      ]
     },
     "execution_count": 247,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#adding connections for the research programs to CDEs\n",
    "\n",
    "net.add_edges([\n",
    "    (12,36),(12,37),(12,38),\n",
    "    (13,36),(13,37),(13,38),(13,39),(13,40),(13,41),(13,42),(13,43),(13,44),(13,45),\n",
    "    (14,36),(14,37),(14,38),(14,39),(14,40),(14,41),(14,42),(14,43),(14,44),(14,45),\n",
    "    (15,36),(15,37),(15,38),(15,39),(15,40),(15,41),(15,42),(15,43),(15,44),(15,45),(15,46),(15,47),(15,48),\n",
    "    (16,38),\n",
    "    (17,36),(17,37),(17,38),\n",
    "    (18,38),\n",
    "    (19,36),(19,37),(19,38),(19,40),(19,41),(19,42),(19,43),(19,44),(19,45),(19,47),(19,48),\n",
    "    (20,36),(20,37),(20,38),(20,39),(20,40),(20,41),(20,42),(20,43),(20,45),(20,46),(20,48),\n",
    "    (21,36),(21,37),(21,38),\n",
    "    (22,36),(22,37),(22,38),(22,40),(22,41),(22,42),(22,43),(22,45),(22,48),\n",
    "    (23,36),(23,37),(23,38),\n",
    "    (24,36),(24,37),(24,38),\n",
    "    (25,36),(25,37),(25,38),(25,39),(25,40),(25,41),(25,42),(25,43),(25,44),(25,45),(25,46),(25,47),(25,48),\n",
    "    (26,36),(26,37),(26,38),(26,39),(26,40),(26,41),(26,42),(26,43),(26,44),(26,45),(26,46),(26,47),(26,48),\n",
    "    (27,36),(27,37),(27,38),(27,39),(27,40),(27,41),(27,42),(27,43),(27,44),(27,45),(27,46),(27,47),(27,48),\n",
    "    (28,36),(28,37),(28,38),(28,40),(28,41),(28,42),(28,43),(28,44),(28,45),(28,47),(28,48),\n",
    "    (29,37),(29,38),(29,39),(29,43),(29,45),(29,48),\n",
    "    (30,36),(30,37),(30,40),(30,41),(30,42),(30,43),(30,45),(30,46),(30,48),\n",
    "    (31,36),(31,37),(31,38),\n",
    "    (32,36),(32,37),(32,38),(32,39),(32,40),(32,41),(32,42),(32,43),(32,44),(32,45),(32,46),(32,47),(32,48),\n",
    "    (33,36),(33,37),(33,38),(33,39),(33,40),(33,41),(33,42),(33,43),(33,44),(33,45),(33,46),(33,47),(33,48),\n",
    "    (34,36),(34,37),(34,38),(34,39),(34,40),(34,41),(34,42),(34,43),(34,44),(34,45),(34,46),(34,47),(34,48),   \n",
    "    (35,36),(35,37),(35,38),(35,39),(35,40),(35,41),(35,42),(35,43),(35,44),(35,45),(35,46),(35,47),(35,48)   \n",
    "]\n",
    ")\n",
    "\n",
    "\n",
    "net.show_buttons(filter_ = ['physics','nodes','edges','layout','interaction'])\n",
    "net.show(\"edges.html\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 248,
   "id": "603f6566-6777-4f5e-b610-619b3d1abfa9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "edges.html\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"95%\"\n",
       "            height=\"900px\"\n",
       "            src=\"edges.html\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x7f96a9632dc0>"
      ]
     },
     "execution_count": 248,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "net.repulsion(spring_strength = 0)\n",
    "\n",
    "net.show(\"edges.html\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 252,
   "id": "9e654f4f-21fb-4aa5-8402-3ca01781979a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save and read graph as HTML file (on Streamlit Sharing)\n",
    "try:\n",
    "    path = '/users/trucpham/downloads'\n",
    "    net.save_graph(f'{path}/edges.html')\n",
    "    HtmlFile = open(f'{path}/edges.html', 'r', encoding='utf-8')\n",
    "\n",
    "# Save and read graph as HTML file (locally)\n",
    "except:\n",
    "    path = '/users/trucpham/html_files'\n",
    "    net.save_graph(f'{path}/edges.html')\n",
    "    HtmlFile = open(f'{path}/edges.html', 'r', encoding='utf-8')\n",
    "\n",
    "# Load HTML file in HTML component for display on Streamlit page\n",
    "    components.html(HtmlFile.read(), height=435)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "55c6c0f5-5e69-4906-9143-6f397993f4bd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
