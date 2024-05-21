import typer
from commands.init import Init
from commands.this_file import ThisFile
from commands.create import Create
from helpers.constants import EXTENSIONS

app = typer.Typer()


# TODO: Validate the input
@app.command(name='init')
def init(name: str = typer.Argument(None), extension: str = typer.Option(EXTENSIONS.TXT.value)):
    Init(main_dir_name=name, extension=extension).run()


@app.command()
def goodbye():
    typer.echo('Goodbye!')


@app.command()
def create(path: str = typer.Argument(None), entry_point_file: str = typer.Option("index.txt"),
           strict: bool = typer.Option(True)):
    Create(path, entry_point_file, strict).run()


@app.command()
def update(name: str = typer.Argument(None), extension: str = typer.Option(EXTENSIONS.TXT.value)):
    pass


@app.command()
def this_file(file_path: str = typer.Argument(None), out_dir: str = typer.Option("out"),
              extension: str = typer.Option(EXTENSIONS.TXT.value)):
    ThisFile(file_path, out_dir, extension).run()


if __name__ == "__main__":
    app()
