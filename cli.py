import subprocess
from pathlib import Path

import click
from django import db


@click.group()
def wp():
    """CLI for wordpress"""


@wp.command()
def build():
    """Wordpress initial setup"""

    # copy the .env.example file to .env if not exists
    env_file = Path("./wordpress.docker/.env")
    if not env_file.exists():
        with open("./wordpress.docker/.env.example") as f:
            env_content = f.read()
            with open("./wordpress.docker/.env", "w") as f2:
                f2.write(env_content)

    # create directory for plugins
    plugins_dir = Path("./wordpress.docker/wp-content/plugins")
    if not plugins_dir.exists():
        plugins_dir.mkdir(parents=True)

    # clone the plugins into the plugins directory
    plugins = ["https://github.com/valu-digital/wp-graphql-offset-pagination.git"]

    for plugin in plugins:
        if not Path(plugins_dir / Path(plugin).stem).exists():
            subprocess.run(["git", "clone", plugin], cwd=plugins_dir)
        else:
            print(f"Plugin {plugin} already exists")


@wp.command()
def up():
    """Wordpress start the container"""
    subprocess.run(["docker-compose", "up", "-d"], cwd="./wordpress.docker")


@wp.command()
def down():
    """Wordpress stop the container"""
    subprocess.run(["docker-compose", "down"], cwd="./wordpress.docker")


@wp.command()
def destroy():
    """Wordpress destroy the container"""
    subprocess.run(["docker-compose", "down", "--volumes"], cwd="./wordpress.docker")

    cleanup = click.prompt("Do you want to clean up the files? (y/n)", type=str)

    if cleanup == "y":
        env_file = Path("./wordpress.docker/.env")
        if env_file.exists():
            env_file.unlink()

        wp_content = Path("./wordpress.docker/wp-content")
        if wp_content.exists():
            subprocess.run(["rm", "-rf", "./wordpress.docker/wp-content"])

        wp_xml = Path("./wordpress.docker/xml")
        if wp_xml.exists():
            subprocess.run(["rm", "-rf", "./wordpress.docker/xml"])


@wp.command()
def load():
    """Wordpress import the demo data"""
    # if docker-compose is not running, start it
    running = subprocess.run(["docker-compose", "ps"], cwd="./wordpress.docker", capture_output=True).stdout.decode(
        "utf-8"
    )
    if "wordpress" not in running:
        click.echo("Please start the container first: 'poetry run cli up'")
        return

    # import the demo data
    subprocess.run(
        ["docker-compose", "exec", "-T", "wordpress", "bin/init.sh"],
        cwd="./wordpress.docker",
    )


@click.group()
def dj():
    """CLI for django"""


commands = {
    "authors": ["http://localhost:8888/wp-json/wp/v2/users", "WPAuthor"],
    "categories": ["http://localhost:8888/wp-json/wp/v2/categories", "WPCategory"],
    "tags": ["http://localhost:8888/wp-json/wp/v2/tags", "WPTag"],
    "pages": ["http://localhost:8888/wp-json/wp/v2/pages", "WPPage"],
    "posts": ["http://localhost:8888/wp-json/wp/v2/posts", "WPPost"],
    "media": ["http://localhost:8888/wp-json/wp/v2/media", "WPMedia"],
    "comments": ["http://localhost:8888/wp-json/wp/v2/comments", "WPComment"],
}


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
