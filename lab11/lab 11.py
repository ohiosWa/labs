'11.1'
import os
from PIL import Image
inpf = 'img_inp'
outf = 'img_out'
os.makedirs(outf, exist_ok=True)
for filename in os.listdir(inpf):
    if filename.lower().endswith(('.jpg','.jpeg','.png','.bmp','.gif')):
        input_path = os.path.join(inpf, filename)
        output_path = os.path.join(outf, filename)
        try:
            with Image.open(input_path) as img:
                new_size = (img.width // 2, img.height // 2)
                resized_img = img.resize(new_size)
                resized_img.save(output_path)
                print(f"obrabotano: {filename}")
        except Exception as e:
            print(f"oshibka {filename}: {e}")
'11.2'
inpf = 'img_inp'
outf = 'img_filtr_out'
os.makedirs(outf, exist_ok=True)
allowd_ext = ('.jpg','.png')
for filename in os.listdir(inpf):
    if filename.lower().endswith(allowd_ext):
        input_path = os.path.join(inpf, filename)
        output_path = os.path.join(outf, filename)
        try:
            with Image.open(input_path) as img:
                bw_img = img.convert('L')
                bw_img.save(output_path)
                print(f"obrabot: {filename}")
        except Exception as e:
            print(f"oshibk {filename}: {e}")
'11.3'
import csv
csv_filename = 'product.csv'
total_sum = 0
print("nyjno kypit:")
with open(csv_filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        product = row['Продукт']
        quant = int(row['Количество'])
        price = int(row['Цена'])
        total_sum += quant * price
        print(f"{product}-{quant} sht. za {price} rub.")
print(f"itog: {total_sum} rub.")

