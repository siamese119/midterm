import random #랜덤함수

ttrs_array = [[0]*7]*10 #7*10의 테트리스판 생성
def print_ttrs(): #2중리스트를 따로 출력하면 문제가 없으나 함수로 출력하면 1줄로 나타남 ㅠ
    for i in ttrs_array :
        for j in i :
            print(j,end=" ")
    print()

#딕셔너리 사용
dect_ttrs = {"rule" : "테트리스의 기본적인 룰은 줄 한 칸을 테트리미노로 가득채우면 사라지는 방식입니다. 원래의 테트리스는 대전형식이 아니었으나, 테트리스가 대전형태를 가지게 되면서 상대보다 더 빨리 줄을 지우는 것이 목적이 되었습니다"}
block_li=["ㄱ","ㄴ","T","ㅣ","ㅁ"]
start_num=True
play_num=True
choicelist = random.choice(block_li)
print("테트리스게임에 오신것을 환영합니다.")
while(start_num):
    print("1.게임 시작 2.설명 3.게임종료")
    number = input("숫자를 입력하세요 : ")
    if number == '1' :
        print("게임을 시작합니다.")
        print("테트리스를 시작")
        while(play_num):
            print_ttrs()
            print("현재 블럭 : ")
            print(choicelist)
            print("1.오른쪽 1칸 이동 2.왼쪽 1칸 이동 3.블록 돌리기 4.블록 내리기")
            number = input("숫자를 입력하세요 : ")
            print("당신이 입력한 숫자 : ", number)
            if number == '1' :
                print("오른쪽으로 1칸 이동")
            elif number == '2':
                print("왼쪽으로 1칸 이동")
            elif number == '3':
                print("블록돌리기")
            elif number == '4':
                print("블록내리기")
                break
    
    if number =='2' :
        print(dect_ttrs["rule"])

    if number == '3' :
        start_num == False
        break