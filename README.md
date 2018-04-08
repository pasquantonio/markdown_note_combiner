# Python static website generator 

a project to write blogs or create static websites in markdown.

There are plenty of other ways to do this (hugo/jekyll) and maybe there is a project just like this but I'm just making to learn some more skills. Other projects will be much more robust but this works for what I wanted to do and is a very small amount of code.

Just write in a text editor/vim (using markdown if you want html) and save your file into the `posts` directory.

## Usage
Create a `posts` directory in the same directory as blog.py if `posts` does not yet exist.

When you are ready to regenerate your blog just run:
`python blog.py --generate`

Everytime a new file is added to the `posts` directory you will have to re-enter author, title, description... because its not that much work to just do it and I didn't want to add a database or another solution.

## Styling
Edit the `style.css` file in the `css` directory with any styling you want. Skeleton CSS is included by default. Add your own styling on top of it.


### Skeleten CSS
By default going to include skeleton css files in a css directory and use that as the styling. I'm not planning to add more but it could be done if wanted.


## Dependencies
1. mistune (converting markdown to html)
2. tbd


## To Do
2. instructions to setup with github pages so when its committed it uploads there.
