from language_data import language_info
import sys

def get_language_info(language):
    formatted_language = language.lower().title()
    if formatted_language in language_info:
        category = language_info[formatted_language]["category"]
        return f"The language '{formatted_language}' falls under Category {category}."
    else:
        return "Language not found."

if __name__ == '__main__':
    if len(sys.argv) > 1:
        language = sys.argv[1]
        print(get_language_info(language))
    else:
        print("Please provide a language as a command-line argument.")