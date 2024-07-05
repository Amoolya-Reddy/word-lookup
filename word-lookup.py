import argparse
from collections import defaultdict


def calculate_matches(text_filepath, predefined_words):
    """
    Calculates and returns word counts from a text file based on a set of
    predefined words.
    Args:
        text_filepath(str): File path of the input text file to be analyzed.
        predefined_words(set): Set of predefined words
    Returns:
        dict: A dictionary of matched words with their count.
    """
    word_count = defaultdict(int)
   
    with open(text_filepath, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().lower().split()
            for word in words:
                if word in predefined_words:
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
    with open(args.predefined_words_filepath, 'r', encoding='utf-8') as file:
        predefined_words = {line.strip().lower() for line in file}

    match_count = calculate_matches(args.text_filepath, predefined_words)
    output_results(match_count, args.output_file)
