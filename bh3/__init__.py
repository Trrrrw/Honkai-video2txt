import easyocr
import asyncio
import cv2
import json
import os
import distance


class extract:
    def __init__(self, video_path) -> None:
        asyncio.run(self.extract_frame_main(video_path))

    async def extract_frame(self, capture, frame_index):
        """
        从视频中提取指定帧并对其进行 OCR 识别

        Args:
            capture: cv2.VideoCapture 对象，用于读取视频帧
            frame_index (int): 目标帧的索引

        Returns:
            result (list): 识别结果
        """
        # 移动到目标帧
        capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

        # 读取目标帧
        success, image = capture.read()

        # 裁切图像
        x, y, w, h = 288, 780, 1315, 249
        image_cropped = image[y:y+h, x:x+w]

        # 创建 OCR 读取器
        reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)

        # 识别图片并返回结果
        result = reader.readtext(image_cropped, detail=0)
        return result

        # 保存目标帧为图像文件
        # if success:
        #     cv2.imwrite('./frame/frame_{}.jpg'.format(frame_index),
        #                 image_cropped)

    async def extract_frame_main(self, video_path):
        """
        从视频中提取帧并保存为json文件

        Args:
            video_path (str): 视频文件的路径

        Returns:
            None

        """
        # 打开视频文件
        capture = cv2.VideoCapture(video_path)

        # 获取视频的帧率和总帧数
        fps = capture.get(cv2.CAP_PROP_FPS)
        total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

        # 每10帧提取一次画面
        tasks = [self.extract_frame(capture, i)
                 for i in range(0, total_frames, 10)]
        results = await asyncio.gather(*tasks)

        # 删除空数组,重复数组
        results = [sublist for sublist in results if sublist != []]
        results = [x for i, x in enumerate(results) if x not in results[:i]]

        # 初步筛选结果
        new_results = []
        for index, result in enumerate(results):
            if index < len(results)-1:
                dist = len("".join(results[index+1]))- len("".join(result))
                if dist < 0:
                    new_results.append(result)

        # 将结果保存为json
        name_without_extension = os.path.splitext(os.path.basename(video_path))[0]
        directory = os.path.dirname(video_path)
        full_path = os.path.join(directory, name_without_extension)
        with open(f'{full_path}.json', 'w') as json_file:
            json.dump(new_results, json_file, ensure_ascii=False)
