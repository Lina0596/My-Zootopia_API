import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animals_data):
    """ Generates content from JSON file """
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


def content_html(html_file_path, data_str, new_html_file_path):
    """ Places content in html file and generates a new html file """
    with open(html_file_path, "r") as html_file:
        html_data = html_file.read()
        new_html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", data_str)
    with open(new_html_file_path, "w") as html_file:
        html_file.write(new_html_data)


if __name__ == "__main__":
    animals_data = load_data("animals_data.json")
    output = ''
    for animal in animals_data:
        output += serialize_animal(animals_data)
        content_html("animals_template.html", output, "animals.html")

