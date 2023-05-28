# 崩坏3文本提取

## 使用方法
### 下载
```bash
git clone https://github.com/Trrrrw/bh3video2txt.git
```
或下载压缩包解压

### 使用
用文本编辑器打开`start.py`，修改
```python
video_folder = '存放视频的文件夹路径'
video_type = '文件类型，例如:mp4、mkv'
```

### 结果
结束后会生成与视频同名的json文件，由于是对视频每10帧进行一次ocr，所有会有一些重复，需要手动筛选。