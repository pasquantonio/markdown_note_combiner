# Markdown converter and joiner

Convert markdown files to html and join them together 

## Usage
`python generate_site.py [directory]`

or if you want the files in reverse order:
`python generate_site.py [directory] reverse`

## Skeleton CSS

a cdn css link is added to the file which adds skeleton css styling. plus things I added myself which I like.


## Dependencies
1. mistune (converting markdown to html)
2. tbd


## To Do
1. sort .md files by creation date (and reverse) - entries should be in order
2. Extract titles of each note (first in file with ## will be the title) for sidebar navigation
