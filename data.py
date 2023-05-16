import tool

'''
执行基础所需数据的计算等工作
'''

def UpdateData(hand_landmarks,mp_hands):

    #region 全局变量声明

    # 五指指头x
    global finger_x
    # 五指指头y
    global finger_y
    # 五指指头x与原点差值
    global fingerOriginDiff_x
    # 五指指头y与原点差值
    global fingerOriginDiff_y
    global finger_z
    # 五指关节y
    global fingerJoint_y
    # 五指关节x
    global fingerJoint_x


    # 计算五指间差
    global fingerDiff_x
    global fingerDiff_y
    global fingerDiff_z

    # 计算五指均差
    global fingerDiffAverage_x
    global fingerDiffAverage_y
    # 计算五指至原点均差
    global fingerOriginDiffAverage_x
    global fingerOriginDiffAverage_y

    # 计算五指指头坐标均值
    global fingerAverage_x
    global fingerAverage_y
    global fingerAverage_z

    # 计算五指关节均值
    global fingerJointAverage_y
    global fingerJointAverage_x

    # 食指与拇指轴差及
    global f0f1diff_y
    global f0f1diff_x

    # 中指无名指小指平均坐标
    global f2f3f4Average_x
    global f2f3f4Average_y 

    # 原点坐标
    global originX
    global originY

    #endregion

    # 五指指头x
    finger_x = [
        hand_landmarks.landmark[mp_hands.HandLandmark(4).value].x,
        hand_landmarks.landmark[mp_hands.HandLandmark(8).value].x,
        hand_landmarks.landmark[mp_hands.HandLandmark(12).value].x,
        hand_landmarks.landmark[mp_hands.HandLandmark(16).value].x,
        hand_landmarks.landmark[mp_hands.HandLandmark(20).value].x,
    ]
    # 五指指头y
    finger_y = [
        hand_landmarks.landmark[mp_hands.HandLandmark(4).value].y,
        hand_landmarks.landmark[mp_hands.HandLandmark(8).value].y,
        hand_landmarks.landmark[mp_hands.HandLandmark(12).value].y,
        hand_landmarks.landmark[mp_hands.HandLandmark(16).value].y,
        hand_landmarks.landmark[mp_hands.HandLandmark(20).value].y,
    ]
    # 五指指头x与原点差值
    fingerOriginDiff_x = [
        hand_landmarks.landmark[mp_hands.HandLandmark(4).value].x - hand_landmarks.landmark[mp_hands.HandLandmark(0).value].x,
        hand_landmarks.landmark[mp_hands.HandLandmark(8).value].x - hand_landmarks.landmark[mp_hands.HandLandmark(0).value].x,
        hand_landmarks.landmark[mp_hands.HandLandmark(12).value].x - hand_landmarks.landmark[mp_hands.HandLandmark(0).value].x,
        hand_landmarks.landmark[mp_hands.HandLandmark(16).value].x - hand_landmarks.landmark[mp_hands.HandLandmark(0).value].x,
        hand_landmarks.landmark[mp_hands.HandLandmark(20).value].x - hand_landmarks.landmark[mp_hands.HandLandmark(0).value].x,
    ]
    # 五指指头y与原点差值
    fingerOriginDiff_y = [
        hand_landmarks.landmark[mp_hands.HandLandmark(4).value].y - hand_landmarks.landmark[mp_hands.HandLandmark(0).value].y,
        hand_landmarks.landmark[mp_hands.HandLandmark(8).value].y - hand_landmarks.landmark[mp_hands.HandLandmark(0).value].y,
        hand_landmarks.landmark[mp_hands.HandLandmark(12).value].y - hand_landmarks.landmark[mp_hands.HandLandmark(0).value].y,
        hand_landmarks.landmark[mp_hands.HandLandmark(16).value].y - hand_landmarks.landmark[mp_hands.HandLandmark(0).value].y,
        hand_landmarks.landmark[mp_hands.HandLandmark(20).value].y - hand_landmarks.landmark[mp_hands.HandLandmark(0).value].y,
    ]

    finger_z = [
        hand_landmarks.landmark[mp_hands.HandLandmark(4).value].z,
        hand_landmarks.landmark[mp_hands.HandLandmark(8).value].z,
        hand_landmarks.landmark[mp_hands.HandLandmark(12).value].z,
        hand_landmarks.landmark[mp_hands.HandLandmark(16).value].z,
        hand_landmarks.landmark[mp_hands.HandLandmark(20).value].z,
    ]
    # 五指关节y
    fingerJoint_y = [
        hand_landmarks.landmark[mp_hands.HandLandmark(3).value].y,
        hand_landmarks.landmark[mp_hands.HandLandmark(6).value].y,
        hand_landmarks.landmark[mp_hands.HandLandmark(10).value].y,
        hand_landmarks.landmark[mp_hands.HandLandmark(14).value].y,
        hand_landmarks.landmark[mp_hands.HandLandmark(18).value].y,
    ]
    # 五指关节x
    fingerJoint_x = [
        hand_landmarks.landmark[mp_hands.HandLandmark(3).value].x,
        hand_landmarks.landmark[mp_hands.HandLandmark(6).value].x,
        hand_landmarks.landmark[mp_hands.HandLandmark(10).value].x,
        hand_landmarks.landmark[mp_hands.HandLandmark(14).value].x,
        hand_landmarks.landmark[mp_hands.HandLandmark(18).value].x,
    ]

    #region 基础所需数据计算

    # 计算五指间差
    fingerDiff_x = []
    fingerDiff_y = []
    fingerDiff_z = []
    for i in range(5):
        for j in range(5):
            if i == j:
                continue
            fingerDiff_x.append(abs(finger_x[i] - finger_x[j]))
            fingerDiff_y.append(abs(finger_y[i] - finger_y[j]))
            fingerDiff_z.append(abs(finger_z[i] - finger_z[j]))

    # 计算五指均差
    fingerDiffAverage_x = sum(fingerDiff_x) / len(fingerDiff_x)
    fingerDiffAverage_y = sum(fingerDiff_y) / len(fingerDiff_y)

    # 计算五指至原点均差
    fingerOriginDiffAverage_x = sum(fingerOriginDiff_x) / len(fingerOriginDiff_x)
    fingerOriginDiffAverage_y = sum(fingerOriginDiff_y) / len(fingerOriginDiff_y)

    # 计算五指指头坐标均值
    fingerAverage_x = sum(finger_x) / len(finger_x)
    fingerAverage_y = sum(finger_y) / len(finger_y)
    fingerAverage_z = sum(finger_z) / len(finger_z)

    # 计算五指关节均值
    fingerJointAverage_y = sum(fingerJoint_y) / len(fingerJoint_y)
    fingerJointAverage_x = sum(fingerJoint_x) / len(fingerJoint_x)

    # 食指与拇指轴差
    f0f1diff_y = abs(hand_landmarks.landmark[mp_hands.HandLandmark(4).value].y - hand_landmarks.landmark[mp_hands.HandLandmark(8).value].y)
    f0f1diff_x = abs(hand_landmarks.landmark[mp_hands.HandLandmark(4).value].x - hand_landmarks.landmark[mp_hands.HandLandmark(8).value].x)

    # 中指无名指小指平均坐标
    f2f3f4Average_x = tool.GetFingerAverage((2,3,4),'x')
    f2f3f4Average_y = tool.GetFingerAverage((2,3,4),'y')

    # 原点坐标
    originX = hand_landmarks.landmark[mp_hands.HandLandmark(0).value].x
    originY = hand_landmarks.landmark[mp_hands.HandLandmark(0).value].y

    #endregion