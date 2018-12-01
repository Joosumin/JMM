from collections

loc = input("위치 입력:") #받은 주소
m_type = input("음식종류 입력:") #고른 음식 종류
store = input("맛집 입력:") #고른 맛집
dic = {'주소 ':loc, '음식 종류: ':m_type, '맛집: ':store}

print(dic)
print(collections.Counter(dic))
