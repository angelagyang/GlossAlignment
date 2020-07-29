import csv 
from collections import defaultdict

class Alignment:
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
    
    def find_match(self, word): 
        return self.alignment_dict['Pose2Idx'][self.alignment_dict['Eng2GlossVocab'].index(word)] 
                                        
