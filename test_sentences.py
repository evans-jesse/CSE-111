from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest

pytest.console_main()


def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["the", "one"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many"]
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners



def test_get_noun():
    
    # Test the singular determiners.
    singular_determiners = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_noun(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    for _ in range(4):
        word = get_noun(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners
    


def test_get_verb():

    
    # Test the singular determiners.
    past_determiners = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_verb(1, 1)
        assert word in past_determiners

    present_single_determiners = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        word = get_verb(1, 2)
        assert word in present_single_determiners

    present_plural_determiners = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        word = get_verb(2, 2)
        assert word in present_plural_determiners

    # Test the plural determiners.
    future_determiners = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(4):
        word = get_verb(2, 3)
        assert word in future_determiners
    
def test_preposition():
    preposition = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    for _ in range(4):
        word = get_preposition()
        assert word in preposition

"""
def test_prepositional_phrase():
    single_prepositional_phrase = (f"{get_preposition()} {get_determiner(1)} {get_noun(1)}")
    for _ in range(4):
        word = get_prepositional_phrase(1)
        assert word in single_prepositional_phrase

    plural_prepositional_phrase = (f"{get_preposition()} {get_determiner(0)} {get_noun(0)}")
    for _ in range(4):
        word = get_prepositional_phrase(0)
        assert word in plural_prepositional_phrase
"""