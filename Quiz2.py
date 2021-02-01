# Quiz2) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

# ex)http://naver.com

#         조건1 : http:// 부분은 제외 => naver.com
#         조건2 : 처음 만나는 점(.) 이 후 부분은 제외 => naver
#         조건3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                             (nav)     (5)         (1)          (!)
#         ex) 생성 비밀번호 : nav51!

naver = "http://naver.com"
google = "http://google.com"

my_str = naver.replace("http://","") #조건 1
print(my_str)

my_str = my_str[:my_str.index(".")] #조건 2 my_str[0:5]
print(my_str)

my_str2 = google.replace("http://","") #조건 1
print(my_str2)

my_str2 = my_str2[:my_str2.index(".")] #조건 2 my_str[0:5]
print(my_str2)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
password2 = my_str2[:3] + str(len(my_str2)) + str(my_str2.count("e")) + "!"

print(password)
print("{0}의 비밀번호는 {1} 입니다.".format(naver, password))
print("{0}의 비밀번호는 {1} 입니다.".format(google, password2))
