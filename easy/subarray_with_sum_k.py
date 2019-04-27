class SubArrayWithGivenSum:
    def __init__(self):
        self.__start = 0
        self.__end = 0

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def subarray_with_given_sum(self, number_list, required_sum):
        interim_sum = number_list[self.__start]
        size = len(number_list)
        while self.__start < size and self.__end < size:
            if interim_sum == required_sum:
                return
            if interim_sum < required_sum:
                self.__end = self.__end + 1
                if self.__end == size:
                    break
                interim_sum = interim_sum + number_list[self.__end]

            if interim_sum > required_sum:
                interim_sum = interim_sum - number_list[self.__start]
                self.__start = self.__start + 1

        self.__start = -1
        self.__end = -1


if __name__ == '__main__':
    tests = int(input())
    for i in range(tests):
        sub_array_given_sum = SubArrayWithGivenSum()
        length, required_sum = input().split()
        length = int(length)
        required_sum = int(required_sum)
        number_list = list(map(int, input().split()))
        sub_array_given_sum.subarray_with_given_sum(number_list, required_sum)
        if sub_array_given_sum.get_start() is not -1:
            print('{} {}'.format(sub_array_given_sum.get_start() + 1, sub_array_given_sum.get_end() + 1))
        else:
            print(-1)
