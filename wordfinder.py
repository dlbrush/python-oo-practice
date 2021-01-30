"""Word Finder: finds random words from a dictionary."""

from random import randrange

class WordFinder:
    """
    Is initialized with a path to a document that contains one word on each line.
    Creates a list of those words.
    When initialized, it returns a string telling you how many words were included.
    Can return a random word from that list.

    Attributes:

    path: a filepath to the list of words that should be read into the list
    word_list: the list of words generated after the file has been read.

    >>> finder = WordFinder('words.txt')
    235886 words read

    >>> len(finder.word_list)
    235886

    >>> finder.random() in finder.word_list
    True

    >>> finder.random() in finder.word_list
    True

    >>> finder.random() in finder.word_list
    True
    
    """
    def __init__(self, path):
        "Creates the Wordfinder object from a path to the word list file and prints the number of words included."
        self.path = path
        self.read_list()
        self.print_words_read()
        
    def read_list(self):
        "Reads words from the linked file and stores each word to the word_list attribute for this WordFinder. Called in the initialization of this class."
        word_file = open(self.path, "r")
        self.word_list = [line.strip() for line in word_file]
        word_file.close()

    def print_words_read(self):
        "Prints a string that says how many words were read when the class was initialized."
        print(f"{len(self.word_list)} words read")

    def random(self):
        "Return a random word from the list of words"
        random_index = randrange(len(self.word_list))
        return self.word_list[random_index]

class SpecialWordFinder(WordFinder):
    """
    Is initialized with a path to a document that contains one word on each line.
    Creates a list of those words, excluding blank lines and 
    When initialized, it returns a string telling you how many words were read.
    Can return a random word from that list.

    >>> specfinder = SpecialWordFinder('specwords.txt')
    4 words read

    >>> len(specfinder.word_list)
    4

    >>> specfinder.random() in specfinder.word_list
    True

    >>> specfinder.random() in specfinder.word_list
    True

    >>> specfinder.random() in specfinder.word_list
    True
    """

    def __init__(self, path):
        super().__init__(path)
        self.word_list = self.filter_words()

    def filter_words(self):
        "Returns a list of words that does not include blank or comment lines"
        return [word for word in self.word_list if self.check_word(word)]

    def check_word(self, word):
        "If the passed word is an empty string or a commented line starting with #, returns false"
        if word != '' and not word.startswith('#'):
                return True
    
        return False

    def print_words_read(self):
        "Prints a string that says how many words were read when the class was initialized (after filtering blanks and comments)."    
        print(f"{len(self.filter_words())} words read")