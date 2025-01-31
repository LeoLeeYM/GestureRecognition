# GestureRecongnition - 基于MediaPipe的手势识别与控制

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-orange)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.8.9%2B-green)

[English Readme](https://github.com/LeoLeeYM/GestureRecognition/blob/main/README_EN.md)

## 项目概述

本项目基于MediaPipe的手势识别技术，通过计算机摄像头实时捕捉手势动作，实现多种手势交互功能。支持屏幕控制、媒体操作、文字输入等多种交互方式，可作为人机交互的扩展方案。

## 主要功能

### 已实现手势
- ✋ 张开手：截图保存
- 👊 握拳：触发屏幕操作
- 👇 下滑手势：页面滚动
- 🤏 捏合手势：音量控制
- 🤞 并拢手势：鼠标移动
- →← 左右张开：媒体控制

### 支持操作
- 屏幕截图
- 音量调节
- 媒体控制（前进/后退）
- 鼠标移动控制
- 自动文字输入
- 页面滚动

## 快速开始

### 环境要求
- Python 3.7+
- 摄像头设备

### 安装依赖
```bash
pip install opencv-python mediapipe pyautogui pywin32
```

### 运行程序
```bash
python core.py
```

## 使用说明
1. 确保摄像头正常工作
2. 保持手部在摄像头可视范围内
3. 使用标准手势进行交互：
   - **张开手 → 握拳**：屏幕截图
   - **反向张开 → 张开**：页面向上滚动
   - **捏合手势上下移动**：音量控制
   - **并拢手势移动**：控制鼠标
   - **左右张开切换**：媒体控制（左/右键）

## 代码结构
```
GestureControl/
├── core.py            # 主程序入口
├── data.py            # 手势数据处理
├── gestureLib.py      # 手势定义库
├── handle.py          # 手势处理逻辑
└── tool.py            # 工具函数
```

## 实现原理
1. **手势检测**：使用MediaPipe Hands模型进行21个手部关键点检测
2. **数据处理**：计算手指关节坐标差值、均值等特征参数
3. **手势识别**：通过几何特征阈值判断手势类型
4. **动作映射**：将手势转换为系统操作（pyautogui实现）

## 开发文档

### 关键参数
- `distanceCoefficient`：距离系数（动态计算）
- `fingerOriginDiff`：手指相对手掌根部的偏移量
- `fingerJointAverage`：关节平均位置

### 扩展手势
1. 在`gestureLib.py`中添加新手势的判断条件
2. 在`handle.py`中实现对应的处理逻辑
3. 更新手势起始判断和状态转换逻辑

## 贡献指南
欢迎通过Issue或PR参与项目改进：
1. Fork项目仓库
2. 创建特性分支（git checkout -b feature/AmazingFeature）
3. 提交修改（git commit -m 'Add some AmazingFeature'）
4. 推送分支（git push origin feature/AmazingFeature）
5. 发起Pull Request

## 注意事项
- 确保pyautogui的FAILSAFE功能已禁用
- 手势识别效果受光照条件和摄像头质量影响
- 部分系统操作需要管理员权限

## 开源协议
[MIT License](LICENSE)

---

**提示**：建议在Python虚拟环境中运行本项目，保持依赖环境干净。首次运行时会自动下载MediaPipe的预训练模型（约10MB）。
