import tensorflow as tf
from deeppavlov import configs, build_model
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

ner_model = build_model(configs.ner.ner_ontonotes_bert_mult, download=True)

def check_name_existance(text):
    '''
    This function takes a string as input and return True if the string has a name in it, False otherwise 
  
        Parameter(s): 
            text (str): string that contains text to be checked for existence of name
    
        Returns: 
            bool: True if name is present, False otherwise 
    '''
    arr = []
    arr.append(text)
    ner_output = ner_model(arr)[1][0]
    for entity in ner_output:
        if entity == "B-PERSON":
            return True
    return False