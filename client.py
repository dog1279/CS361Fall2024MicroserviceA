import zmq

def send_request(language):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    print(f"Sending request for language: {language}")
    socket.send_json({"language": language})

    response = socket.recv_json()
    print(f"Received response: {response}")

if __name__ == "__main__":
    languages_to_test = ["French", "German", "Japanese", "Unknown Language"]
    for language in languages_to_test:
        send_request(language)