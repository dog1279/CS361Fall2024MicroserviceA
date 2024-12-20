# CS361Fall2024MicroserviceA

# Language Microservice

This microservice provides information about different languages, including the category they fall under based on the number of class hours required.

## Communication Contract

### Requesting Data

To request data from the microservice, you need to send a JSON request to the microservice server using ZeroMQ. The request should contain the language name.

#### Example Call

```python
import zmq

def send_request(language):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    print(f"Sending request for language: {language}")
    socket.send_json({"language": language})

    response = socket.recv_json()
    print(f"Received response: {response}")

# Example usage
languages_to_test = ["French", "German", "Japanese", "Unknown Language"]
for language in languages_to_test:
    send_request(language)
```

### Receiving Data

The data is received as a JSON response from the microservice server. The response will contain the language category or an error message if the language is not found.

### Microservice Implementation

The microservice server listens for incoming requests and responds with the language category.

#### Example Implementation

```python
import zmq

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
```

<img width="546" alt="image" src="https://github.com/user-attachments/assets/cdeca4ca-952e-42d9-ae0e-f2e1425bc8dc">
