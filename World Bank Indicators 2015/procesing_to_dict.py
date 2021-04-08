# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 09:53:45 2021

@author: Yefry Lopez
"""
# Define lists2dict()
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values.
    
    
    Args:
        
        list1:(list) The keys for the dictionary
        list2:(list) The values for the dictionary
        
        
    Return:
        
        dictionary
               
    """

    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return rs_dict    

