            return False

        for key in s1Counter:
            if s1Counter[key] != s2Counter[key]:
                return False

        cnt = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
        if cnt not in (0, 2):
            return False
            

        return True
"
