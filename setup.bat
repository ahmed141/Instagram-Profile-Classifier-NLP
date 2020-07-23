@ECHO OFF
TITLE NER System Initialization
ECHO Please Wait... Insatalling Requirements

pip install -r requirements.txt
python -m deeppavlov install ner_ontonotes_bert_mult

PAUSE