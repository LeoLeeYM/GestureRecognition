hand_landmarks = None
mp_hands = None
from win32 import win32gui, win32print
from win32.lib import win32con

'''
一些数据处理函数
'''

# 计算指定手指的轴均值
def GetFingerAverage(fingerID : tuple, XorY : str) -> float: 
    finger = [4,8,12,16,20]
    if XorY == 'x':
        return sum(hand_landmarks.landmark[mp_hands.HandLandmark(finger[i]).value].x for i in fingerID) / len(fingerID)
    if XorY == 'y':
        return sum(hand_landmarks.landmark[mp_hands.HandLandmark(finger[i]).value].y for i in fingerID) / len(fingerID)

# 计算指定手指关节的轴均值
def GetFingerJointAverage(fingerID : tuple, XorY : str) -> float:
    finger = [3,6,10,14,18]
    if XorY == 'x':
        return sum(hand_landmarks.landmark[mp_hands.HandLandmark(finger[i]).value].x for i in fingerID) / len(fingerID)
    if XorY == 'y':
        return sum(hand_landmarks.landmark[mp_hands.HandLandmark(finger[i]).value].y for i in fingerID) / len(fingerID)

# 计算指定手指的轴均差
def GetFingerAverageDiff(fingerID : tuple, XorY : str) -> float:
    finger_ = [4,8,12,16,20]
    finger = [finger_[i] for i in fingerID]
    
    fingerDiff = []
    for i in range(len(finger)):
        for j in range(len(finger)):
            if i == j:
                continue
            if XorY == 'x':
                fingerDiff.append(abs(hand_landmarks.landmark[mp_hands.HandLandmark(finger[i]).value].x - hand_landmarks.landmark[mp_hands.HandLandmark(finger[j]).value].x))
            else:
                fingerDiff.append(abs(hand_landmarks.landmark[mp_hands.HandLandmark(finger[i]).value].y - hand_landmarks.landmark[mp_hands.HandLandmark(finger[j]).value].y))
    
    return sum(fingerDiff) / len(fingerDiff)
   
# 计算手指变化的轴值对应屏幕大小的像素值
def GetChangeCoordinateForScreen(x,y):

    hDC = win32gui.GetDC(0)
    w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)

    absX = abs(x)
    absY = abs(y)

    changePixelX = w * absX
    changePixelY = h * absY

    return (changePixelX if x >= 0 else changePixelX * -1, changePixelY if y >= 0 else changePixelY * -1)



