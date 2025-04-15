from PIL import Image
'task 10.1'
image_path = 'otkr.jpg'
image = Image.open(image_path)
crop_area = (100, 100, 200, 200)
cropped_image = image.crop(crop_area)
cropped_image.save('cropped_otkr.jpg')
'task 10.2'
postcards = {
    "Новый год": "new_year.jpg",
    "День рождения": "birthday.jpg",
    "8 марта": "march_8.jpg"
}
holid = input("Введите название праздника: ")
if holid in postcards:
    postcard_file = postcards[holid]
    postcard_image = Image.open(postcard_file)
    postcard_image.show()
else:
    print("Открытка для этого праздника не найдена")
'task 10.3'
from PIL import ImageDraw, ImageFont
def add_congratulation(image_path, name):
    image = Image.open(image_path).convert("RGBA")
    txt_layer = Image.new("RGBA", image.size)
    draw = ImageDraw.Draw(txt_layer)
    font_size = int(image.size[1] / 15)
    font_path = "/path/to/your/font.ttf"
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
    text = f"{name}, congr!"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    position = ((image.size[0] - text_width) // 2, 10)
    draw.text(position, text, fill=(255, 0, 0), font=font)
    watermarked_image = Image.alpha_composite(image.convert("RGBA"), txt_layer)
    return watermarked_image.convert("RGB")
name_to_congratulate = input("Введите имя того, кого хотите поздравить: ")
postcard_file_to_use = 'nulo.jpg'
final_image = add_congratulation(postcard_file_to_use, name_to_congratulate)
final_image.save('final_congratulation.png')