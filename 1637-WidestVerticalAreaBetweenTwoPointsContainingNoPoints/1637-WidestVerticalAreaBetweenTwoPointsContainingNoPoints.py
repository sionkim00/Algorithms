        for x, y in points:
            xpoints.append(x)

        xpoints.sort()
        
        maxDif = 0

        for i in range(1, len(xpoints)):
            maxDif = max(maxDif, xpoints[i] - xpoints[i-1])
        return maxDif
[
