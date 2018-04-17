#!/usr/bin/env python3
"""
Combine your markdown notes into a single html file

dependencies:
    - mistune
"""
import os
import sys
import mistune  # pip install mistune

if __name__ == "__main__":
    if sys.argv[1] == 'help':
        print('join markdown files into single html file')
        print('usage: python generate_site.py [directory]')
        exit()
    markdown_text = "\n"
    file_id = 0
    dir = os.listdir(sys.argv[1])
    if len(sys.argv) > 2:
        if sys.argv[2] == "reverse":
            dir.reverse()
    if os.path.isdir(sys.argv[1]):
        for f in dir:
            if os.path.isfile(os.path.join(sys.argv[1], f)) and f.endswith('.md'):
                try:
                    with open(os.path.join(sys.argv[1], f), 'r') as f:
                        markdown_text += "\nreplace_me{}\n".format(file_id)
                        markdown_text += f.read()
                        markdown_text += "\nclose_me\n"
                        markdown_text += '\n---\n'
                        file_id += 1
                except Exception as e:
                    print(e)
    markdown = mistune.Markdown()  # default settings
    html_formatted = markdown(markdown_text)
    for i in range(0, file_id):
        replace_me = "<p>replace_me{}</p>".format(i)
        replacement = "<div id=file_id{}>".format(i)
        html_formatted = html_formatted.replace(replace_me, replacement)
    html_formatted = html_formatted.replace("<p>close_me</p>", "</div>")
    html_formatted = "<div class=container style='font-family: verdana;'>" \
                     + html_formatted + "</div>"
    # build sidebar navigation
    side_bar = "<div class='two columns sidebar' style='font-family: verdana; float: left; height: 900px; position: fixed; border-right: 1px solid #E1E1E1;'><br>"
    side_bar += "<h2>Notes</h2><ul style='list-style-type: none;'>"
    for i in range(0, file_id):
        side_bar += "<a href=#file_id{0} style='text-decoration: none;'><li style='border-bottom: 1px solid #E1E1E1'>Note {0}</li></a>".format(i)
    side_bar += "</ul>"
    side_bar += "</div><br>"
    html_formatted = side_bar + html_formatted
    html_formatted = '<link href="https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.css" rel="stylesheet"></link> ' + html_formatted
    name = 'index.html'
    name = os.path.join(sys.argv[1], name)
    with open(name, 'w') as f:
        f.write(html_formatted)
    print(name)
