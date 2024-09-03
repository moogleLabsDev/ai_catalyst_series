import os
import uuid
import base64
import logging

import firebase_admin
from firebase_admin import credentials, storage as fb_storage

from google.api_core.exceptions import GoogleAPICallError
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to generate image
def generate_image_base64(prompt_text: str):
    location = ''
    project_id = ""
    vertexai.init(project=project_id, location=location)
    model = ImageGenerationModel.from_pretrained("imagegeneration@006")
    images = []
    while not images:
        try:
            logger.info(f"Generating image for: {prompt_text}")
            images = model.generate_images(
                prompt=prompt_text,
                number_of_images=1,
                language="en",
                aspect_ratio="1:1",
                safety_filter_level="block_few",
                person_generation="allow_adult",
            )
        except GoogleAPICallError as exp:
            logger.error(f"Error while generating the image: {exp}")
            prompt_text = ' '.join(prompt_text.split(' ')[0:-2])  # if failed: remove the last word
            continue
    if images:
        return images[0]._as_base64_string()

def save_to_firebase(blob_file_path: str, base_64_string: str, content_type: str='image/png') -> str:
    decoded_file = base64.b64decode(base_64_string)
    bucket = fb_storage.bucket()
    blob = bucket.blob(blob_file_path)
    blob.upload_from_string(decoded_file, content_type=content_type)
    blob.make_public()
    logger.info("Uploaded to Firebase with URL: {}".format(blob.public_url))
    return blob.public_url

def generate_image(prompt_text: str):
    image_description = prompt_text
    base_64_string = None
    while not base_64_string:
        base_64_string = generate_image_base64(prompt_text)
    image_url = save_to_firebase(f'generated_images/{str(uuid.uuid4())}.png', base_64_string, 'image/png')
    return image_url, image_description

# Main testing script
if __name__ == "__main__":
    # Set environment variables for Google Cloud and Firebase
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 's.json'

    # Initialize Firebase
    cred = credentials.Certificate(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
    firebase_bucket_path = ''
    firebase_admin.initialize_app(cred, {'storageBucket': firebase_bucket_path})

    # Test prompts
    test_prompts = [
        "photo of a pumpkin",
        
    ]

    for prompt in test_prompts:
        try:
            image_url, description = generate_image(prompt)
            logger.info(f"Generated image for prompt '{prompt}': {image_url}")
        except Exception as e:
            logger.error(f"Failed to generate image for prompt '{prompt}': {e}")
