def getDataBitInfo(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    for byte in binary_data:
        print(format(byte, '08b'), end=' ')


if __name__ == '__main__':
    print("查看文档二进制信息")
    file_path = 'D:/Hello.txt'
    getDataBitInfo(file_path)

    '''
    print("\n")
    file_path2 = 'C:/Users/Administrator/Pictures/20210506173254168.png'
    print("查看图片二进制信息")
    getDataBitInfo(file_path2)
    '''

    '''
    print("\n")
    file_path3 = 'D:/1.mp4'
    print("查看mp4二进制信息+")
    getDataBitInfo(file_path3)
    '''
