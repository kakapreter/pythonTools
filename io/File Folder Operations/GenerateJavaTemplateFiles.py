import os

def generate_java_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

def main():
    # 指定生成文件的范围（起始和结束值）
    start_index = 1
    end_index = 200

    # 指定Java文件的内容模板
    java_content_template = """package com.tedu.test;
public class Main%03d {
    public static void main(String[] args) {
        System.out.println("Hello from Main%03d!");
    }
}
"""

    # 指定生成文件的目录
    output_directory = "generated_java_files"

    # 创建目录
    os.makedirs(output_directory, exist_ok=True)

    # 生成文件
    for i in range(start_index, end_index + 1):
        file_name = os.path.join(output_directory, f"Main{i:03d}.java")
        java_content = java_content_template % (i, i)
        generate_java_file(file_name, java_content)

if __name__ == "__main__":
    main()
