from tqdm import tqdm

class EnumeratingTokenizer:
    def __init__(self, text):
        self.text = text

    def tokenize_text_by_enumerating(self):
        self.unique_symbols = sorted(set(self.text))
        word_to_tokode = dict([(y, x) for (x, y) in tqdm(enumerate(self.unique_symbols), total=len(self.unique_symbols))])
        text_digitized = [word_to_tokode[x] for x in tqdm(self.text)]
        return text_digitized
