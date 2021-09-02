import os

SRC_DIR = r"novels"
DST_DIR = r"encoded_novels"
VOCAB_FILE = "Vocab.txt"

if not os.path.exists(DST_DIR):
    os.makedirs(DST_DIR)

# open dict_set.txt file
with open(VOCAB_FILE, "r+", encoding="utf-8")as file:
    tokens = file.read().split()

count = 0

for i, filename in enumerate(os.listdir(SRC_DIR)):
    file_abs_path = os.path.join(SRC_DIR, filename)
    print(file_abs_path)

    with open(file_abs_path, "r+", encoding="utf-8") as file:
        # 文章开头标记为 0
        dst_list = ["0"]
        reading_char = file.read(1)
        while reading_char:
            if reading_char == '\n' or reading_char == '\r' or reading_char == '\t' or ord(reading_char) == 12288:
                # 换行，标记为1
                dst_list.append("1")
            elif reading_char == ' ':
                # 如果是空格，标记为3
                dst_list.append("3")
            else:
                try:
                    # 把文章中的字标记为【字典对应的编码】
                    dst_list.append(str(tokens.index(reading_char)))
                except:
                    # 其他情况标记为 2
                    dst_list.append("2")
            # while 循环 结尾句
            reading_char = file.read(1)
    count += 1
    with open(os.path.join(DST_DIR, "{}.txt".format(count)), "w+", encoding="utf-8") as df:
        df.write(" ".join(dst_list))
print(count)
