NLTK Trigram Text Generator

This Python script uses the Natural Language Toolkit (NLTK) library to generate random sentences based on a trigram model. It reads a text file and tokenizes it into words, then uses these words to create trigrams. It stores these trigrams and their associated frequencies in dictionaries, and uses these dictionaries to generate new sentences.

How It Works

The script takes as input a text file and uses the NLTK library's WhitespaceTokenizer function to tokenize the file into individual words. It then uses the trigrams function to generate a list of trigrams, which are sequences of three consecutive words from the text.

A trigram dictionary is created, where each key is a pair of words from a trigram, and the value is a list of words that follow this pair in the text. For each pair of words, the frequency of each following word is calculated and stored in another dictionary.

The text_generator function generates a given number of sentences. Each sentence starts with a random capitalised word pair from the trigram dictionary that does not end with a punctuation mark. It then appends a randomly chosen word from the list of words that follow this pair in the text, weighted by their frequencies. This process is repeated until the sentence reaches at least seven words and ends with a punctuation mark.

Usage

Before running the script, ensure that you have installed the required libraries: nltk and collections. You can install these using pip:

bash
Copy code
pip install nltk
Then, you can simply run the script in a Python environment. When prompted, provide the path to a text file.

The output will be ten generated sentences based on the trigram model of the provided text.

Future Improvements

Currently, the script generates sentences of at least seven words. This number could be made configurable. Other improvements could include support for different types of n-grams (e.g., bigrams, 4-grams), error handling for non-existent files or empty texts, and using command-line arguments for input. Contributions are welcome!

Disclaimer

This script is for educational purposes only. Always respect the rights of the content creators. Do not use it to generate text from copyrighted content without permission.
