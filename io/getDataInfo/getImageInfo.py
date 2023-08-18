def getImageInfo(path):
    # 打开图片文件
    image_file_path = path  # 替换为实际的图片文件路径
    with open(image_file_path, 'rb') as file:
        image_binary_data = file.read()

    # 打印所有字节的十六进制表示
    hex_representation = ' '.join(format(byte, '02X') for byte in image_binary_data)
    print("所有字节的十六进制表示:")
    print(hex_representation)


if __name__ == '__main__':
    path = 'C:/Users/Administrator/Pictures/20210506173254168.png'
    getImageInfo(path)
