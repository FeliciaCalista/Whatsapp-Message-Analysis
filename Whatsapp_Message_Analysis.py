import matplotlib.pyplot as plt


def return_list(input_list, key):
    tmp_list = []
    for dictionary in input_list:
        tmp_list.append(dictionary[key])
    return tmp_list


def count_list(input_list):
    dictionary = {}
    tmp_list = []
    for item in input_list:
        if item not in tmp_list:
            dictionary[item] = 1
            tmp_list.append(item)
        else:
            dictionary[item] += 1
    return dictionary


def sort_dict(dictionary):
    keys_list = list(dictionary.keys())
    values_list = list(dictionary.values())
    for i in range(len(keys_list)):
        for j in range(i + 1, len(keys_list)):
            if values_list[i] < values_list[j]:
                keys_list[i], keys_list[j] = keys_list[j], keys_list[i]
                values_list[i], values_list[j] = values_list[j], values_list[i]
    tmp_dictionary = {}
    for i in range(len(keys_list)):
        tmp_dictionary[keys_list[i]] = values_list[i]
    return tmp_dictionary


chats = []

with open("Whatsapp Message", "r", encoding="utf-8") as file:
    chats = file.readlines()

# remove \n & clean up
for i in range(len(chats)):
    chats[i] = chats[i][:-1]
    splitted_chats = chats[i].split(" - ")
    date_time = splitted_chats[0].split(", ")
    name_message = splitted_chats[1].split(": ")
    chats[i] = {"date": date_time[0], "time": date_time[1], "name": name_message[0], "message": name_message[1]}

dates_list = return_list(chats, "date")
times_list = return_list(chats, "time")
names_list = return_list(chats, "name")
messages_list = return_list(chats, "message")

# plot 2
name_list_counted = count_list(names_list)
# plot 4
date_list_counted = count_list(dates_list)

# plot 1
date_count_sorted = sort_dict(date_list_counted)

# cut to only three separated chats
three_date_labels = list(date_count_sorted.keys())[:3]

# separate three separated_chats
separated_chats = [[], [], []]

for i in range(len(three_date_labels)):
    for chat in chats:
        if chat["date"] == three_date_labels[i]:
            separated_chats[i].append(chat)

for i in range(len(separated_chats)):
    for j in range(len(separated_chats[i])):
        separated_chats[i][j]['time'] = separated_chats[i][j]['time'].split(":")[0]

hours_lists = [[], [], []]
hours_lists_counted = [[], [], []]


for i in range(3):
    hours_lists[i] = return_list(separated_chats[i], "time")
    hours_lists_counted[i] = count_list(hours_lists[i])

hours_lists_counted_sorted = [{}, {}, {}]

for i in range(3):
    for j in range(24):
        hour = str(j).zfill(2)
        if hour not in hours_lists_counted[i]:
            hours_lists_counted_sorted[i][hour] = 0
        else:
            hours_lists_counted_sorted[i][hour] = hours_lists_counted[i][hour]

print(hours_lists_counted_sorted)

splitted_messages = []

for i in range(len(messages_list)):
    if "<Media omitted>" not in messages_list[i]:
        messages_list[i] = messages_list[i].lower()
        messages_list[i] = messages_list[i].replace('.', '').replace(',', '').replace('?', '').replace('!', '')
        splitted_messages += messages_list[i].split()

splitted_messages_counted = count_list(splitted_messages)
splitted_messages_counted_sorted = sort_dict(splitted_messages_counted)

top_5_words_x = list(splitted_messages_counted_sorted.keys())[0:5]
top_5_words_counted_y = list(splitted_messages_counted_sorted.values())[0:5]

new_canvas = plt.figure(figsize=(12, 6))
fig1 = new_canvas.add_subplot(2, 2, 1)
fig1.set_title('3 busiest days and hours')
fig1.set_ylabel('chats')
fig1.set_xlabel('hours')
fig2 = new_canvas.add_subplot(2, 2, 2)
fig2.set_title('the most to chat')
fig3 = new_canvas.add_subplot(2, 2, 3)
fig3.set_title('5 topics')
fig4 = new_canvas.add_subplot(2, 2, 4)
fig4.set_title('most chats in one week')

fig1.plot(hours_lists_counted_sorted[0].keys(), hours_lists_counted_sorted[0].values(), label=three_date_labels[0])
fig1.plot(hours_lists_counted_sorted[1].keys(), hours_lists_counted_sorted[1].values(), label=three_date_labels[1])
fig1.plot(hours_lists_counted_sorted[2].keys(), hours_lists_counted_sorted[2].values(), label=three_date_labels[2])
fig1.legend()
fig4.bar(date_list_counted.keys(), date_list_counted.values())
fig3.bar(top_5_words_x, top_5_words_counted_y)
fig2.pie(name_list_counted.values(), labels=name_list_counted.keys(), autopct='%1.1f%%')
plt.tight_layout()
plt.show()
