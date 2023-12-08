# 更新：
增加一个后台播放音频文件的节点Play Sound，包括音量调节。这个节点支持多线程播放。

# ComfyUI_MSSpeech_TTS  
ComfyUI下使用的文本转语音插件。使用Microsoft speech TTS 接口将文本内容转为MP3格式的语音文件。  

![image](image/ComfyUI_MSSpeech_TTS.png)

### 插件调整项：  
**voice:** 语音种类。   
**rate：** 语音速度。默认是0，调整范围从-200到200。数字越大速度越快。  
**filename_prefix:**  文件名前缀。   

### 输出： 
MP3 File,字符串类型，其内容是语音文件地址。

## 安装方法：  
- 解压zip文件，将"ComfyUI_MSSpeech_TTS"文件夹复制到 ComfyUI\custom_nodes\
- 安装依赖包，在资源管理器ComfyUI\custom_nodes\ComfyUI_MSSpeech_TTS\ 这个位置打开cmd窗口，输入以下命令：  
```..\..\..\python_embeded\python.exe -s -m pip install -r requirements.txt```
- 重新打开ComfyUI
