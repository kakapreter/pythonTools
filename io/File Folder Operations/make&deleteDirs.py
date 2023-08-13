import os
import shutil
'''
批量创建文件夹
parent_directory : 父路径
folder_prefix : 文件夹前缀
num_folders : 创建的数量(后缀)
'''
def makeDirs(parent_directory,folder_prefix,num_folders):
    # 使用循环批量创建文件夹
    for i in range(1, num_folders + 1):
        folder_name = f"{folder_prefix}{i}"
        folder_path = os.path.join(parent_directory, folder_name)
        # 使用os.path.exists()检查文件夹是否存在
        if os.path.exists(folder_path):
            print(f"文件夹'{folder_name}'已存在，跳过创建。")
        else:
            os.makedirs(folder_path)
            print(f"文件夹'{folder_name}'已创建在'{folder_path}'")
    print("批量创建完成！")

'''
批量删除文件夹
parent_directory : 父路径
'''
def deleteDirs(parent_directory):
    folder_names = [folder_name for folder_name in os.listdir(parent_directory) if
                    os.path.isdir(os.path.join(parent_directory, folder_name))]
    # 使用循环批量删除文件夹
    for folder_name in folder_names:
        folder_path = os.path.join(parent_directory, folder_name)
        try:
            shutil.rmtree(folder_path)
            print(f"文件夹'{folder_name}'已删除。")
        except OSError as e:
            print(f"无法删除文件夹'{folder_name}': {e}")
    print("批量删除完成！")


#批量创建文件夹
makeDirs('./imgs','img',5)

#批量删除文件夹
#deleteDirs('./imgs')
