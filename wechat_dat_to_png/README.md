# 思路
- 微信用户名\FileStorage\Image 里面保存的应该是图片，但是后缀名是dat，修改文件后缀名之后打开图片失败
- png 文件头为0xFFD8
- 观察dat 文件，发现大家的文件头都一样，但不是0xFFD8，那么应该存在一种映射关系，经测试，应该是文件头^魔术 = 0xFFD8


# 参考
> https://juejin.im/post/5c9cbf7c5188252d52560151