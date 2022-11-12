from PIL import Image
import pyocr

tools = pyocr.get_available_tools()
tool = tools[0]


# print(tools)
# print(tool.get_name())

img = Image.open("spartacamp_jp.png")
# img.show()


# txt = tool.image_to_string(img, lang="eng", builder=pyocr.builders.TextBuilder())  # 英語

txt = tool.image_to_string(img, lang="jpn", builder=pyocr.builders.TextBuilder())  # 日本語

# txt = tool.image_to_string(
#     img, lang="eng+jpn", builder=pyocr.builders.TextBuilder()
# )  # 英語+日本語

print(txt)
