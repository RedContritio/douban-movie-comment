import os

DATA_BASE_DIR = os.path.join('..', 'data')

DATA_PRESET_DIR = os.path.join(DATA_BASE_DIR, 'preset')

DATA_PROCESSED_DIR = os.path.join(DATA_BASE_DIR, 'processed')

DATA_MODEL_DIR = os.path.join(DATA_BASE_DIR, 'model')

DATA_TEXT_SEQUENCES_PATH = os.path.join(DATA_PROCESSED_DIR, 'text_sequences.pkl')

DATA_LABELS_PATH = os.path.join(DATA_PROCESSED_DIR, 'labels.pkl')

DATA_W2V_DIR = os.path.join(DATA_PROCESSED_DIR, 'w2v')

DATA_W2V_VECTOR_PATH = os.path.join(DATA_W2V_DIR, 'vector.tsv')

DATA_W2V_META_PATH = os.path.join(DATA_W2V_DIR, 'metadata.tsv')

for (k, v) in list(locals().items()):
    if k.endswith('_DIR') and not os.path.exists(v):
        os.mkdir(v)

class CustomIterator:
    def __init__(self, dataset, operator = lambda x: x):
        self.dataset = dataset
        self.operator = operator
    
    def __iter__(self):
        for line in self.dataset:
            yield self.operator(line)