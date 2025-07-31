# 代码生成时间: 2025-07-31 10:48:09
import os
import requests
from typing import List, Tuple

"""
批量文件重命名工具
"""

class BatchRenameTool:
    def __init__(self, directory: str):
        """
        初始化工具，设置目录
        :param directory: 文件所在的目录
        """
        self.directory = directory

    def get_files(self) -> List[str]:
        """
        获取目录下的所有文件
        :return: 文件列表
        """
        try:
            return os.listdir(self.directory)
        except OSError as e:
            print(f"Error accessing directory: {e}")
            return []

    def rename_files(self, file_names: List[str], new_names: List[str]) -> None:
        """
        批量重命名文件
        :param file_names: 原始文件名列表
        :param new_names: 新文件名列表
        """
        if len(file_names) != len(new_names):
            raise ValueError("File name lists must be the same length")

        for old_name, new_name in zip(file_names, new_names):
            try:
                os.rename(os.path.join(self.directory, old_name),
                          os.path.join(self.directory, new_name))
            except OSError as e:
                print(f"Error renaming file {old_name} to {new_name}: {e}")

    def run(self, new_names: List[str]) -> None:
        """
        执行重命名操作
        :param new_names: 新文件名列表
        """
        files = self.get_files()
        self.rename_files(files, new_names)


def main():
    directory = "/path/to/your/directory"  # 替换为你的目录路径
    new_names = ["new_file_1.txt", "new_file_2.txt", "new_file_3.txt"]  # 替换为你的新文件名
    tool = BatchRenameTool(directory)
    tool.run(new_names)

if __name__ == "__main__":
    main()