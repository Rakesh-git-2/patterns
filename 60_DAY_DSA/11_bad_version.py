class BadVersion:

    call_count = 0

    def __bad_version(self,x) :
        self.call_count += 1
        if x>50:
            return True
        return False

    def find_bad(self,input):
        left = 0
        right = len(input)

        while left < right :
            print(left,right)
            center = (left + right )// 2
            print(center)
            if self.__bad_version(input[center]):
                print("executing if")
                if not self.__bad_version(input[center-1]):
                    return input[center]
                right = center
            else :
                print("executing else")
                left = center

        return False



bad_version = BadVersion()

input = [1,24,50,52,66,77]

print(bad_version.find_bad(input))