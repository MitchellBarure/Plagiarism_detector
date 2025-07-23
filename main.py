def read_file(file_path):
    """This function reads the content of a file and returns it as a string allowing us to analyze the file content with the detector"""
    try:
        with open(file_path, 'r') as file:  #Opens the file in read mode
            return file.read()
    except FileNotFoundError:  #Check that the file exists
        print(f"File not found:{file_path}")
        return ""

#Import String function to handle punctuation in essays
import string

def preprocess(text):
    """Converts text to lowercase, removes punctuation and spilts essay into words"""
    #Convert to lowercase
    text = text.lower()

    #Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    #Split into words
    words = text.split()

    return words  

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

#Confirm that the preprocess function was successful
print("Processed Essay 1 Words:", essay1_words[:10])
print("Processed Essay 2 Words:", essay2_words[:10])



