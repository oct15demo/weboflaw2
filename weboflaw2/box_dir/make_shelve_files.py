import shelve
import re
import os

# global_versions = False
# filename_to_global_citation_dict = False
# global_citations = False
# party_key_hash = False

def create_global_shelves(file_prefix):
    global global_versions
    global filename_to_global_citation_dict
    global global_citations
    global party_key_hash
    global_versions_filename = file_prefix+'_global_versions.slv'
    fn_to_g_filename = file_prefix+'filename_to_global_citation_dict.slv'
    global_citations_filename = file_prefix+'_global_citations.slv'
    party_key_filename = file_prefix+'_party_key.slv'
    for filename in [global_versions_filename,fn_to_g_filename,
                 global_citations_filename,party_key_filename]:
        if os.path.isfile(filename):
             os.remove(filename)
    global_versions = shelve.open(global_versions_filename,writeback=True)
    filename_to_global_citation_dict = shelve.open(fn_to_g_filename,writeback=True)
    global_citations = shelve.open(global_citations_filename,writeback=True)
    party_key_hash = shelve.open(party_key_filename,writeback=True)
    return(global_versions,filename_to_global_citation_dict,global_citations,party_key_hash)
    
    
