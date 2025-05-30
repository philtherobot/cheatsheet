from bs4 import BeautifulSoup

def reorder_shortcut_description(html):
    soup = BeautifulSoup(html, 'html.parser')

    for pair in soup.select('.pair'):
        shortcut = pair.find('div', class_='shortcut')
        description = pair.find('div', class_='description')
        if shortcut and description:
            shortcut.extract()
            description.extract()
            pair.clear()
            pair.append(description)
            pair.append(shortcut)

    return str(soup)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python reorder_keys.py input.html output.html")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, 'r', encoding='utf-8') as f:
        original_html = f.read()

    modified_html = reorder_shortcut_description(original_html)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(modified_html)

    print(f"Processed HTML saved to {output_path}")
