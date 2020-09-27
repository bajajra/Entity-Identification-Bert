import transformers

MAX_LEN = 128
TRAIN_BATCH_SIZE = 32
VALID_BATCH_SIZE = 8
EPOCHS = 5
BASE_MODEL_PATH = "input/bert_base_uncased"
MODEL_PATH = "model.bin"
TRAINING_FILE = "input/dataset.csv"
JSON_FILE = ""
TOKENIZER = transformers.BertTokenizer.from_pretrained(
    BASE_MODEL_PATH,
    do_lower_case = True
)
