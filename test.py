class MessagePrinter:
    def __init__(self, default_message):
        self.default_message = default_message  # インスタンス変数の設定

    def print_message(self, message=None):
        if message is None:
            message = self.default_message  # インスタンス変数の使用
        print(message)

# インスタンスの作成とメソッドの呼び出し
printer = MessagePrinter("Default Message")
printer.print_message("Hello, World!")  # "Hello, World!" を出力
printer.print_message()  # "Default Message" を出力（default_messageを使用）
