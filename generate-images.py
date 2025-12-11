#!/usr/bin/env python3
"""Generate images for Vibe Coding landing page using Gemini 2.5 Flash Image (Nano Banana)"""

from google import genai
from PIL import Image
import os

# Configure client with API key
client = genai.Client(api_key="AIzaSyCH3Z0GA--EvxQciPHbFaNhm_hw1TE0Zes")

# Image prompts - exciting tech/workspace scenes
prompts = [
    {
        "name": "hero-image.png",
        "prompt": "A vibrant modern tech workspace with glowing screens displaying beautiful colorful code and website mockups. Warm golden hour lighting streaming through large windows. Green potted plants, sleek laptops, coffee cups on a clean white desk. Inspirational creative atmosphere. High quality digital art, cinematic lighting."
    },
    {
        "name": "vibe-coder.png",
        "prompt": "A cozy creative corner with a laptop displaying a stunning colorful website design. Comfortable modern chair, warm ambient lighting, steaming coffee mug, small succulent plant. Inviting productive workspace vibes. Soft focus background. Professional lifestyle photography style, warm tones."
    },
    {
        "name": "success-moment.png",
        "prompt": "A celebratory scene with a laptop screen showing a successfully launched website with sparkles and confetti effects around it. Modern minimalist desk with plants and warm lighting. Achievement and success theme. Bright cheerful atmosphere. Digital art style, vibrant colors."
    }
]

output_dir = "/home/student/Lessons/L6/vibe-coding-landing/images"
os.makedirs(output_dir, exist_ok=True)

print("Using Gemini 2.5 Flash Image (Nano Banana)")
print("=" * 50)

for i, item in enumerate(prompts, 1):
    print(f"\n[{i}/3] Generating: {item['name']}")
    print(f"Prompt: {item['prompt'][:70]}...")

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=[item['prompt']],
        )

        # Process response parts
        saved = False
        for part in response.parts:
            if part.text is not None:
                print(f"Text: {part.text[:100]}...")
            elif part.inline_data is not None:
                image = part.as_image()
                filepath = os.path.join(output_dir, item['name'])
                image.save(filepath)
                print(f"SUCCESS! Saved: {filepath}")
                saved = True
                break

        if not saved:
            print(f"No image generated for {item['name']}")

    except Exception as e:
        print(f"Error: {e}")

print("\n" + "=" * 50)
print("Done! Checking images folder:")
os.system(f"ls -la {output_dir}")
