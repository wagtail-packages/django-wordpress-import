import subprocess
from pathlib import Path

import click

wordpress_url = "192.168.1.197"

commands = {
    "authors": [f"http://{wordpress_url}:8888/wp-json/wp/v2/users", "WPAuthor"],
    "categories": [f"http://{wordpress_url}:8888/wp-json/wp/v2/categories", "WPCategory"],
    "tags": [f"http://{wordpress_url}:8888/wp-json/wp/v2/tags", "WPTag"],
    "pages": [f"http://{wordpress_url}:8888/wp-json/wp/v2/pages", "WPPage"],
    "posts": [f"http://{wordpress_url}:8888/wp-json/wp/v2/posts", "WPPost"],
    "media": [f"http://{wordpress_url}:8888/wp-json/wp/v2/media", "WPMedia"],
    "comments": [f"http://{wordpress_url}:8888/wp-json/wp/v2/comments", "WPComment"],
}


@click.group()
def dj():
    """CLI for django"""



@dj.command()
def complete():
    """Import all from wordpress"""
    subprocess.run(["poetry", "run", "python", "manage.py", "import", commands["authors"][0], commands["authors"][1]])
    subprocess.run(
        ["poetry", "run", "python", "manage.py", "import", commands["categories"][0], commands["categories"][1]]
    )
    subprocess.run(["poetry", "run", "python", "manage.py", "import", commands["tags"][0], commands["tags"][1]])
    subprocess.run(["poetry", "run", "python", "manage.py", "import", commands["pages"][0], commands["pages"][1]])
    subprocess.run(["poetry", "run", "python", "manage.py", "import", commands["posts"][0], commands["posts"][1]])
    subprocess.run(["poetry", "run", "python", "manage.py", "import", commands["media"][0], commands["media"][1]])
    subprocess.run(["poetry", "run", "python", "manage.py", "import", commands["comments"][0], commands["comments"][1]])


@dj.command()
def authors():
    """Import authors from wordpress"""
    subprocess.run(["poetry", "run", "python", "manage.py", "import", commands["authors"][0], commands["authors"][1]])


@dj.command()
def categories():
    """Import categories from wordpress"""
    subprocess.run(
        ["poetry", "run", "python", "manage.py", "import", commands["categories"][0], commands["categories"][1]]
    )


@dj.command()
def tags():
    """Import tags from wordpress"""
    subprocess.run(["poetry", "run", "python", "manage.py", "import", commands["tags"][0], commands["tags"][1]])


@dj.command()
def pages():
    """Import pages from wordpress"""
    subprocess.run(["poetry", "run", "python", "manage.py", "import", commands["pages"][0], commands["pages"][1]])


@dj.command()
def posts():
    """Import posts from wordpress"""
    subprocess.run(["poetry", "run", "python", "manage.py", "import", commands["posts"][0], commands["posts"][1]])


@dj.command()
def media():
    """Import media from wordpress"""
    subprocess.run(["poetry", "run", "python", "manage.py", "import", commands["media"][0], commands["media"][1]])


@dj.command()
def comments():
    """Import comments from wordpress"""
    subprocess.run(["poetry", "run", "python", "manage.py", "import", commands["comments"][0], commands["comments"][1]])


@dj.command()
def runserver():
    """Run the django server"""
    subprocess.run(["poetry", "run", "python", "manage.py", "runserver"])


@dj.command()
def destroy():
    """Destroy the database"""
    # delete the database
    db = Path("./django_wordpress_import/db.sqlite3")
    if db.exists():
        db.unlink()
