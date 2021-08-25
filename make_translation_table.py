import csv
import json

translation_table_list = {}
with open("morph.csv") as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i != 0:
            # 英語名を小文字にして統一。
            eng_morph_name = row[0].lower()
            # 英語名が辞書の中になければ新しく追加。（yellowberryとybも区別されるように設計。）
            if eng_morph_name not in translation_table_list:
                translation_table_list[eng_morph_name] = row[1]

print(translation_table_list)

# jsonファイルとして保存
tf = open("translation_table.json", "w")
json.dump(translation_table_list,tf)
tf.close()