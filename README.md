# Service-switch
hoshino服务层开关（伪）,基于hoshinov2的priv魔改，依GPL-3.0进行开源<br>
`priv.py`基于hoshinov2自带的`priv.py`修改<br>
`switch.py`参考了别人写的一个拉黑插件中提取msg中时间部分的代码（但是我找不到那个项目了，暂时无法列出链接。。。）
## 原理
获得指令后主动拉黑该群聊，以达到“关闭”hoshinobot服务的功能，**实际上并没有关，只是不响应了而已**。
## 部署
1. 下载源码
2. 将`priv.py`替换hoshino原生`priv.py`
3. 将`switch.py`放入`botmanage`文件夹中
4. 重启hoshino
## 使用
@Bot或点名Bot+休息+休息的时间（分钟，分，小时，天）<br>
**例：**<br>
`可萝仔休息`  Bot会默认拉黑本群8小时<br>
`可萝仔休息5分钟`  Bot会拉黑本群5分钟<br>
`可萝仔醒醒`  Bot会提前解除拉黑，恢复在本群的响应<br>
***更多操作见代码***
