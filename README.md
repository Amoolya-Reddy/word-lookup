# Word Lookup

This python project is used to perform a lookup of text in a predefined set of words. 

There are two approaches presented in the project - one using a hash map(word-lookup.py) and one with a trie(word-lookup-trie.py). For the specified task of matching entire words from a list of predefined words against a 20 MB text file, the hash map approach is recommended. Trie can be memory-intensive and would be more suitable when there are prefixes and no exact matches. Trie would be an overkill in this scenario but a good option in the exploration of performing a lookup.

Clean code and software design principles are applied with pep8 formatting of the scripts.

## Usage

Run the program from the command line, specifying the path to the predefined words file and the text file to be analyzed. Optionally, specify an output file to write the results.

```bash
python word-lookup.py <predefined_words_filepath> <text_filepath> [-o <output_filepath>]
```

## Testing Done

* Tested the script against a few defined input and output scenarios.
* Tested all the failure points of the script and handled the errors properly.
* Unit tested the script.