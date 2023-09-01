word_list = "D:/Projects/udd-practice/data/sowpods.txt"
# Please give me a list of every 100th word in the file.
with open(word_list, 'r') as file:
    words = file.readlines()
result = []
x = range(1, len(words))

count = 0
for word in words:
    count += 1
    if (count % 100) == 0:
        result.append(word.strip())
print(result)