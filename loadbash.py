from keras.preprocessing.text import Tokenizer

def load_bash_history(file_path):
    # Read the bash history file
    with open(file_path, 'r') as file:
        bash_history = file.read()

    # Split the history into individual commands
    commands = bash_history.split('\n')
    print(commands)

    # Create a tokenizer to process the commands
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(commands)

    # Convert the commands to sequences of integers
    sequences = tokenizer.texts_to_sequences(commands)

    return sequences


load_bash_history('history.txt')



