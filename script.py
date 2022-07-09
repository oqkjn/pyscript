import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://github.com/oqkjn" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["red", "blue"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "소현")
write("description", "16살")
write("button", "버튼")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "좋아하는 과목": "수학,과학,사회,음악,미술,체육",
  "좋아하는 음식": "아이스크림,고기,젤리",
  "소속 학교": "효성중학교",
  "생일": "2007 03 02"
}
information(informations)