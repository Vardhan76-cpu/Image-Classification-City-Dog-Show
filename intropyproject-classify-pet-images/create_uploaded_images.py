from PIL import Image, ImageOps, ImageDraw
from pathlib import Path


output_dir = Path("uploaded_images")
output_dir.mkdir(exist_ok=True)


# Create Dog_01.jpg
dog = Image.new("RGB", (400, 400), "white")
draw = ImageDraw.Draw(dog)

draw.ellipse((90, 100, 310, 320), fill="#D9A441")
draw.ellipse((120, 70, 180, 150), fill="#B8792E")
draw.ellipse((220, 70, 280, 150), fill="#B8792E")

draw.ellipse((150, 180, 170, 200), fill="black")
draw.ellipse((230, 180, 250, 200), fill="black")
draw.ellipse((180, 230, 220, 265), fill="black")

dog.save(
    output_dir / "Dog_01.jpg",
    "JPEG",
    quality=95
)


# Create Dog_02.jpg by horizontally flipping Dog_01
dog_flipped = ImageOps.mirror(dog)

dog_flipped.save(
    output_dir / "Dog_02.jpg",
    "JPEG",
    quality=95
)


# Create Cat_01.jpg
cat = Image.new("RGB", (400, 400), "white")
draw = ImageDraw.Draw(cat)

draw.ellipse((100, 100, 300, 320), fill="#999999")

draw.polygon(
    [(110, 130), (130, 60), (180, 130)],
    fill="#777777"
)

draw.polygon(
    [(220, 130), (270, 60), (290, 130)],
    fill="#777777"
)

draw.ellipse((145, 175, 165, 195), fill="green")
draw.ellipse((235, 175, 255, 195), fill="green")

draw.polygon(
    [(195, 215), (205, 215), (200, 225)],
    fill="pink"
)

cat.save(
    output_dir / "Cat_01.jpg",
    "JPEG",
    quality=95
)


# Create Laptop_01.jpg
laptop = Image.new("RGB", (400, 400), "white")
draw = ImageDraw.Draw(laptop)

draw.rectangle(
    (70, 80, 330, 260),
    fill="#555555",
    outline="black",
    width=5
)

draw.rectangle(
    (90, 100, 310, 240),
    fill="#D0D0D0"
)

draw.polygon(
    [(50, 270), (350, 270), (380, 320), (20, 320)],
    fill="#888888",
    outline="black"
)

draw.rectangle(
    (100, 280, 300, 305),
    fill="#444444"
)

laptop.save(
    output_dir / "Laptop_01.jpg",
    "JPEG",
    quality=95
)


print("Created uploaded images successfully.")
print()
print("Dog_01.jpg")
print("Dog_02.jpg")
print("Cat_01.jpg")
print("Laptop_01.jpg")