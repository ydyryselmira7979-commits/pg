import sys


jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'



def read_header(file_name, header_length):
    try:
        f = open(file_name, 'rb')      # открываем в двоичном режиме
        data = f.read(header_length)   # читаем нужное количество байт
        f.close()
        return data
    except:
        return b''                     # если ошибка — возвращаем пусто



def is_jpeg(file_name):
    header = read_header(file_name, len(jpeg_header))
    return header == jpeg_header



def is_gif(file_name):
    header = read_header(file_name, 6)
    return header == gif_header1 or header == gif_header2



def is_png(file_name):
    header = read_header(file_name, len(png_header))
    return header == png_header



def print_file_type(file_name):
    if is_jpeg(file_name):
        print(f"{file_name} je JPEG")
    elif is_gif(file_name):
        print(f"{file_name} je GIF")
    elif is_png(file_name):
        print(f"{file_name} je PNG")
    else:
        print(f"{file_name} je neznámý typ")



if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
        print_file_type(file_name)
    except:
        print("Chyba: zadej jméno souboru
