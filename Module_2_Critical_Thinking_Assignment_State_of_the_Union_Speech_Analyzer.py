"""
PSEUDOCODE – State of the Union Speech Analyzer

1. Define main function.
2. Set file path to speech text file.
3. Open the file using a context manager and read contents into a string.
4. Clean the text using regular expressions:
      - Remove unwanted punctuation.
      - Preserve letters, numbers, apostrophes, and hyphens.
5. Convert text to lowercase.
6. Split cleaned text into a list of words.
7. Remove standalone hyphen tokens.
8. Calculate:
      - Character count
      - Word count
      - Total word length
      - Average word length
      - Sentence count
      - Average sentence length
9. Display summary statistics in tabular format.
10. Use Counter to compute word frequency distribution.
11. Extract top 20 most frequent words.
12. Display word distribution in tabular format.
13. Extract unique words.
14. Sort words by length in descending order.
15. Select top 10 longest words.
16. Display top 10 longest words in tabular format.
17. Execute main function.
"""

"""
CSC484 Module 2 Critical Thinking Assignment
State of the Union Speech Analyzer

This program reads a State of the Union speech from a text file and
analyzes the following:

- Word count
- Character count
- Average word length
- Average sentence length
- Word frequency distribution
- Top ten longest words

Results are displayed in a clean, tabular console format.
"""

import re
from collections import Counter

def main():
    """
    Executes the State of the Union Speech Analyzer.

    Reads the selected speech file, processes the text,
    computes required metrics, and displays results
    in a structured tabular format.
    """
    file_path = "Obama SOTU Speech 2010.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        speech_text = file.read()

    cleaned_text = re.sub(r"[^A-Za-z0-9'\-]+", " ", speech_text)
    words = cleaned_text.lower().split()

    # Remove standalone hyphens
    words = [word for word in words if word != "-"]

    # Calculates total characters
    character_count = len(speech_text)

    # Calculates total words
    word_count = len(words)

    # Calculates the average length of the words
    total_word_length = sum(len(word) for word in words)
    average_word_length = total_word_length / word_count

    # Calculates the average length of the sentences
    sentence_count = speech_text.count('.') + speech_text.count('!') + speech_text.count('?')
    average_sentence_length = word_count / sentence_count if sentence_count != 0 else 0

    print("\nSpeech Summary")
    print(f"{'Metric':<25}{'Value':>15}")
    print("-" * 40)
    print(f"{'Character Count':<25}{character_count:>15}")
    print(f"{'Word Count':<25}{word_count:>15}")
    print(f"{'Avg Word Length':<25}{average_word_length:>15.2f}")
    print(f"{'Avg Sentence Length':<25}{average_sentence_length:>15.2f}")

    # Calculates word frequency
    word_frequency = Counter(words)
    top_words = word_frequency.most_common(20)

    print("\nWord Distribution (Top 20)")
    print(f"{'Word':<20}{'Count':>10}")
    print("-" * 30)

    for word, count in top_words:
        print(f"{word:<20}{count:>10}")

    # Calculates top ten longest words
    unique_words = set(words)
    top_ten_longest = sorted(unique_words, key=len, reverse=True)[:10]

    print("\nTop Ten Longest Words")
    print(f"{'Rank':<6}{'Word':<25}{'Length':>10}")
    print("-" * 41)

    rank = 1
    for word in top_ten_longest:
        print(f"{rank:<6}{word:<25}{len(word):>10}")
        rank += 1

# Ensures the program runs only when executed directly,
# and not when imported as a module.
if __name__ == "__main__":
    main()



