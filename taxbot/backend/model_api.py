from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage
import prompts

main_model = "bielik:collect"
# main_model = "codellama:latest"

llm = Ollama(model=main_model, request_timeout=600)
next_prompt = "intro"
# next_prompt = "yes"  #unlock to skip 1 steps
generated_xml = ""

name = "Jan Jak"

def send_prompt(user_question):
    global next_prompt
    global llm
    global name
    print(f"next prompt: {next_prompt}")
    if next_prompt == "intro":
        response = run_ollama(question=user_question, system_prompt=prompts.intro)
        response += "\n \n <b>Czy chcesz wypełnić formularz PCC-3. Wpisz tak lub nie</b>"
        next_prompt = "yesno"
        return response

    if next_prompt == "yesno":
        llm = Ollama(model=main_model, request_timeout=600)
        response = run_ollama(question=user_question, system_prompt=prompts.yesno)
        print( response)
        response = remove_special_characters(response.lower().replace("assistant:", "").strip())
        print( response)
        if response.lower().strip() == "tak":
            response = "Podaj imię i nazwisko osoby do wypełnienia formularza PCC-3."
            next_prompt = "yes"
        elif response.lower() == ("nie"):
            next_prompt = "no"
        return response

    if next_prompt == "no":
        response = "Dziękujemy za skorzystanie z taxbota."
        # next_prompt = "exit"
        return response

    if next_prompt == "yes":
        llm = Ollama(model=main_model, request_timeout=600)
        name = user_question
        #question with data
        response = run_ollama(question=user_question, system_prompt=prompts.data_validation)
        print(f"fa{response.lower()}")
        if "dane są poprawne" in response.lower()\
                or "assistant: Dane są poprawne" in response:
            next_prompt = "name_validateion"
        return response

    if next_prompt == "name_validateion":
        # Validate name
        llm.request_timeout =600
        print(f"name: {name}")
        response = run_ollama(question=f"generuj plik xml, uwzględniając podane dane. Imie i nazwisko Podmiot1: {name}", system_prompt=prompts.data_xml_generation)
        # response = validate_name(response)
        global generated_xml
        generated_xml = response.replace("```", "")
        response = '<a href="/taxform.xml">link text</a>'
        next_prompt = "no"
        return response


def run_ollama(question, system_prompt):
    messages = [
        ChatMessage(
            role="system",
            content=system_prompt
        ),
        ChatMessage(role="user", content=question),
    ]
    response = llm.chat(messages)
    return response.__str__()


import re


def remove_special_characters(input_string):
    """
    Remove all special characters from the input string.

    Args:
        input_string (str): The input string containing special characters.

    Returns:
        str: A string with all special characters removed.
    """
    # Define a regular expression pattern to match any character that is not alphanumeric, whitespace, or punctuation
    pattern = r'[^a-zA-Z0-9\s.,!?]'

    # Use re.sub() to replace the matched characters with an empty string
    cleaned_string = re.sub(pattern, '', input_string)

    return cleaned_string



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Example usage:
    input_str = "Hello! This is a test string with special characters: @#$%^&*()_+{}|:\" <>?~` -= [];',./."
    cleaned_str = remove_special_characters(input_str)
    print("Original String:", input_str)
    print("Cleaned String:", cleaned_str)

    # main_model = "codellama:latest"
    # run_ollama(main_model, "hi there")
