# CS361Fall2024MicroserviceA

# Language Microservice

This microservice provides information about different languages, including the category they fall under based on the number of class hours required.

## Communication Contract

### Requesting Data

To request data from the microservice, you need to call the `language_service.py` script with the language name as a command-line argument. This can be done programmatically using the `subprocess` module in Python.

#### Example Call

```
python
import subprocess

def request_language_info(language):
    result = subprocess.run(['python', 'language_service.py', language], capture_output=True, text=True)
    return result.stdout.strip()

# Example usage
language = "Japanese"
response = request_language_info(language)
print(f"Response from microservice: {response}")
```

### Receiving Data

The data is received as the standard output from the language_service.py script. The output will be a string containing the language information or an error message if the language is not found.

#### Example Call
```
import subprocess

def receive_language_info(language):
    result = subprocess.run(['python', 'language_service.py', language], capture_output=True, text=True)
    return result.stdout.strip()

# Example usage
language = "Japanese"
response = receive_language_info(language)
print(f"Response from microservice: {response}")
```

### Instructions
#### Requesting Data:

Use the subprocess.run method to call language_service.py with the language name as an argument.
Capture the output using capture_output=True and text=True.
#### Receiving Data:

The output from the subprocess call will contain the language information or an error message.
Use result.stdout.strip() to get the response as a string.

<img width="546" alt="image" src="https://github.com/user-attachments/assets/cdeca4ca-952e-42d9-ae0e-f2e1425bc8dc">

