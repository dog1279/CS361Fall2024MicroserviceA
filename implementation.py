def language_category(language):
    language_info = {
        "Danish": "Category I",
        "Dutch": "Category I",
        "French": "Category I",
        "Italian": "Category I",
        "Norwegian": "Category I",
        "Portuguese": "Category I",
        "Romanian": "Category I",
        "Spanish": "Category I",
        "Swedish": "Category I",
        "German": "Category II",
        "Indonesian": "Category II",
        "Malaysian": "Category II",
        "Swahili": "Category II",
        "Albanian": "Category III",
        "Amharic": "Category III",
        "Armenian": "Category III",
        "Azerbaijani": "Category III",
        "Bengali": "Category III",
        "Bosnian": "Category III",
        "Bulgarian": "Category III",
        "Burmese": "Category III",
        "Croatian": "Category III",
        "Czech": "Category III",
        "Estonian": "Category III",
        "Finnish": "Category III",
        "Georgian": "Category III",
        "Greek": "Category III",
        "Hebrew": "Category III",
        "Hindi": "Category III",
        "Hungarian": "Category III",
        "Icelandic": "Category III",
        "Kazakh": "Category III",
        "Khmer": "Category III",
        "Kurdish": "Category III",
        "Kyrgyz": "Category III",
        "Lao": "Category III",
        "Latvian": "Category III",
        "Lithuanian": "Category III",
        "Macedonian": "Category III",
        "Mongolian": "Category III",
        "Nepali": "Category III",
        "Pashto": "Category III",
        "Persian (Dari, Farsi, Tajik)": "Category III",
        "Polish": "Category III",
        "Russian": "Category III",
        "Serbian": "Category III",
        "Sinhala": "Category III",
        "Slovak": "Category III",
        "Slovenian": "Category III",
        "Tagalog": "Category III",
        "Thai": "Category III",
        "Turkish": "Category III",
        "Ukrainian": "Category III",
        "Urdu": "Category III",
        "Uzbek": "Category III",
        "Vietnamese": "Category III",
        "Xhosa": "Category III",
        "Zulu": "Category III",
        "Arabic": "Category IV",
        "Chinese - Cantonese": "Category IV",
        "Chinese - Mandarin": "Category IV",
        "Japanese": "Category IV",
        "Korean": "Category IV"
    }
    
    formatted_language = language.lower().title()
    return language_info.get(formatted_language, "Language not found.")

import zmq

def microservice_A():
    print("Connecting server.")
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    print("Server connected successfully.")

    while True:
        print("Waiting for request from client...")
        request = socket.recv_json()
        print("Request received. Returning language category now.")
        response = language_category(request["language"])
        print("Sending response back to client.")
        socket.send_json({"category": response})

if __name__ == "__main__":
    microservice_A()