def solution(new_id):
    # 1단계 소문자 변경
    new_id = new_id.lower()

    # 2단계 !,@,#,* 제거
    for i in new_id:
        if not (i.islower() or i.isdigit() or i in {"-","_","."}):
            new_id = new_id.replace(i,"")

    # 3단계 .. 제거
    while '..' in new_id:
        new_id = new_id.replace("..",".")

    # 4단계 앞, 뒤 . 제거
    new_id = new_id.strip(".")

    # 5단계 빈 문자열 확인
    if new_id == '':
        new_id = "a"

    # 6단계 15자 초과 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[14] == ".":
            new_id = new_id[:-1]

    # 7단계 3 미만 추가
    while len(new_id) < 3:
        plus = new_id[-1]
        new_id+=plus

    return new_id