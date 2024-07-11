def hello():
    print("hello world")


if __name__ == "__main__":
    # 测试时加上上面这句话可以避免模块被导入后还执行以下测试语句
    print("Please use me as a modules")
    hello()
