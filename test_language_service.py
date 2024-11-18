import subprocess

def test_language_service(language):
    result = subprocess.run(['python', 'language_service.py', language], capture_output=True, text=True)
    return result.stdout.strip()

if __name__ == '__main__':
    while True:
        language = input("Please enter a language (or type 'exit' to quit): ")
        if language.lower() == 'exit':
            break
        response = test_language_service(language)
        print(f"Response from microservice: {response}")