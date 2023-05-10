"""
    CS5001
    Fall 2022
    HW6
    Leigh-Riane Amsterdam

    This a program that transforms words to emojis
"""


def load_data(source_file: str):
    """
    Function: load_data
        Opens and reads the original text file and puts it in a list
    :param source_file: (str) The name of the source text file
    :return: (list) List of lines in the text file
    """

    data = []
    with open(source_file, mode="r", encoding="utf8") as in_file:
        for each_data in in_file:
            data.append(each_data)
        return data


def load_directives(directives: str):
    """
    Function: load_directives
        Opens and reads the directives text file and puts it in a list
    :param directives: (str) The name of the directives text file
    :return: (list) List of lines in the text file
    """

    directive = []
    with open(directives, mode="r", encoding="utf8") as in_file:
        for each_directive in in_file:
            directive.append(each_directive)
        return directive


def load_emoji(emoji_file: str):
    """
    Function: load_emoji
        Opens and reads the directives text file and puts it in a list
    :param emoji_file: (str) The name of the emoji text file
    :return: (list) List of lines in the text file
    """

    emoji = []
    with open(emoji_file, mode="r", encoding="utf8") as in_file:
        for each_emoji in in_file:
            emoji.append(each_emoji.split())
        return emoji


def create_dictionary(input_lang: str, output_lang: str, emoji_file: str):
    """
    Function: create_dictionary
        Makes dictionary and input language is key and output language is value
    :param input_lang: (str) The original language in the text file
    :param output_lang: (str) The target language for translation
    :param emoji_file: (str) The name of the emoji text file
    :return: (dict) A dictionary where input is key and output is value
    """

    dictionary = {}
    emoji = load_emoji(emoji_file)
    # Get index position for input/output language from metadata
    # Map index position minus one to the other lists in emoji file
    input_index = 0
    output_index = 0
    for i in range(len(emoji[0])):
        if input_lang.upper() == emoji[0][i].upper():
            input_index = i - 1
        if output_lang.upper() == emoji[0][i].upper():
            output_index = i - 1

    # Check if input/output language is english and switch to lowercase
    for i in range(1, len(emoji)):
        if input_lang.upper() == "ENGLISH":
            key = emoji[i][input_index].lower()
        else:
            key = emoji[i][input_index]

        if output_lang.upper() == "ENGLISH":
            value = emoji[i][output_index].lower()
        else:
            value = emoji[i][output_index]
        dictionary[key] = value
    return dictionary


def translate_text(source_file, destination, dictionary):
    """
    Function: translate_text
        Replaces words in text file with emojis and writes to new file
    :param source_file: (str) The name of the source text file
    :param destination: (str) The name of the new text file to be written
    :param dictionary: (dict) Dictionary where input is key and output is value
    :return:
    """

    translated_list = []

    # split source file into each word is element in list
    input_file = load_data(source_file)
    for i in range(len(input_file)):
        string_test = " "
        input_words = input_file[i].split()

        # check if word in dictionary and replaces it with value at the key
        for j in range(len(input_words)):
            if input_words[j] in dictionary:
                input_words[j] = dictionary[input_words[j]]
            string_test += " " + input_words[j]

        translated_list.append(string_test)

    with open(destination, mode="w", encoding="utf8") as out_file:
        for each_line in translated_list:
            out_file.write(each_line + "\n")


def batch_translate(emoji_file_name: str, directives_file_name: str):
    """
    Function: batch_translate
        For each line in directives, makes dictionary and translates text file
    :param emoji_file_name: (str) The name of the emoji text file
    :param directives_file_name: (str) Text file instructions for source file
    :return:
    """

    try:
        emoji_file = emoji_file_name
        directives = load_directives(directives_file_name)

        # splits line into words as elements and sets indices for parameters
        for i in range(len(directives)):
            directive_words = directives[i].split()
            input_lang = directive_words[0]
            output_lang = directive_words[1]
            source_file = directive_words[2]
            destination = directive_words[3]
            dictionary = create_dictionary(input_lang, output_lang, emoji_file)
            translate_text(source_file, destination, dictionary)
    except IOError:
        print("Error has occurred")


def main():
    batch_translate("emojis.txt", "emoji_directives.txt")
    print("Done!")


if __name__ == "__main__":
    main()
