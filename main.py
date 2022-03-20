from bi_lstm_crf.app import WordsTagger

model = WordsTagger(model_dir="model_dir")
tags, sequences = model(["besoin de infirmiere à mtl"])  # CHAR-based model
print(tags)
# [["B", "B", "I", "B", "B-LOC", "I-LOC", "I-LOC", "I-LOC", "I-LOC", "B", "I", "B", "I"]]
print(sequences)
# [['市', '领导', '到', ('成都', 'LOC'), ...]]

# model([["市", "领导", "到", "成都", ...]])  # WORD-based model
