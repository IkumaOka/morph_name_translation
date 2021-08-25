import json

tf = open("translation_table.json", "r")
transition_table_list = json.load(tf)
tf.close()
print(transition_table_list)