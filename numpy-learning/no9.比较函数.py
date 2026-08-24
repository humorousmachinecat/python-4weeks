import numpy as np

##比较  大于    小于    等于
##      逻辑与  逻辑或  逻辑非
##检查数组中是否至少有一个True元素，是否所有都为True
##自定义条件

arr1 = np.array([1,2,3,4,5,6,7,8,9])
#是否大于
print(np.greater([3,4,5,6,7],4))

#是否小于
print(np.less(arr1,4))

#是否等于
print(np.equal(arr1,4))
print(np.equal([3,4,5],[4,4,5]))

#逻辑与(1 1 = True）    逻辑非（0 = True 1 = False）    逻辑或（有1为Ture）
print(np.logical_and([1,0,0],[1,1,0]))
print(np.logical_not([1,0]))
print(np.logical_or([0,0],[1,0]))

#检查数组中是否至少有一个True元素，是否所有都为True
print(np.any([0,0,0,0,0,1]))
print(np.any([0,0,0,0,0,0]))
print(np.all([1,1,1,1,1,1]))
print(np.all([1,1,1,1,1,0]))

#自定义条件
#print(np.where(条件，符合条件，不符合条件))
print(np.where(arr1>3,arr1,0))
#自定义嵌套
score = np.random.randint(1,101,20)
print(score)
print(np.where(
    score<60,'E',np.where(
        score<70,'D',np.where(
            score<80,'C',np.where(
                score<90,'B','A'
                )
            )
        )
    )
)
#np.select(条件，返回的结果)
print(np.select([score<60,
                 (score<70)&(score>=60),
                 (score<80)&(score>=70),
                 (score<90)&(score>=70),
                 (score<=100)&(score>=90)],
                 ['E','D','C','B','A'],
                 default='non'))