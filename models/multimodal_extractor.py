# models/multimodal_extractor.py
from transformers import DonutProcessor, VisionEncoderDecoderModel
import torch

# Load PUBLIC pre-trained Donut model
processor = DonutProcessor.from_pretrained('naver-clova-ix/donut-base')
model = VisionEncoderDecoderModel.from_pretrained('naver-clova-ix/donut-base')

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)

def extract_text_from_image(image):
    # Preprocess image
    pixel_values = processor(image, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)
    
    # Generate output
    outputs = model.generate(pixel_values, max_length=512)
    sequence = processor.batch_decode(outputs, skip_special_tokens=True)[0]
    return sequence
