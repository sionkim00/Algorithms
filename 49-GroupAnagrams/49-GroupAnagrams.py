            # Convert the Counter object to a tuple so it can be used as a key in the defaultdict
            count = Counter(word)
        for word in strs:
        kvp = defaultdict(list)
            kvp[tuple(sorted(count.items()))].append(word)
        return list(kvp.values())
[
