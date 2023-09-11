import sys
import os
import markdown


class FileConverter:
    def __init__(self):
        self.args: list = []
        self.input_md_path: str = ''
        self.input_html_path: str = ''
        self.html_elements: str = ''

    def is_md_file(self, file_path: str) -> bool:
        file_extension: str = file_path.split('.')[-1].lower()
        return file_extension == 'md'

    def is_html_file(self, file_path: str) -> bool:
        file_extension: str = file_path.split('.')[-1].lower()
        return file_extension == 'html'

    def is_exist_file(self, file_path: str) -> bool:
        return os.path.isfile(file_path)

    def is_valid_command(self) -> bool:
        if not len(self.args) == 3:
            print('\nエラー: 正しい入力形式ではありません。')
            return False
        if not self.is_md_file(self.args[1]):
            print('\nエラー: mdファイルを指定してください。')
            return False
        if not self.is_html_file(self.args[2]):
            print('\nエラー: HTMLファイルを指定してください。')
            return False

        self.input_md_path = self.args[1]
        self.input_html_path = self.args[2]

        if not self.is_exist_file(self.input_md_path) or not self.is_exist_file(self.input_html_path):
            print('\nエラー: 存在しないファイルを指定しています。')
            return False

        return True

    def create_html_elements(self):
        md_contents: str = ''

        with open(self.input_md_path, 'r') as md_file:
            md_contents = md_file.read()

        self.html_elements = markdown.markdown(md_contents)

    def is_overwrite_allowed(self) -> bool:
        overwrite_permission: str = input(
            '\nHTMLファイルの内容が上書きされます。許可しますか？ (y/n): ')

        while overwrite_permission not in ["y", "n", 'Y', 'N']:
            print("\nエラー: 無効な入力です。'y' または 'n' を入力してください。")
            overwrite_permission = input(
                '\nHTMLファイルの内容が上書きされます。許可しますか？ (y/n): ')

        if overwrite_permission == 'n' or overwrite_permission == 'N':
            print('\n処理を中止しました。')
            return False

        return True

    def analyze_command(self):
        self.args = sys.argv

        if not self.is_valid_command():
            return

        if self.is_overwrite_allowed():
            self.create_html_elements()

            with open(self.input_html_path, "w") as html_file:
                html_file.write(self.html_elements)
            print('\n完了しました。')


file_converter: object = FileConverter()
file_converter.analyze_command()
