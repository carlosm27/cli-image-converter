from pathlib import Path

from file_checkers import webp_to_png, jpeg_to_png, webp_to_jpg, png_to_jpg
import typer

def callback():
    typer.echo("Converting files")

app = typer.Typer(callback=callback)


@app.command()
def png(path: Path):
    p = path
    if p.is_dir() == True :
        for child in p.iterdir():
            if child.suffix == ".webp":
                webp_to_png(child)
            elif child.suffix == ".jpg":
                jpeg_to_png(child)
            else:
                print("Not a file with extension .webp or .jpeg")
    
    elif p.is_file() == True:
        if p.suffix == ".webp":
            webp_to_png(p)
     
        elif p.suffix == ".jpg":
            jpeg_to_png(p)
    else:
        print("This is not a directory or file webp,jpeg")


@app.command()
def jpeg(path: Path):
    p = path
    if p.is_dir() == True:
        for child in p.iterdir():
            if child.suffix == ".webp":
                webp_to_jpg(child)
            elif child.suffix == ".png":
                png_to_jpg(child)
            else:
                print("Not a file with extension .webp or .png")

    elif p.is_file() == True:
        if p.suffix == ".webp":
            webp_to_jpg(p)

        elif p.suffix == ".jpg":
            png_to_jpg(p)
    else:
        print("This is not a directory or file webp, png")

if __name__=="__main__":
    app()




