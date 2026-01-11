# *_* coding : UTF-8 *_*
# 开发团队 ：乐育科技
# 开发人员 ：zcq
# 开发时间 ：2022/6/11 9:39
# 文件名称 ：main.PY 
# 开发工具 ：PyCharm
from PyQt5.Qt import *
import sys
from ParamMonitor import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ParamMonitor()
    window.show()
    sys.exit(app.exec_())