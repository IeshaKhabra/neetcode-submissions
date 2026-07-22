class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create dict
        my_dict = {}

        # fill the dict with count of each numbers occurance
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        buckets = [[] for _ in range(len(nums)+1)]
        for num, frequency in my_dict.items():
            buckets[frequency].append(num)

        # extract top k
        # go from highest frequency bucket to the lowest one
        # based on whatever the value of k is
        result = []
        for frequency in range(len(buckets) - 1, 0, -1):
            # add all numbers having this freq
            for num in buckets[frequency]:
                result.append(num)
                # as soon as we collected k elements 
                if len(result) == k:
                    return result 
