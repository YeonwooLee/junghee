import json
import pathlib
import requests
import traceback
import gui_tool


def print_trace_back():
    msg = traceback.format_exc()
    print("\033[31m>>>>>>>>>>>>>\n" + msg + "\n<<<<<<<<<<<<<<<\033[0m")
    return msg
# 아래 두 함수 load_json과 write_json은 딕셔너리, 리스트 같은 것들을 그 자체로 저장하고 읽을 수 있습니다.
# 가령 dict_a={}를 텍스트'dict_a={}'가 아닌 dict_a={} 그 자체로 저장하고 읽을 수 있습니다.
# 이걸 쓰면 큰 데이터들을 미리 모아두고 코드에서 읽어서 바로 딕셔너리로 사용할 수 있습니다

def load_json(filename):
    file = pathlib.Path(str(filename) + '.json')
    file_text = file.read_text(encoding='utf-8-sig')
    #file.__exit__()
    return json.loads(file_text)


def write_json(filename, data):
    with open(str(filename) + '.json', 'w', encoding='UTF-8-sig') as file:
        file.write(json.dumps(data, ensure_ascii=False))

#url에 요청보냄, 응답을 json 형태로 반환
def url_to_json(url):
    return requests.get(url).json()

#문자열에 들어있는 따옴표 큰따옴표 제거
def del_quote(string):
    string = str(string)
    return string.replace('\'','').replace('\"','')
def main():
    raise gui_tool.noErrorException
if __name__ == "__main__":
    try:
        main()
    except gui_tool.noErrorException as e:
        print("에러메세지")
        print(e.__str__())
        k = print_trace_back()

        print("입니다")
        print(k)
        print("sdfsdf")