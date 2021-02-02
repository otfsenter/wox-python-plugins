# -*- coding: utf-8 -*-
# 固定写法，导入相关类库和函数
from util import WoxEx, WoxAPI, load_module, Log

# 统一加载模块
with load_module():
    from datetime import datetime


class Main(WoxEx):  # 继承WoxEx

    def query(self, keyword):
        results = list()
        results.append({
            "Title": "input",
            "SubTitle": keyword,
            "IcoPath": "Images/ico.ico",
            "JsonRPCAction": {
                "method": "update_todo",
                "parameters": [keyword],
                "dontHideAfterAction": False
            }
        })
        return results

    def get_minute(self):
        today = datetime.now()
        year_month_day = str(today).split(' ')[0]
        hour_min = ':'.join([
            str(today.hour),
            str(today.minute)
        ])
        return ' '.join([year_month_day, hour_min])

    def update_todo(self, keyword):
        file_todo = r'D:\note\docs\source\0-todo.rst'
        with open(file_todo, 'a', encoding='utf-8') as f:
            f.write('\n' +
                    '- [ ] (%s) ' % self.get_minute() +
                    str(keyword) + '\n')


if __name__ == "__main__":
    Main()
