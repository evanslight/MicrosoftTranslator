这个调用的核心不是Bing Translator，Google Translator，Youdao Translator，iciba Translator， Baidu Translator.

最近接到了翻译任务，由于翻译繁多，所以打算自动化操作一下
用了很多其他工具，都不太好用，目前微软Azure推出的翻译工具对比来看是最好的了。
翻译中容易出问题的是不清楚如何request。我相信我的代码能够提供一些帮助

这个API也有语言检测（language detect）功能，我把那个注释掉了。

总体而言翻译效果还行，以句子为单位，准确率在85%到90%。但翻译效果不如微软自家的bing翻译，不知道是为什么。


Reference:
https://github.com/evanslight/Text-Translation-API-V3-Python
https://github.com/TheEibwen/RawMangaTranslator
https://docs.microsoft.com/en-us/azure/cognitive-services/translator/quickstart-python-detect
