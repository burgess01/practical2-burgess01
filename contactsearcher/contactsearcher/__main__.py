"""Define the command-line interface for the contact searching program."""

from pathlib import Path
from typing import Optional


import typer

from contactsearcher import search


def main(
    job_description: str = typer.Option(..., prompt=True),
    contacts_file: Optional[Path] = typer.Option(None),
):
    """Search for either an email address of a contact who has a job in the file."""
    # display details about the file provided on the command line
    # --> the file was not specified so we cannot continue using program
    if contacts_file is None:
        typer.echo("No contacts file specified!")
        raise typer.Abort()
    # --> the file was specified and it is valid so we should read and check it
    if contacts_file.is_file():
        contacts_text = contacts_file.read_text()
        contacts_line_count = len(contacts_text.splitlines())
        typer.echo(
            f"The contacts file contains {contacts_line_count} people in it! Let's get searching!"
        )
    # --> the file was specified but it does not exist so we cannot continue using program
    elif not contacts_file.exists():
        typer.echo("The contacts file does not exist!")
    # TODO: display details about the search key for the job provided on the command line
    # TODO: perform the search for all of the relevant email addresses given the job description
    # we know that there are some contacts in the list, so iterate through the list of
    # the contacts and display them in the terminal window
    if contacts_list:
        typer.echo("")
        for contact in contacts_list:
            print("  " + " is a ".join(map(str, contact)))
    # TODO: display final information about the program's behavior in the terminal window
    # TODO: if no contacts were found, then display a suitable statement
    # TODO: if contacts were found, then display a suitable statement
    # TODO: refer to the README.md file for the precise outputs for these conditions


if __name__ == "__main__":
    # TODO: indirectly call the main function through the typer.run function
