class PhoneNumber:
    def __init__(self, number):
        self.country_code = 1
        self.area_code = None
        self.exchange_code = None
        self.user_code = None
        self.number = None
        self.handle(number)

    def handle(self, number):
        number = number.replace(' ', '').replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace('.', '')
        for char in number:
            if not str.isdigit(char):
                if str.isalpha(char):
                    raise ValueError("letters not permitted")
                else:
                    raise ValueError("punctuations not permitted")
        if len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(number) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(number) == 11:
            if number[0] != '1':
                raise ValueError("11 digits must start with 1")
            number = number[1:]
        if number[0] == '0':
            raise ValueError("area code cannot start with zero")
        if number[0] == '1':
            raise ValueError("area code cannot start with one")
        if number[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        if number[3] == '1':
            raise ValueError("exchange code cannot start with one")
        self.number = number
        self.area_code = number[:3]
        self.exchange_code = number[3:6]
        self.user_code = number[6:]

    def pretty(self):
        return f'({self.area_code})-{self.exchange_code}-{self.user_code}'


if __name__ == '__main__':
    phoneNumber = PhoneNumber('12234567890')
    print(phoneNumber.__dict__)
