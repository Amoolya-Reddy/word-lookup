import argparse
from collections import defaultdict


class TrieNode:
    """
    Class defining a node of the Trie.
    """
    def __init__(self):
        self.children = {}
        self.is_word_end = False


class Trie:
    """
    Class encapsulating the Trie operations.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the Trie.

        Args:
            word(str): Word to be inserted into the Trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word_end = True

    def search(self, word):
        """
        Searches for a word in the Trie and returns True if the word exists in
        the Trie.
        Args:
            word(str): Word that needs to be searched in the Trie.
        Returns:
            boolean: Returns True if the word exists, else False.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word_end


def build_trie_from_file(filepath):
    """
    Builds a Trie from the words given in the specified file path.
    Args:
        filepath(str): File path of predefined words to build a Trie.
    """
    trie = Trie()
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            trie.insert(line.strip().lower())
    return trie


def calculate_matches_with_trie(text_filepath, word_trie):
    """
    Calculates and returns word counts from a text file based on a trie of
    predefined words.
    Args:
        text_filepath(str): File path of the input text file to be analyzed.
        word_trie(Trie): Trie built out of predefined words
    Returns:
        dict: A dictionary of matched words with their count.
    """
    word_count = defaultdict(int)
    
    with open(text_filepath, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().lower().split()
            for word in words:
                if word_trie.search(word):
                    word_count[word] += 1

    return word_count


def output_results(match_count, output_file=None):
    """
    Formats and outputs the results to either stdout or specified output file.
    Args:
        match_count(dict): A dictionary with the words and their corresponding
        counts.
        output_file(str): File path to which output needs to be written.
    """
    results = f"{'Predefined word':<50}{'Match count'}\n"
    for word, count in sorted(match_count.items(),
                              key=lambda item: item[1],
                              reverse=True):
        results += f"{word:<50}{count}\n"
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(results)
    else:
        print(results)


def process_args():
    """
    Parses and processes command line arguments.
    Returns:
        List of args with the filepaths of predefined words, text file and
        output file, if specified.
    """
    parser = argparse.ArgumentParser(
        description="Count matches of predefined words in a text file."
    )
    parser.add_argument(
        "predefined_words_filepath",
        type=str,
        help="File path to the predefined words."
    )
    parser.add_argument(
        "text_filepath",
        type=str,
        help="File path to the text file for analysis."
    )
    parser.add_argument(
        "-o", "--output",
        dest="output_file",
        type=str,
        help="Optional output file to write the results."
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = process_args()

    word_trie = build_trie_from_file(args.predefined_words_filepath)

    match_count = calculate_matches_with_trie(args.text_filepath, word_trie)
    output_results(match_count, args.output_file)
