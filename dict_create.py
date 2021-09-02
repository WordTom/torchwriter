import os
"""将所有文章中的字，符号提取出来，去重后存入一个txt文档中"""

DIR_PATH = r"novels"
VOCAB_FILE = r"Vocab.txt"
dict_set = set()
file_counter = 0
for index, filename in enumerate(os.listdir(DIR_PATH)):
    file_counter = file_counter + 1
    file_abs_path = os.path.join(DIR_PATH, filename)
    print(file_abs_path)
    with open(file_abs_path, "r+", encoding="utf-8")as f:
        reading_char = f.read(1)
        while reading_char:
            if reading_char == '\n' or reading_char == '\r' or reading_char == ' ':
                # dict_set,add('ISEPJ')
                pass
            else:
                dict_set.add(reading_char)
            reading_char = f.read(1)
print(file_counter)
with open(VOCAB_FILE, "W+", encoding="utf-8")as f:
    f.write("[START] [SEQ] [UNK] [PAD] [END]")
    f.write("".join(dict_set))
    f.flush()
