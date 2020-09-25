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
    # display details about the search key for the job provided on the command line
    typer.echo("")
    typer.echo(f"  We are looking for contacts who have a job related to {job_description}")
    # perform the search for all of the relevant email addresses given the job description
    contacts_list = search.search_for_email_given_job(job_description, contacts_text)
    # we know that there are some contacts in the list, so iterate through the list of
    # the contacts and display them in the terminal window
    if contacts_list:
        typer.echo("")
        for contact in contacts_list:
            print("  " + " is a ".join(map(str, contact)))
    # display final information about the program's behavior in the terminal window
    typer.echo("")
    # if no contacts were found, then display a suitable statement
    if len(contacts_list) == 0:
        typer.echo("Sorry, we could not find any contacts who have your desired job! Try again!")
    # if contacts were found, then display a suitable statement 
    else:
        typer.echo("Wow, we found some contacts! Email them to learn about your job!")


if __name__ == "__main__":
    main()
