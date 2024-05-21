def get_periodic_table():
    periodic_table = {}
    with open('periodic_table.txt', 'r') as file:
        for line in file:
            element, properties_string = line.strip().split('=')
            element = element.strip()
            properties = {}
            for property_string in properties_string.split(','):
                property_name, value = property_string.split(':')
                property_name = property_name.strip()
                value = value.strip()
                try:
                    value = float(value) if '.' in value else int(value)
                except ValueError:
                    pass
                properties[property_name] = value
            periodic_table[element] = properties
    return periodic_table

def generate_css():
    # write css code to style.css
    css = 'table {\n'
    css += '    border-collapse: collapse;\n'
    css += '    width: 100%;\n'
    css += '}\n'
    css += 'th, td {\n'
    css += '    border: 1px solid black;\n'
    css += '    padding: 8px;\n'
    css += '    text-align: center;\n'
    css += '}\n'
    css += 'th {\n'
    css += '    background-color: #f2f2f2;\n'
    css += '}\n'

    with open('style.css', 'w') as file:
        file.write(css)

def generate_html(periodic_table):
    # write html code to periodic_table.html
    html = '<link rel="stylesheet" href="style.css">'
    html += '<table>\n'
    html += '<tr><th>Element</th><th>Position</th><th>Number</th><th>Small</th><th>Molar</th><th>Electron</th></tr>\n'
    for element, properties in periodic_table.items():
        html += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>\n'.format(
        element, properties['position'], properties['number'], properties['small'], properties['molar'], properties['electron'])
    html += '</table>'

    with open('periodic_table.html', 'w') as file:
        file.write(html)

# main
if __name__ == "__main__":
    periodic_table = get_periodic_table()
    generate_css()
    generate_html(periodic_table)
