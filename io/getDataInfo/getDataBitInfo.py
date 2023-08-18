"""
打印数据2进制信息
"""


def getDataBinaryInfo(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    bin_data = ' '.join(format(byte, '08b') for byte in binary_data)
    print(bin_data)
    print("显示完成")
    print("\n")


'''
打印数据16进制信息
'''


def getDataHexadecimalInfo(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    hex_data = ' '.join(format(byte, '02X') for byte in binary_data)
    print(hex_data)

    print("显示完成")
    print("\n")


if __name__ == '__main__':
    file_path = 'assets/Hello.txt'
    '''
    print("txt二进制信息")
    getDataBinaryInfo(file_path)
    '''
    '''
    print("txt十六进制信息")
    getDataHexadecimalInfo(file_path)
    '''

    file_path2 = 'assets/20210506173254168.png'
    '''
    print("png二进制信息")
    getDataBinaryInfo(file_path2)
    '''
    '''
    print("png十六进制信息")
    getDataHexadecimalInfo(file_path2)
    '''

    file_path3 = 'assets/1.mp4'
    '''
    print("mp4二进制信息")
    getDataBinaryInfo(file_path3)
    '''
    '''
    print("mp4十六进制信息")
    getDataHexadecimalInfo(file_path3)
    '''

    file_path4 = 'assets/1.md'
    '''
    print("md二进制信息")
    getDataBinaryInfo(file_path4)
    '''
    '''
    print("md十六进制信息")
    getDataHexadecimalInfo(file_path4)
    '''
