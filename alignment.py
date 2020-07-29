import csv 
from collections import defaultdict

class Alignment:
    """
    Reads the csv into a dictionary 
    """
    def __init__(self, filename="gloss_alignment.csv"):
        self.alignment_dict = self.csv_to_dict(filename)
     
    def csv_to_dict(self, filename): 
        alignment_dict = defaultdict(list)
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader: 
                for (k, v) in row.items():
                    alignment_dict[k].append(v)
        return alignment_dict
    
    """
    For a single gloss token (output from eng2gloss), returns the index of corresponding gloss token in pose2gloss vocab
    - index used to lookup the corresponding symbol/video in Liz.data
    """
    def find_match(self, token): 
        if word in self.alignment_dict['Eng2GlossVocab']:
            return self.alignment_dict['Pose2Idx'][self.alignment_dict['Eng2GlossVocab'].index(token)] 
        else: 
            return 0 # shouldn't happen 
        
"""
Example usage 
a = Alignment()
print(a.alignment_dict.keys())
print(a.find_match("A")) --- 11
print(pose2idx['A']) ------- 11
"""
