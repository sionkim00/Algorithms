                        factor_index[f] = i
                    while n % f == 0:
                        n = n // f
            if n > 1:
                if n in factor_index:
                    uf.union(i, factor_index[n])
                f += 1
                else:
                    factor_index[n] = i
        return uf.count == 1
[
