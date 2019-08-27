class FourDigitYearConverter:
    regex = r'\d{4}'
    # url로부터 추출한 문자열을 뷰에 넘겨주기 전에 변환
    def to_python(self, value):
        return int(value)
    # url reverse 시에 호출
    def to_url(self, value):
        return "%04d" % value