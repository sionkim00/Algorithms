                if j == 0:
                    if evenNode and nodes[i][j] % 2 != 0:
                        return False
                    if not evenNode and (nodes[i][j-1] % 2 == 0):
                        return False
                    continue
                if evenNode and not(nodes[i][j-1] > nodes[i][j]):
                    return False
                if evenNode and (nodes[i][j-1] % 2 != 0 or nodes[i][j] % 2 != 0):
                    return False
                if not evenNode and not(nodes[i][j-1] < nodes[i][j]):
                    return False
                if not evenNode and (nodes[i][j-1] % 2 == 0 or nodes[i][j] % 2) == 0:
                    return False
[
