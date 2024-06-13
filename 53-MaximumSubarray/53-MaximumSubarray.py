class�Solution:
����def�maxSubArray(self,�nums:�List[int])�->�int:
��������maxSum�=�float(-inf)
��������curSum�=�0

��������for�num�in�nums:
������������curSum�=�max(0,�curSum)�+�num
������������maxSum�=�max(maxSum,�curSum)

��������return�maxSum
[
