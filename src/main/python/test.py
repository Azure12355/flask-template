import os

# 获取当前文件所在的目录（src/main/python/）
current_dir = os.path.dirname(os.path.abspath(__file__))
# 相对路径定位到 src/main/resource/application.yml
config_path = os.path.join(current_dir, '../resource/application.yml')
# 规范化路径
config_path = os.path.normpath(config_path)

print(config_path)