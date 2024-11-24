import nltk
from nltk import word_tokenize
from collections import Counter
from data import sentences,prompts
nltk.download('punkt')


def tokenize_sentences(sentences):
    """Tokenizes sentences into lowercase words, filtering out punctuation."""
    return [word_tokenize(sentence.lower()) for sentence in sentences]

def tokenize_question(question):
    """Tokenizes the user's input question, removing punctuation."""
    return word_tokenize(question.lower())

def get_most_relevant_sentence(user_input, sentences):
    # Tokenize both the user input (question) and the provided sentences
    tokenized_input = tokenize_question(user_input)
    tokenized_sentences = tokenize_sentences(sentences)

    # Create a Counter object for the user's input (question)
    input_counter = Counter(tokenized_input)

    max_relevance = 0
    most_relevant_sentence = ""

    for idx, sentence_tokens in enumerate(tokenized_sentences):
        # Create a Counter for each sentence
        sentence_counter = Counter(sentence_tokens)

        # Find the intersection of words between the question and sentence (common words)
        common_keywords = sum((input_counter & sentence_counter).values())

        if common_keywords > max_relevance:
            max_relevance = common_keywords
            most_relevant_sentence = sentences[idx]

    return most_relevant_sentence

# Example usage
while True:
    user_input = input("Enter a prompt related to football: ")
    if user_input.lower() == "exit" or user_input.lower() == "quit":
        print("Goodbye!")
        break

    most_relevant_sentence = get_most_relevant_sentence(user_input, sentences)
    print(most_relevant_sentence)
