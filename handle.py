import time
import tool
import pyautogui
import data
import gestureLib

nowStart = ''
fingerToOriginDistance = 0
distanceCoefficient = 0 # 距离系数
startKneadingTime = 0
nowKneadingY = 0
nowKneadingX = 0

handIntime = 0

pyautogui.FAILSAFE=False

def Handle(hand_landmarks, mp_hands):

    global nowStart
    global fingerToOriginDistance
    global distanceCoefficient # 距离系数
    global startKneadingTime
    global nowKneadingY
    global nowKneadingX
    global handIntime

    tool.hand_landmarks = hand_landmarks
    tool.mp_hands = mp_hands

    # 数据及手势判定更新
    data.UpdateData(hand_landmarks,mp_hands)
    gestureLib.UpdateGesture(hand_landmarks,mp_hands)

    # 获取当前时间戳
    handIntime = time.time()

    # 起始手势判定
    if nowStart == '':
        if not False in gestureLib.gesture_open:
            nowStart = 'open'
            # 中指指尖到原点距离计算距离系数
            fingerToOriginDistance = abs(hand_landmarks.landmark[mp_hands.HandLandmark(12).value].y - hand_landmarks.landmark[mp_hands.HandLandmark(0).value].y)
            distanceCoefficient = round(abs(hand_landmarks.landmark[mp_hands.HandLandmark(12).value].y - hand_landmarks.landmark[mp_hands.HandLandmark(0).value].y) / 0.35,4) # 距离系数
            startKneadingTime = time.time()
            print('起始手势_张开')
        elif not False in gestureLib.gesture_otherOpen:
            nowStart = 'otherOpen'
            startKneadingTime = time.time()
            print('起始手势_反向张开')
        elif not False in gestureLib.gesture_rightOpen:
            nowStart = 'rightOpen'
            startKneadingTime = time.time()
            print('起始手势_朝右张开')
        elif not False in gestureLib.gesture_leftOpen:
            nowStart = 'leftOpen'
            startKneadingTime = time.time()
            print('起始手势_朝左张开')
        elif not False in gestureLib.gesture_kneading:
            nowStart = 'kneading'
            startKneadingTime = time.time()
            nowKneadingY = tool.GetFingerAverage((0,1),'y')
            print('起始手势_朝左捏合')
        elif not False in gestureLib.gesture_kneadingOn:
            nowStart = 'kneadingOn'
            startKneadingTime = time.time()
            nowKneadingX = tool.GetFingerAverage((0,1),'x')
            nowKneadingY = tool.GetFingerAverage((0,1),'y')
            print('起始手势_朝上捏合')
        elif not False in gestureLib.gesture_together:
            nowStart = 'together'
            startKneadingTime = time.time()
            nowKneadingX = tool.GetFingerAverage((0,1),'x')
            nowKneadingY = tool.GetFingerAverage((0,1),'y')
            print('起始手势_朝上并拢')
        elif not False in gestureLib.gesture_middle:
            pyautogui.typewrite('cnmd')
        else:
            nowStart = ''

    # 后续手势判断
    if nowStart == 'open': # open起始手势的后续手势
        if not False in gestureLib.gesture_fist:
            nowStart = ''
            print('起始手势_张开_后续手势_握拳')
            im = pyautogui.screenshot()
            im.save('xx.png')
        elif not False in gestureLib.gesture_otherOpen:
            nowStart = ''
            print('起始手势_张开_后续手势_下滑')
            pyautogui.scroll(500)
    
    if nowStart == 'otherOpen': # otherOpen起始手势的后续手势
        if not False in gestureLib.gesture_open:
            nowStart = ''
            print('起始手势_反向张开_后续手势_上滑')
            pyautogui.scroll(-500)

    if nowStart == 'leftOpen': # leftOpen起始手势的后续手势
        if not False in gestureLib.gesture_rightOpen:
            nowStart = ''
            print('起始手势_向左张开_后续手势_右滑')
            pyautogui.press('left')

    if nowStart == 'rightOpen': # rightOpen起始手势的后续手势
        if not False in gestureLib.gesture_leftOpen:
            nowStart = ''
            print('起始手势_向右张开_后续手势_左滑')
            pyautogui.press('right')
    
    if nowStart == 'kneading': # kneading起始手势的后续手势
        if not False in gestureLib.gesture_kneading:
            if time.time() - startKneadingTime >= 0.1:
                if tool.GetFingerAverage((0,1),'y') - nowKneadingY >= 0.01:
                    startKneadingTime = time.time()
                    print('起始手势_朝左捏合_后续手势_捏合下滑')
                    pyautogui.press('volumedown')
                if tool.GetFingerAverage((0,1),'y') - nowKneadingY <= -0.01:
                    startKneadingTime = time.time()
                    print('起始手势_朝左捏合_后续手势_捏合上滑')
                    pyautogui.press('volumeup') 
                nowKneadingY = tool.GetFingerAverage((0,1),'y')

    if nowStart == 'kneadingOn': # kneadingOn起始手势的后续手势
        if not False in gestureLib.gesture_kneadingOn:
            if time.time() - startKneadingTime >= 0.1:

                if tool.GetFingerAverage((0,1),'x') - nowKneadingX >= 0.01:
                    startKneadingTime = time.time()
                    print('起始手势_朝上捏合_后续手势_捏合右滑')
                    pyautogui.press('right')

                if tool.GetFingerAverage((0,1),'x') - nowKneadingX <= -0.01:
                    startKneadingTime = time.time()
                    print('起始手势_朝上捏合_后续手势_捏合左滑')
                    pyautogui.press('left') 

                nowKneadingX = tool.GetFingerAverage((0,1),'x')

    if nowStart == 'together': # together起始手势的后续手势
        if not False in gestureLib.gesture_together:
            if time.time() - startKneadingTime >= 0:

                # if tool.GetFingerAverage((0,1),'x') - nowKneadingX >= 0.01:
                #     startKneadingTime = time.time()
                #     print('起始手势_朝上捏合_后续手势_捏合右滑')
                #     pyautogui.press('right')

                # if tool.GetFingerAverage((0,1),'x') - nowKneadingX <= -0.01:
                #     startKneadingTime = time.time()
                #     print('起始手势_朝上捏合_后续手势_捏合左滑')
                #     pyautogui.press('left') 

                moveData = tool.GetChangeCoordinateForScreen((tool.GetFingerAverage((1,2),'x') - nowKneadingX) * 1.5, (tool.GetFingerAverage((1,2),'y') - nowKneadingY) * 1.5)

                pyautogui.moveRel(moveData[0],moveData[1],duration=0.1)

                nowKneadingX = tool.GetFingerAverage((1,2),'x')
                nowKneadingY = tool.GetFingerAverage((1,2),'y')

    #print(gesture_fist,((-0.3 * distanceCoefficient),fingerOriginDiffAverage_y),((0.07 * distanceCoefficient),fingerDiffAverage_x))
    #print(distanceCoefficient,fingerOriginDiffAverage_y, fingerDiffAverage_x,fingerDiffAverage_y, fingerAverage_z,fingerToOriginDistance)
    #print(fingerOriginDiffAverage_x,fingerDiffAverage_x,fingerDiffAverage_y)
    #print((f0f1diff_x,f0f1diff_y),(f2f3f4Average_x,f2f3f4Average_y))
    #print((f0f1diff_x,f0f1diff_y))
    #print(gesture_kneading,f2f3f4Average_y,tool.GetFingerAverage((0,1),'y'))
    #print(nowKneadingY)
    #print(abs(tool.GetFingerAverage((0,1),'x') - f2f3f4Average_x - originX),f0f1diff_y,gesture_kneadingOn)
    #print(tool.GetFingerAverage((0,1),'x') - nowKneadingX)
    #print(gesture_together,abs(tool.GetFingerAverage((1,1),'x') - tool.GetFingerJointAverage((1,1),'x')),abs(tool.GetFingerAverage((2,2),'x') - tool.GetFingerJointAverage((2,2),'x')))



