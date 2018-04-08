# Terminal Blogger

a project to write blogs in markdown from a command-line.

There are plenty of ways to blog and maybe there is a project just like this but I'm just making to learn some more skills.

Just write in a text editor or vim (using markdown) and save your file into the `posts` directory.

## Usage
Everytime a new file is added to the `posts` directory you will have to re-enter author, title, description... because I'm lazy and its not that much work to just do it.

When you are ready to regenerate your blog just run:
`python blog.py --generate`

## Styling
Edit the `style.css` file in the `css` directory with any styling you want. Skeleton CSS is included by default. Add your own styling on top of it.


### Skeleten CSS
By default going to include skeleton css files in a css directory and use that as the styling. I'm not planning to add more but it could be done if wanted.


## Dependencies
1. mistune (converting markdown to html)
2. tbd


## To Do
2. setup with github pages so when its committed it uploads there.
