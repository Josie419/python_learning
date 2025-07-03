'''
创建 BankAccount 类
包含属性：account_holder(账户名), balance(余额)
实现方法：
    deposit(amount)：存款
    withdraw(amount)：取款（需检查余额）
基础功能测试：
python
    acc = BankAccount("小明", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc.balance)  # 应输出1300

需掌握知识点：
    类属性初始化 (__init__)
    实例方法操作属性 (self.balance += amount)
    基础条件判断（取款时检查余额）
'''


class BankAccount:
    # 初始化账户名和余额
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    # 存款
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金额需为正数")    #raise是主动抛出异常
        self.balance += amount
        print(f"{self.account_holder}账户，存入{amount}，当前余额：{self.balance}")
    # 取款
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("取款金额需为正数")
        if amount > self.balance:
            raise ValueError("钱不够还敢取？")
        self.balance -= amount
        print(f"{self.account_holder}账户，取出{amount}，剩余余额：{self.balance}")


p1 = BankAccount("大佬A", 10000)
p2 = BankAccount("辣鸡B", 100)
p1.deposit(3000) #13000


p2.withdraw(110)

