# 崩坏3文本提取
代码有种Chat-GPT的美😋

## 使用方法
### 下载
```bash
git clone https://github.com/Trrrrw/Honkai-video2txt.git
```
或下载压缩包解压

### 环境
Python（编写环境为3.10）
```bash
pip install -r requirements.txt
```

### 使用
用文本编辑器打开`start.py`，修改
```python
video_folder = '存放视频的文件夹路径'
video_type = '文件类型，例如:mp4、mkv'
```

### 结果
结束后会生成与视频同名的json文件，由于是对视频每10帧进行一次ocr，所有会有一些重复，需要手动筛选。

## 参考
[崩坏3剧情/崩坏三剧情游戏CG＋对话整理（活动篇1）(更新至5.0活动 盛夏海滨游乐园-04）](https://www.bilibili.com/video/BV1wy4y157ou)