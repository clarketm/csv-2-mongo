#!/usr/bin/env python3

from json import loads
from os.path import basename
from re import match
from sys import exit

import warnings
import click
from pandas import read_csv
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

__VERSION__ = "0.0.1"

warnings.filterwarnings("ignore", category=DeprecationWarning)


@click.command()
@click.help_option("-h", "--help")
@click.version_option(__VERSION__, "-v", "--version", message="Version %(version)s")
@click.option(
    "-d",
    "--database",
    metavar="name",
    default="test",
    help="Database name.",
    show_default=True,
)
@click.option(
    "-c",
    "--collection",
    metavar="name",
    default="test",
    help="Collection name.",
    show_default=True,
)
@click.option(
    "-H",
    "--host",
    metavar="host",
    default="0.0.0.0",
    help="Host name.",
    show_default=True,
)
@click.option(
    "-p",
    "--port",
    metavar="port",
    default=27017,
    help="Port number.",
    show_default=True,
)
@click.option(
    "-t",
    "--timeout",
    metavar="sec",
    default=5,
    help="Connection timeout (seconds).",
    show_default=True,
)
@click.option(
    "-f", "--force", default=False, is_flag=True, help="Overwrite collection if exists."
)
@click.option(
    "-y", "--yes", default=False, is_flag=True, help="Automatic yes to prompts."
)
@click.argument("file")
def cli(database, collection, host, port, timeout, force, yes, file):
    """Import a csv FILE to MongoDB"""

    # Connect to MongoDB client
    click.echo("....................................")
    click.echo(f"Connecting to {host}:{port}")
    click.echo("....................................")
    print()
    mongo_client = MongoClient(host, port, serverSelectionTimeoutMS=timeout)
    check_connection(mongo_client, host, port)

    # Get database, collection, and format csv to json
    db = mongo_client[database]
    coll = db[collection]
    data_csv = read_csv(file)
    data_json = loads(data_csv.to_json(orient="records"))

    # Ask for user confirmation on "database "and "collection"
    if not yes:
        # TODO: use "click.prompt"
        prompt = f"Import {basename(file)} to database={database} collection={collection} [y/N]? "
        if not match(r"[yY]", input(prompt)):
            cancel_upload()

    # Check if collection already exists
    if not force:
        if collection in db.collection_names():
            # TODO: use "click.prompt"
            prompt = f"Collection={collection} already exists. Overwrite [y/N]? "
            is_overwrite = match(r"[yY]", input(prompt))
            coll.remove() if is_overwrite else cancel_upload()

    # Insert collection into database
    coll.insert(data_json)

    click.echo(click.style("Import complete!", fg="green"))


def check_connection(mongo_client, host, port):
    try:
        mongo_client.server_info()
    except ServerSelectionTimeoutError as e:
        click.echo(f"Connection error while attempting to connect to {host}:{port}")
        exit(1)


def cancel_upload():
    print()
    click.echo(click.style("Import cancelled!", fg="red"))
    exit(1)


if __name__ == "__main__":
    cli()
