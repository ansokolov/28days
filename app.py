import os 
import datetime
import csv
import json

i = 0

def initial_menu():
    user_action = input("1. Log In \n" + 
                        "2. Create new user \n" +
                        "3. Create with CSV \n" +
                        "4. Update with CSV \n")

    if user_action == "1":
        user_name = input("What is your name? \n")
        file_name = user_name + ".json" 
        if os.path.isfile(file_name):
            secondary_menu(file_name)
        else: 
            user_choice = input("There is no such a user. Would you like to create new user? \n")
            if user_choice == "Yes":
                initial_menu()
            else:
                exit()

    if user_action == "2":
        user_name = input("What is your name? \n")
        file_name = user_name + ".json" 
        user_profile = open(file_name,"w")

        current_date = datetime.datetime.now()

        filled_profile = {  "name": "",
                            "created_on": "",
                            "words": []}
        filled_profile["name"] = user_name
        filled_profile["created_on"] = current_date.strftime("%Y-%m-%d")

        json.dump(filled_profile, user_profile)
        user_profile.close()
        print("The profile was create successfully. You can log in now.")   

    if user_action == "3":
        user_name = input("What is your name? \n")
        file_name = user_name + ".json" 
        csv_file = open(user_name + ".csv","r")
        csv_data = csv.reader(csv_file, delimiter=";")

        user_profile = open(file_name,"w")

        filled_profile = {  "name": "",
                            "created_on": "",
                            "words": []}
        filled_profile["name"] = user_name
        current_date = datetime.datetime.now()
        filled_profile["created_on"] = current_date.strftime("%Y-%m-%d")
        words = filled_profile["words"]
        word_profile = {"word": "",
                        "sentence": "",
                        "translation": "",
                        "learnt_on": "",
                        "last_repeat": "",
                        "repetitions": ""}

        for row in csv_data: 
            word_profile["word"] = row[0]
            word_profile["sentence"] = row[1]
            word_profile["translation"] = row[2]
            word_profile["learnt_on"] = row[3]
            word_profile["last_repeat"] = row[4]
            word_profile["repetitions"] = row[5]     
            words.append(word_profile)

        json.dump(filled_profile, user_profile)
        user_profile.close()
        print("The profile was create successfully. You can log in now.")   

    if user_action == "4":
        user_name = input("What is your name? \n")
        file_name = user_name + ".json" 
        if os.path.isfile(file_name):
            user_file = open(file_name,"r")
            user_profile = user_file.read()
            user_data = json.loads(user_profile)
            user_file.close()

            csv_file = open(user_name + ".csv","r")
            csv_data = csv.reader(csv_file, delimiter=";")

            user_file = open(file_name,"w")
            words = user_data["words"]
            word_profile = {"word": "",
                            "sentence": "",
                            "translation": "",
                            "learnt_on": "",
                            "last_repeat": "",
                            "repetitions": ""}

            for row in csv_data: 
                word_profile["word"] = row[0]
                word_profile["sentence"] = row[1]
                word_profile["translation"] = row[2]
                word_profile["learnt_on"] = row[3]
                word_profile["last_repeat"] = row[4]
                word_profile["repetitions"] = row[5]     
                words.append(word_profile)

            json.dump(user_data, user_file)
            user_file.close()
            print("The profile was updated successfully.")
        else: 
            user_choice = input("There is no such a user. Would you like to create new user? \n")
            if user_choice == "Yes":
                initial_menu()
            else:
                exit()

def secondary_menu(file_name):   
    user_choice = input("1. Repeat Words \n" + 
                        "2. Add new words \n")
    if user_choice == "1":
        repeat_words(file_name)
    elif user_choice == "2":
        new_word(file_name)
    else:
        print("There is no such option.")
        secondary_menu(file_name) 

def words_menu(user_profile):
    user_choice = input("1. Add new word \n" + 
                        "2. Back \n")
    if user_choice == "1":
        new_word(user_profile)
    elif user_choice == "2":
        secondary_menu(user_profile)
    else:
        print("There is no such option.")
        words_menu(user_profile) 

def new_word(file_name):
    user_profile = open(file_name,"r")
    data = user_profile.read()
    user_profile.close()
    serialized_data = json.loads(data)
    word_profile = {"word": "",
                    "sentence": "",
                    "translation": "",
                    "learnt_on": "",
                    "last_repeat": "",
                    "repetitions": ""}

    word = input("What is the word you learnt? \n")
    sentence = input("In which sentence did you see that word? \n")
    translation = input("What does the word mean? \n")

    words = serialized_data["words"]
    word_profile["word"] = word
    word_profile["sentence"] = sentence
    word_profile["translation"] = translation
    current_date = datetime.datetime.now()
    word_profile["learnt_on"] = current_date.strftime("%Y-%m-%d")
    word_profile["repetitions"] = 0
    words.append(word_profile)

    user_profile = open(file_name,"w+")
    json.dump(serialized_data, user_profile)
    user_profile.close()

    print("The word has been successfully saved.")
    user_choice = input("1. Add new word \n" + 
                        "2. Back \n")
    if user_choice == "1":
        new_word(file_name)
    elif user_choice == "2":
        secondary_menu(user_profile)
    else:
        print("There is no such option.")
        secondary_menu(user_profile) 

def repeat_words(file_name):
    user_profile = open(file_name,"r")
    data = user_profile.read()
    user_profile.close()
    serialized_data = json.loads(data)
    words = serialized_data["words"]
    i = 0
    while i < len(words):
        word = words[i]
        count = 0
        if int(word["repetitions"]) == 0:
            last_repeat = word["learnt_on"]
            calculated_date = calculate_date_difference(1)
            if calculated_date == last_repeat:
                word, i, count = show_sentence(word, i, count)
            else:
                i += 1

        elif int(word["repetitions"]) < 7 and word["repetitions"] > 0:
            last_repeat = word["last_repeat"]
            calculated_date = calculate_date_difference(1)
            if calculated_date == last_repeat:
                word, i, count = show_sentence(word, i, count)
            else:
                i += 1

        elif int(word["repetitions"]) == 7:
            last_repeat = word["last_repeat"]
            calculated_date = calculate_date_difference(7)
            if calculated_date == last_repeat:
                word, i, count = show_sentence(word, i, count)
            else:
                i += 1
        
        elif int(word["repetitions"]) == 8:
            last_repeat = word["last_repeat"]
            calculated_date = calculate_date_difference(14)
            if calculated_date == last_repeat:
                word, i, count = show_sentence(word, i, count)
            else:
                i += 1
        
        else:
            i += 1

    if count == 0:
        print("There is no words for today. Come tomorrow.")
    else:
        print("That's all the words for today.")
        user_profile = open(file_name,"w+")
        json.dump(serialized_data, user_profile)
        user_profile.close()

def calculate_date_difference(difference):
    current_date = datetime.datetime.now()
    calculated_date = current_date - datetime.timedelta(days=difference)
    calculated_date = calculated_date.strftime("%Y-%m-%d")
    return calculated_date

def show_sentence(word, i, count):
    print(word["sentence"])
    word["repetitions"] = int(word["repetitions"]) + 1
    current_date = datetime.datetime.now()
    word["last_repeat"] = current_date.strftime("%Y-%m-%d")
    count += 1
    i += 1
    return word, i, count

print("Welcome to 28 days words learning app. This app is based on the Anton Brejestovski's word  learning method. \n")
initial_menu()
