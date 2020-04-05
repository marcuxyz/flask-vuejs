import os
import platform
import subprocess
from distutils.dir_util import copy_tree

import click
from flask.cli import with_appcontext

BASEDIR = os.path.dirname(os.path.dirname(__file__))


@click.group()
def vue():
    """ Perform your application with Vue.JS. """
    pass


@vue.command()
@click.option("--init", default=False)
@with_appcontext
def init(init):
    """ Configure your project. """
    front_original = os.path.join(BASEDIR, "flask_vuejs")
    frontend_dir = "frontend"

    if (
        os.path.isdir(frontend_dir)
        or os.path.isfile("package.json")
        or os.path.isfile("webpack.config.js")
    ):
        return click.echo("You already configured your application.")

    # copy directories locals to application directory
    copy_tree(os.path.join(front_original, "init"), ".")
    copy_tree(os.path.join(front_original, frontend_dir), frontend_dir)

    return click.echo(
        "Setup configured successfully! Run the command to compile the vue\n\nflask vue compile\n"
    )


@vue.command()
@with_appcontext
def install():
    """ Install the vue packages """
    subprocess.check_call("npm i --silent", shell=True)


@vue.command()
@with_appcontext
def compile():
    """ Compile assets only once """
    subprocess.check_call("npm run build", shell=True)
    return click.echo("\nCompiled!\n")


@vue.command()
@with_appcontext
def watch():
    """ Watch the vue files """
    text = "Before execute this command, you should be set FLASK_ENV as development mode. \n\n$ {} FLASK_ENV=development\n"

    if os.getenv("FLASK_ENV") == "development":
        subprocess.check_call("npm run watch", shell=True)

    if platform.system() == "Windows":
        return click.echo(text.format("set"))
    return click.echo(text.format("export"))


def init_app(app):
    app.cli.add_command(vue)
