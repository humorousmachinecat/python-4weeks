import numpy as np
#ndarray的数据类型
#布尔类型   bool
arr1 = np.array([1,0,2,0],dtype=bool)           #bool类型非0全为ture，为0全为false
print(arr1)
#整数类型   int(带正负号)   unit（不带正负号）
arr2 = np.array([-128,0,127,0],dtype=np.int8)
print(arr2)
#浮点数     float
#复数       complex 

#各种数据类型
#int8	    整数（-128 to 127）
#int16	    整数（-32768 to 32767）
#int32	    整数（-2147483648 to 2147483647）
#int64	    整数（-9223372036854775808 to 9223372036854775807）
#uint8	    无符号整数（0 to 255）
#uint16	    无符号整数（0 to 65535）
#uint32	    无符号整数（0 to 4294967295）
#uint64	    无符号整数（0 to 18446744073709551615
#float_	    float64 类型的简写
#float16	半精度浮点数，包括：1 个符号位，5 个指数位，10 个尾数位
#float32	单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位
#float64	双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位
#complex_	complex128 类型的简写，即 128 位复数
#complex64	复数，表示双 32 位浮点数（实数部分和虚数部分）
#complex128	复数，表示双 64 位浮点数（实数部分和虚数部分）
