# import random
# history=[]
# def guess_number():
#     answer = random.randint(1, 10)
#     print("欢迎参加猜数字游戏！你有3次机会~")
#
#     for i in range(1, 4):  # 循环3次（1,2,3）
#
#         try:
#             guess = int(input(f"第{i}次尝试，请输入1-10的数字: "))
#         #异常输入处理，防止报错
#         except ValueError:
#             print("请输入有效数字！")
#             continue
#
#         if guess == answer:
#             print("真棒~恭喜你猜对啦！")
#             print(f"你一共猜了{i}次")
#             history.append(f'{i}次')
#             print(f"历史记录: {history[-5:]}")  # 只显示最近5条
#             return  # 猜对后结束游戏
#
#         elif guess > answer:
#             print("小菜比，你猜大啦！")
#         else:
#             print("小菜比，你猜小啦")
#
#         if i==3:
#             history.append("失败")
#             print(f"历史记录: {history[-5:]}")  # 只显示最近5条
#     print(f"游戏结束，正确答案是: {answer}")
#
# # 测试连续玩多局
# while True:
#     guess_number()
#     if input("再玩一局？(y/n): ").lower() != 'y':
#         break



# 导入所需模块
import random  # 生成随机数
import json  # 处理JSON文件
import os  # 文件路径操作

# 常量定义：历史记录存储文件名
HISTORY_FILE = "guess_game_history.json"


def save_history(history):
    """
    将历史记录保存到JSON文件
    :param history: 要保存的历史记录列表
    """
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:  # 以写入模式打开文件
        json.dump(history, f, ensure_ascii=False)  # 是 Python 中用于将数据写入 JSON 文件的关键方法,ensure_ascii=False支持中文
        print(f"历史记录已保存到 {HISTORY_FILE}")


def load_history():
    """
    从JSON文件加载历史记录
    :return: 历史记录列表（文件不存在时返回空列表）
    """
    if os.path.exists(HISTORY_FILE):  # 检查文件是否存在
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)  # 读取并解析JSON数据
            except json.JSONDecodeError:
                print("警告：历史记录文件损坏，已重置")
                return []
    return []  # 默认返回空列表


class GuessGame:
    """猜数字游戏类（封装游戏逻辑）"""

    def __init__(self):
        """初始化游戏实例时自动加载历史记录"""
        self.history = load_history()  # 调用加载方法
        print("历史记录加载完成")

    def play(self):
        """执行单局游戏"""
        answer = random.randint(1, 10)  # 生成1-10的随机答案
        print(f"\n==== 新游戏开始 ====")
        print(f"最近记录: {self.history[-5:]}\n")  # 显示最近5条记录

        # 最多允许猜3次
        for attempt in range(1, 4):
            try:
                guess = int(input(f"第{attempt}次尝试，输入1-10的数字: "))
            except ValueError:  # 处理非数字输入
                print("请输入有效数字！")
                continue

            # 判断猜测结果
            if guess == answer:
                result = f'第{attempt}次猜中'
                self.history.append(result)
                save_history(self.history)  # 立即保存
                print(f"🎉 {result}")
                print(f"更新记录: {self.history[-5:]}")
                return  # 结束当前游戏

            print("猜大了" if guess > answer else "猜小了")

        # 三次都未猜中
        result = "失败"
        self.history.append(result)
        save_history(self.history)
        print(f"游戏结束！答案是 {answer}")
        print(f"更新记录: {self.history[-5:]}")


if __name__ == "__main__":
    """主程序入口"""
    print("====== 猜数字游戏 ======")
    print("规则：猜1-10的数字，最多3次机会\n")

    game = GuessGame()  # 创建游戏实例

    # 主循环
    while True:
        game.play()  # 开始一局游戏
        # 询问是否继续
        if input("\n再玩一局？(y/n): ").strip().lower() != 'y':
            print("\n==== 游戏结束 ====")
            print("最终历史记录:", game.history[-5:])
            break  # 退出循环

