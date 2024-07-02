# laufen.py

from PIL import Image
import os

# Verzeichnis, in dem sich die Bilder befinden
image_dir = 'static/images'
# Namen der zu skalierenden Bilder
image_names = ['arnold_walk9.png', 'arnold_walk10.png', 'arnold_walk11.png']

# Zielgröße
target_size = (64, 64)

for image_name in image_names:
    image_path = os.path.join(image_dir, image_name)
    # Bild öffnen
    image = Image.open(image_path)
    # Bild skalieren auf 64x64 Pixel
    resized_image = image.resize(target_size, Image.LANCZOS)
    # Pfad für das skalierten Bild
    new_image_path = os.path.join(image_dir, f'resized_{image_name}')
    # Skaliertes Bild speichern
    resized_image.save(new_image_path)
    print(f"Das Bild {image_name} wurde erfolgreich auf 64x64 Pixel skaliert und gespeichert unter {new_image_path}")


# Verzeichnis, in dem sich die Bilder befinden
image_dir = 'static/images'
# Namen der zu skalierenden Bilder
image_names = ['hannes_walk9.png', 'hannes_walk10.png', 'hannes_walk11.png']

# Zielgröße
target_size = (64, 64)

for image_name in image_names:
    image_path = os.path.join(image_dir, image_name)
    # Bild öffnen
    image = Image.open(image_path)
    # Bild skalieren auf 64x64 Pixel
    resized_image = image.resize(target_size, Image.LANCZOS)
    # Pfad für das skalierten Bild
    new_image_path = os.path.join(image_dir, f'resized_{image_name}')
    # Skaliertes Bild speichern
    resized_image.save(new_image_path)
    print(f"Das Bild {image_name} wurde erfolgreich auf 64x64 Pixel skaliert und gespeichert unter {new_image_path}")