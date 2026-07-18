class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        """
        temp add a sorted version of the word and create a list and add them all in list form to the dict


        """

        my_dict = {}
        
        for s in strs:
            if str(sorted(s)) in my_dict:
                my_dict[str(sorted(s))].append(s)
            else:
                my_dict[str(sorted(s))] = [s]

        result = []
        for key in my_dict:
            result.append(my_dict[key])
        return result
