import pdb
import pyperclip
import string

character_map = {
 ord('\n') : ' ',
 ord('\t') : ' ',
 ord('\r') : None
}


def text_preparation(text):
    # remove character_map  symbols
    text.translate(character_map)

    # remove unnesesery spaces
    text.strip()

    # remove punctuation symbols
    text.translate(string.punctuation)



s_input = input("Введите текст (или нажмите Enter): ")

text_preparation(s_input)

if not s_input :
    s_input = pyperclip.paste()

text_preparation(s_input)

v_words = s_input.split()

v_dimensions = []
v_count = []

#def find_mm_pcs (text)
prev = ""
for i in range(len(v_words)):
    current_element = v_words[i]

    #print(current_element)
    if current_element == "mm":
        v_dimensions.append(prev)

    if current_element == "pcs":
        v_count.append(prev)


    prev = current_element

v_length = []
v_width = []

for i, item in enumerate(v_dimensions):
    if i % 2 == 0:
        v_length.append(item)
    else:
        v_width.append(item)

#pdb.set_trace()

result = []
for i in range (len(v_count)):
    l = v_length[i]
    w = v_width[i]
    c = v_count[i]
    result.append("{}\t{}\t{}\n".format(l, w, c))

#v_t = ['\t'] * len(v_count)
#result = [result for x in zip (v_length, v_width, v_count) for result in x]

print ("hi:\n")

tmp = ''.join([str(x) for x in result]) 
print(tmp)
pyperclip.copy(tmp)

#print(v_length)
#print(v_width)
#print(v_count)
    


