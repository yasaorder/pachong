# pachong
爬虫工具

## Selenium_tiku
应付考试的爬虫，可以爬答题网站的题库，最后生成一个docx文档，方便答题的时候进行查找
### 使用方法
打开cmd，输入以下代码：
```python
cd C:\Program Files\Google\Chrome\Application
C:\Program Files\Google\Chrome\Application>chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"
```
参数解释：
--remote --debugging - port值，可以指定任何打开的端口。
--user-data-dir标记，指定创建新Chrome配置文件的目录。它是为了确保在单独的配置文件中启动chrome，不会污染你的默认配置文件。
PS: user-data-dir 如果是其他盘或者c 盘一些需要管理员权限的文件，chrome 会报错，无法对其进行读写操作, 所以选择直接在c盘下自动创建selenium等文件夹，比较方便点

然后用打开的浏览器登录想爬的答题网站，登录，转到答题页面，根据页面的内容开始爬题
