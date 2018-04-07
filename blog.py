"""
blog from your terminal.

use markdown to publish blog from command-line.

dependencies:
    - mistune
"""
import argparse
import mistune


def add_skeleton_css(html_file):
    """
    Add a link to skeleton css make html look good.

    :param html_file: full path to an html file
    :return: the html file
    """
    pass


def convert_to_html(filename):
    """
    Convert a markdown file to html using mistune libary.

    :param filename: The full path to a file including filename
    :return: a converted html file
    """
    markdown = mistune.Markdown()  # default settings.
    md_file = open(filename, 'r')  # pass in full path file
    html = markdown(md_file.read())
    save_html_file(html)
    return html


def save_html_file(html_file, directory=None):
    """
    Save the new html file.

    :param html_file: full path to an html file
    :param directory: a specific directory otherwise use same as md_file
    :return: path to file
    """
    with open('converted.html', 'w') as f:
        f.write(html_file)


def create_new_html_file(title, author, description):
    """
    Genereate an html file with the users credentials.

    :param title: string -> name of the blog
    :param author: string -> name of the author
    :return: html file
    """
    title = title.replace(' ', '_')
    filename = title + '.html'
    html = """<!DOCTYPE html>
<html>
<head>
<title>{0}</title>
<meta charset='utf-8' />
<meta name='viewport' content='width=device-width, initial-scale=1' />
<meta name='author' content='{1}' />
<meta name='description' content='{2}' />
<link rel="stylesheet" type="text/css" href="css/normalize.css">
<link rel="stylesheet" type="text/css" href="css/skeleton.css">
<style>
body {{font-family: verdana, arial, helvetica;}}
</style>
</head>
<body>
    <div class=container>
        <span id=find_me style="display=none;"></span>
    </div>
</body>
</html>""".format(title, author, description)
    with open(filename, 'w') as f:  # note this doesnt check if it exists
        f.write(html)
    return


def create_new_blog():
    """
    Get user info and generate an html file for the new blog.

    :return:
    """
    blog_title = input("Blog title: ")
    author_name = input("Author: ")
    description = input("Description: ")
    create_new_html_file(blog_title, author_name, description)


def get_post_input():
    """
    Prompt user for their blog post input.

    To exit must type exit()
    :return: the combined lines from user input
    """
    print('Type exit() to finish your post.')
    lines = []
    while True:
        line = input()
        if line == 'exit()':
            break
        else:
            lines.append(line)
    lines.append('<span id=find_me style="display=none;"></span>')
    text = '\n'.join(lines)
    return text


def add_post(blog_file):
    """
    Add a new post to an existing blog.

    :param blog_file: the html file being added to
    :return:
    """
    markdown = mistune.Markdown()
    post = get_post_input()
    post = markdown(post)
    with open(blog_file, 'r') as f:
        blog_text = f.read()

    new_blog = []
    for line in blog_text.split('\n'):
        if '<span id=find_me style="display=none;"></span>' in line:
            line = line.replace(
                        '<span id=find_me style="display=none;"></span>',
                        post)
        new_blog.append(line)

    blog = '\n'.join(new_blog)
    with open(blog_file, 'w') as f:
        f.write(blog)
    return


def main():
    """Main."""
    parser = argparse.ArgumentParser(
        description='create and publish a blog from your command-line'
    )
    parser.add_argument('--new_blog',
                        help='create a new blog',
                        action='store_true')
    args = parser.parse_args()
    if args.new_blog:
        create_new_blog()
    add_post('testing.html')


if __name__ == "__main__":
    main()
