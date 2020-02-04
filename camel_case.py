# This program takesa sentence and converts it to camel case

def main():
    display_banner()

    while True:
        sentence = get_input()
        numbers = check_for_numbers(sentence)
        sentence = remove_special_chars(sentence)
        if numbers:
            print('Do not enter any numbers.')
        else:
            break
    
    sentence = camel_case(sentence)
    print('Your sentence in camel case is: %s' % sentence)

# Get the sentence from the user
def get_input():
    while True:
        sentence = input('Enter a sentence: ')
        if sentence != '':
            return sentence
        else:
            print('The sentence must not be left blank.')


# Check for any numbers in the sentence
def check_for_numbers(sentence):
    if any(char.isdigit() for char in sentence): # True if there is a number in the sentence
        return True
    else:
        return False


# Check for any special characters in the sentence
def remove_special_chars(sentence):
    invalid_chars = '@#$%^&*()_-+=[[}{;:"<>/`~|!?.,'
    for char in sentence:
        if char in invalid_chars:
            sentence = sentence.replace(char, '')
    return sentence


def display_banner():
    """ Display program name in banner """
    msg = 'AWSOME camelCaseGenerator PROGRAM'
    stars = '*' * len(msg)
    print(f'\n {stars} \n {msg} \n {stars}\n')
    print('Enter a sentence to convert to camelCase.')


def camel_case(sentence):
    words = sentence.split(' ')  # Split sentence into list
    new_words = [n.capitalize() for n in words]  # Capitalize the first letter of all items in list
    new_sentence = ''.join(new_words)  # Join all words together
    new_sentence = new_sentence[:1].lower() + new_sentence[1:]  # Make the first letter of the string lowercase
    return new_sentence


if __name__ == "__main__":
    main()