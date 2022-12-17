# Imports the random module.
import random

# Defines the main function.
def main():

    # Creates lists.
    pre_quantity = [0 , 1]
    pre_tense = ["past", "present", "future"]

    # Randomizes and chooses an element from each
    # list above and stores them into variables.
    quantity = random.choice(pre_quantity)
    tense = random.choice(pre_tense)

    # Calls the functions and their parameters then
    # stores them into a variables.
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    first_prepositional_phrase = get_prepositional_phrase(quantity)
    second_prepositional_phrase = get_prepositional_phrase(quantity)

    # Prints a string making a sentence with the
    # variables above.
    print(f"{determiner.capitalize()} {noun} {first_prepositional_phrase} {verb} {second_prepositional_phrase}.")

# Creates a function with parameter to get the
# determiner.
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    # Based on quanitity of items, if it's singular
    # or not, it chooses a word.
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)

    return word

# Creates a function with parameter to get the
# noun.
def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    # Based on quanitity of items, if it's singular
    # or not, it chooses a word.
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
            "dog", "girl", "man", "rabbit", "woman"]
    else:
        words =["birds", "boys", "cars", "cats", "children",
            "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    word = random.choice(words)

    return word

# Creates a function with two parameters to get the
# verb.
def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    # Based on quanitity of items, if it's singular
    # or not; and based on tense, it chooses a word.
    if tense.lower() == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"]
    elif quantity == 1 and tense.lower() == "present":
        words = ["drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"]
    elif quantity != 1 and tense.lower() == "present":
        words = ["drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"]
    else:
        words = ["will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"]

    # Randomly choose and return a determiner.
    word = random.choice(words)

    return word

# Creates a function with no parameters to get a
# preposition.
def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """

    # Based on quanitity of items, if it's singular
    # or not, it chooses a word.
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    # Randomly choose and return a determiner.
    word = random.choice(words)

    return word

# Creates a function with no parameters to get a
# preposition.
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """

    # Uses a function and stores the result
    # in their specific variables.
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    # Creates the phrase and stores it
    # into a variable to be used later.
    preposition_phrase = str(f"{preposition} {determiner} {noun}")

    return preposition_phrase

# Calls the main function to
# start the program
if __name__ == "__main__":
    main()