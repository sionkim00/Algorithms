        for c in word1:
            str1[ord(c) - ord('a')] += 1
        
        for c in word2:
            str2[ord(c) - ord('a')] += 1
        
        for i in range(26):
            if (str1[i] == 0 and str2[i] != 0) or (str1[i] != 0 and str2[i] == 0):
                return False
        
        str1.sort()
        str2.sort()

        for i in range(26):
            if str1[i] != str2[i]:
                return False
        return True
"
