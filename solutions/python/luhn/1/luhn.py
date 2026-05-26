class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        if not self.card_num:
            return False
        self.card_num = self.card_num.replace(' ', '')
        if len(self.card_num) < 2:
            return False
        if not self.card_num.isdigit():
            return False
        nums = []
        for i, num in enumerate(self.card_num[::-1]):
            if i % 2:
                num = int(num) * 2
                nums.append(num - 9 if num > 9 else num)
            else:
                nums.append(int(num))
        return sum(nums) % 10 == 0


if __name__ == '__main__':
    print(Luhn('091').valid())
