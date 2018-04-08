"""
simple static sites from your terminal.

use markdown to make static site from command-line.

dependencies:
    - mistune
"""
import os
import argparse
import mistune
import time
import datetime


def create_new_html_file(title, author, description):
    """
    Genereate an html file with the users credentials.

    :param title: string -> name of the blog
    :param author: string -> name of the author
    :return: html file
    """
    filename = 'blog.html'
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
<link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
    <div class=container>
        <div>
            <h1>{0}</h1>
            <p>a blog about {2} by {1}</p>
            <hr>
        </div>
        <span id=find_me style="display=none;"></span>
    </div>
</body>
</html>""".format(title, author, description)
    with open(filename, 'w') as f:  # note this doesnt check if it exists
        f.write(html)
    return


def add_post(post, blog_file):
    """
    Add a new post to an existing blog.

    :param blog_file: the html file being added to
    :return:
    """
    post_datetime = str(post[1])
    post = post[0]
    markdown = mistune.Markdown()
    post = markdown(post)
    post = post + '<span>created: ' + post_datetime + '</span>' "<hr>"
    post = post + '<span id=find_me style="display=none;"></span>'
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


def add_posts_to_blog(posts):
    """
    Add each post from the list to the html file.

    :param posts: a list of lists of posts (markdown text) and created time
    :return:
    """
    posts.sort(key=lambda x: x[1], reverse=True)
    for post in posts:
        post[1] = datetime.datetime.strptime(post[1], "%a %b %d %H:%M:%S %Y")
        add_post(post, 'blog.html')


def generate():
    """
    Combine all your markdown files into your static html file.

    Ordered by file creation time from function add_posts_to_blog.

    :return:
    """
    posts = []
    directory = os.listdir(os.getcwd()+'/posts/')
    for filename in directory:
        a = os.stat(os.getcwd()+'/posts/'+filename)
        with open(os.getcwd()+'/posts/'+filename, 'r') as f:
            posts.append([f.read(), time.ctime(a.st_ctime)])
    add_posts_to_blog(posts)


def create_new_blog():
    """
    Get user info and generate an html file for the new blog.

    :return:
    """
    blog_title = input("Blog title: ")
    author_name = input("Author: ")
    description = input("Description: ")
    create_new_html_file(blog_title, author_name, description)
    print('Blog created: blog.html')
    print('add more markdown files to posts to expand your blog.')


def main():
    """Main."""
    parser = argparse.ArgumentParser(
        description='create and publish a blog from your command-line'
    )
    parser.add_argument('--generate',
                        help='generate your blog again with new posts',
                        action='store_true')
    parser.add_argument('--new_blog',
                        help='create a new blog',
                        action='store_true')
    args = parser.parse_args()
    if args.generate:
        create_new_blog()  # yes this will be repetitive but i dont want a db
        generate()


if __name__ == "__main__":
    main()
