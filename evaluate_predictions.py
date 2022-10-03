import sys


fi = open(sys.argv[1], "r")


first = True
guess_dict = {}
for line in fi:
    if first:
        first = False
        continue
    else:
        parts = line.strip().split(",")
        guess_dict[int(parts[0])] = parts[1]

fi = open("/content/data/WANLI/test.txt", "r")

correct_dict = {}
first = True

label_list = []
i = 0
for line in fi:
    i += 1
    if first:
        labels = line.strip().split("\t")
        idIndex = labels.index("pairID")
        first = False
        continue
    else:
        parts = line.strip().split("\t")
        # while len(parts) < len(labels):
        #     parts.append("")
        this_line_dict = {}
        for index, label in enumerate(labels):
            if label == "pairID":
                continue
            else:
                this_line_dict[label] = parts[index]

        correct_dict[parts[idIndex]] = this_line_dict
        
        if this_line_dict["gold"] not in label_list:
            label_list.append(this_line_dict["gold"])

ent_correct_count = 0
ent_incorrect_count = 0
neu_correct_count = 0
neu_incorrect_count = 0
con_correct_count = 0
con_incorrect_count = 0

for key in correct_dict:
    traits = correct_dict[key]
    correct = traits["gold"]
    guess = guess_dict[int(key)]

    if guess == correct:
        if correct == "entailment":
            ent_correct_count += 1
        elif correct == "neutral":
            neu_correct_count += 1
        else:
            con_correct_count += 1
    else:
        if correct == "entailment":
            ent_incorrect_count += 1
        elif correct == "neutral":
            neu_incorrect_count += 1
        else:
            con_incorrect_count += 1
    
corrects_count = 0
overall = 0
print("")
print("Final results:")

correct = ent_correct_count
incorrect = ent_incorrect_count
total = correct + incorrect
percent = correct * 1.0 / total
corrects_count += correct
overall += total
print("entailment" + ": " + str(percent))

correct = neu_correct_count
incorrect = neu_incorrect_count
total = correct + incorrect
percent = correct * 1.0 / total
corrects_count += correct
overall += total
print("neutral" + ": " + str(percent))

correct = con_correct_count
incorrect = con_incorrect_count
total = correct + incorrect
percent = correct * 1.0 / total
corrects_count += correct
overall += total
print("contradiction" + ": " + str(percent))

print("")

print("Overall WANLI Test Evaluation Accuracy: " + str(corrects_count/overall))
