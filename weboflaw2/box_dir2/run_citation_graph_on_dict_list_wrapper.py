'''
Created on Jun 30, 2020

@author: charles
'''

''' Emulate one line shell script used to call run_citation_graph_on_directory_list.py
    shell script run_on_scotus consists of the following line:
    python3.6 run_citation_graph_on_directory_list.py scotus.list scotus_c '''

import run_citation_graph_on_directory_list as run_cite_graph

def main():
    run_cite_graph.main([__name__, 'scotus.list', 'scotus_c']);

if __name__ == '__main__':
    main()
