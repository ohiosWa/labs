from PIL import Image, ImageFilter
'task 9.1'
image = Image.open('bombombini gusini.jpg')
image.show()
print(f"size: {image.size}")
print(f"format: {image.format}")
print(f"cvet model: {image.mode}")
'task 9.2'
reduced_image = image.resize((image.width // 3, image.height // 3))
reduced_image.save('red_im.jpg')
horizontal_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
vertical_flip = image.transpose(Image.FLIP_TOP_BOTTOM)
horizontal_flip.save('horiz_flip.jpg')
vertical_flip.save('vert_flip.jpg')
'task 9.3'
import os
output_folder= 'fil_img'
os.makedirs(output_folder, exist_ok=True)
for i in range(1,6):
    image_path = f'{i}.jpg'
    image = Image.open(image_path)
    filtered_image= image.filter(ImageFilter.CONTOUR)
    filtered_image.save(os.path.join(output_folder, f'filtered_{i}.jpg'))
'task 9.4'
def add_watermark(image_path, watermark_text):
    base_image = Image.open(image_path).convert("RGBA")
    watermark_layer = Image.new("RGBA", base_image.size)
    from PIL import ImageDraw, ImageFont
    draw = ImageDraw.Draw(watermark_layer)
    font_size = int(base_image.size[1] / 20)
    font = ImageFont.load_default()
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    position = (base_image.size[0] - text_width - 10, base_image.size[1] - text_height - 10)
    draw.text(position, watermark_text, fill=(255, 255, 255), font=font)
    watermarked_image = Image.alpha_composite(base_image.convert("RGBA"), watermark_layer)
    return watermarked_image.convert("RGB")
watermark_text = "italianobro"
output_folder_watermarked = 'watermarked_images'
os.makedirs(output_folder_watermarked, exist_ok=True)
for i in range(1, 6):
    image_path = f'{i}.jpg'
    watermarked_image = add_watermark(image_path, watermark_text)
    watermarked_image.save(os.path.join(output_folder_watermarked, f'watermarked_{i}.jpg'))







