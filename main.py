# main.py
from models.multimodal_extractor import extract_text_from_image
from utils.postprocessing import structure_text
from utils.evaluation import evaluate_extraction
import os
import json
from PIL import Image

def main():
    image_folder = r'C:\Users\Rahul_Jindal\Downloads\archive\data'  # << Your real images folder
    output = []

    for img_file in os.listdir(image_folder):
        if img_file.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(image_folder, img_file)
            image = Image.open(img_path)
            raw_text = extract_text_from_image(image)
            structured_data = structure_text(raw_text)
            output.append({
                'image_file': img_file,
                'extracted_data': structured_data
            })

    with open('extracted_results.json', 'w') as f:
        json.dump(output, f, indent=4)

    print("Extraction Completed. Results saved to extracted_results.json")

if __name__ == "__main__":
    main()
