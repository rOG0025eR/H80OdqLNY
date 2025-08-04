# 代码生成时间: 2025-08-04 19:10:14
import requests

# 定义排序算法
class SortingService:
    def __init__(self):
        pass

    def bubble_sort(self, arr):
        """冒泡排序算法

        参数:
        arr (list): 需要排序的列表

        返回:
        list: 排序后的列表
        """
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def quick_sort(self, arr):
        """快速排序算法

        参数:
        arr (list): 需要排序的列表

        返回:
        list: 排序后的列表
        """
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return self.quick_sort(less_than_pivot) + [pivot] + self.quick_sort(greater_than_pivot)

    def selection_sort(self, arr):
        """选择排序算法

        参数:
        arr (list): 需要排序的列表

        返回:
        list: 排序后的列表
        """
        for i in range(len(arr)):
            min_index = i
            for j in range(i+1, len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

# 测试排序算法
if __name__ == '__main__':
    # 初始化排序服务
    sorting_service = SortingService()

    # 测试数据
    test_data = [64, 34, 25, 12, 22, 11, 90]

    # 冒泡排序测试
    print("冒泡排序结果：", sorting_service.bubble_sort(test_data.copy()))
    # 快速排序测试
    print("快速排序结果：", sorting_service.quick_sort(test_data.copy()))
    # 选择排序测试
    print("选择排序结果：", sorting_service.selection_sort(test_data.copy()))