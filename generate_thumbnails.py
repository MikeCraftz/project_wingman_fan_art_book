import os
from PIL import Image

IMG_DIR = 'static/img'
THUMB_DIR = os.path.join(IMG_DIR, 'thumbs')

def generate_thumbnails():
    if not os.path.exists(THUMB_DIR):
        os.makedirs(THUMB_DIR)
        print(f"Created directory: {THUMB_DIR}")

    # Supported extensions
    exts = ('.jpg', '.jpeg', '.png')

    for filename in os.listdir(IMG_DIR):
        if filename.lower().endswith(exts):
            file_path = os.path.join(IMG_DIR, filename)
            
            # Create thumbnail filename
            thumb_path = os.path.join(THUMB_DIR, filename)

            if os.path.exists(thumb_path):
                print(f"Skipping {filename}, thumbnail exists.")
                continue

            try:
                with Image.open(file_path) as img:
                    # Maintain aspect ratio, max width 600
                    img.thumbnail((600, 600))
                    
                    # Save
                    img.save(thumb_path, optimize=True, quality=85)
                    print(f"Generated thumbnail for {filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

if __name__ == "__main__":
    generate_thumbnails()
