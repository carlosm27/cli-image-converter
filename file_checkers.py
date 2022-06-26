from pathlib import Path


from PIL import Image



def webp_to_png(path: Path):
    p = path
    if p.suffix == (".webp"):
        im = Image.open(p).convert("RGB")
        file_name = p.name
        img_png = file_name.replace(".webp", ".png")
        im.save("./ " +img_png, "png")
    else:
        print("Not a .webp file")

def jpeg_to_png(path: Path):
    p = path
    if p.suffix == (".jpg"):
        im = Image.open(p).convert("RGB")
        file_name = p.name
        img_png = file_name.replace(".jpg", ".png")
        im.save("./ " +img_png, "png")
    else:
        print("Not a .jpg file")

def webp_to_jpg(path:Path):
    p = path
    if p.suffix == ".webp":
        im = Image.open(p).convert("RGB")
        file_name = p.name
        img_jpg = file_name.replace(".webp", ".jpg")
        im.save("./"+img_jpg, "png")
    else:
        print("Not a .webp file")

def png_to_jpg(path:Path):
    p = path
    if p.suffix == ".png":
        im = Image.open(p).convert("RGB")
        file_name = p.name
        img_jpg = file_name.replace(".png", ".jpg")
        im.save("./"+img_jpg, "png")
    else:
        print("Not a .png file")