#Import in-built String module to handle punctuation in essays
import string

"""This function reads the content of a file and returns it as a string allowing us to analyze the file content with the detector"""
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:  #Opens the file in read mode
            return file.read()
    except FileNotFoundError:  #Check that the file exists
        print(f"File not found:{file_path}")
        return ""
    if not essay1.strip() or not essay2.strip():
        print("Cannot proceed...one or both essay files are empty!")

"""Converts text to lowercase, removes punctuation and spilts essay into words"""
def preprocess(text):
    #Convert to lowercase
    text = text.lower()

    #Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    #Split into words
    words = text.split()

    return words  

#Returns a lists of words that are found in the essays being compared
def find_common_words(words1, words2):
    #Convert both lists to sets to remove duplicates and allow easy comparison
    set1 = set(words1)
    set2 = set(words2)

    #Find common words
    common = set1.intersection(set2)

    return list(common)

#Calculates the Plagiarism percentage between two essays
def calculate_percentage_plagiarism(words1, words2):
    """Define variables again although they are in def find_common_words because functions have a local scope"""
    set1 = set(words1)
    set2 = set(words2)
    
    if not set1 and not set2: #Prevents a math error (division by zero) if the number of unique words=0
        return 0.0
    
    intersection = set1.intersection(set2)
    union = set1.union(set2)

    percentage = (len(intersection) / len(union)) * 100
    return round(percentage, 2)

#Allows user to search for a specific word in essay1 and essay2
def search_word(word, words1, words2):
    count1 = words1.count(word)
    count2 = words2.count(word)

    if count1 == 0 and count2 == 0:
        print(f"The word '{word}' was not found in either essay.")
        return False
    else:
        print(f"Results for '{word}:'")
        if count1 > 0:
            print(f"Essay 1: {count1} occurrence(s)")
        if count2 > 0:
            print(f"Essay 2: {count2} occurrrence(s)")
            return True

#Defining paths to the essays
essay1_path = "essay_samples/essay1.txt"
essay2_path = "essay_samples/essay2.txt"

essay1 = read_file(essay1_path)
essay2 = read_file(essay2_path)

"""#Confirm that the read_file function was successful
print("Essay 1 preview:", essay1[:100], "\n")
print("Essay 2 preview:", essay2[:100])"""

#Preprocess the essays
essay1_words = preprocess(essay1)
essay2_words = preprocess(essay2)

"""#Confirm that the preprocess function was successful
print("Processed Essay 1 Words:", essay1_words[:10])
print("Processed Essay 2 Words:", essay2_words[:10])"""

#Find and print common words
common_words = find_common_words(essay1_words, essay2_words)
#print(f"Common words ({len(common_words)} found):", common_words)

#List how many times the common word appears in each essay:print("\nFrequency of common words:")
#for word in common_words:
 #   print(f"'{word}': Essay 1 = {essay1_words.count(word)} | Essay 2 = {essay2_words.count(word)}")

#Calculate the plagiarism percentage
plagiarism_percent = calculate_percentage_plagiarism(essay1_words, essay2_words)
print(f"Plagiarism detected: {plagiarism_percent}%")
if plagiarism_percent >= 50:
    print("Plagiarism Detected!")
else:
    print("No Plagiarism Detected.")


#Ask user to search for a specific word
word_to_search = input("\n Enter a word to search for in  both essays:").lower()
search_word(word_to_search, essay1_words, essay2_words)



