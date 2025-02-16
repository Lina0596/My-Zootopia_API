import data_fetcher


def serialize_animal(animals_data):
    """
    Generates content from Animals API
    """
    output = ''
    output += '<li class="cards__item">\n'
    if "name" in animal:
        name = animal["name"]
        output += f'<div class="card__title">{name}</div>\n'
    output += '<p class ="card__text">\n'
    if "diet" in animal["characteristics"]:
        diet = animal["characteristics"]["diet"]
        output += f"<strong>Diet:</strong> {diet}<br/>\n"
    if "locations" in animal:
        location = animal["locations"][0]
        output += f"<strong>Location:</strong> {location}<br/>\n"
    if "type" in animal["characteristics"]:
        type = animal["characteristics"]["type"]
        output += f"<strong>Type:</strong> {type}<br/>\n"
    output += '</p>\n'
    output += '</li>\n'
    return output


def create_error_message(animal_name):
    """
    Generates a error message for the animal name
    that doesn't exist in the API
    """
    output = ''
    output += f'<h2>The animal "{animal_name}" does not exist.</h2>'
    return output


def content_html(html_file_path, data_str, new_html_file_path):
    """
    Places content in html file and generates a new html file
    """
    with open(html_file_path, "r") as html_file:
        html_data = html_file.read()
        new_html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", data_str)
    with open(new_html_file_path, "w") as html_file:
        html_file.write(new_html_data)


if __name__ == "__main__":
    animal_name = input("Enter an animal: ")
    animals_data = data_fetcher.fetch_data(animal_name)
    if animals_data == []:
        output = create_error_message(animal_name)
        content_html("animals_template.html", output, "animals.html")
    else:
        output = ''
        for animal in animals_data:
            output += serialize_animal(animals_data)
            content_html("animals_template.html", output, "animals.html")
    print("Website was successfully generated to the file animals.html.")
