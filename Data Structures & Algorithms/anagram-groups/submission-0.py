class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Check if anagram: sorted(strs[0]) == sorted(strs[1]):
        '''buckets = {}
        for s in strs:
            length = len(s)
            buckets.setdefault(length,[]).append(s)
        result = list()
        for key in buckets.items():
            print(buckets[key[0]])
        return list(list())'''
        result = list()
        seen =set()
        for i in range(len(strs)):
            if strs[i] in seen:
                continue
            
            sub_list = list()
            sub_list.append(strs[i])
            
            for j in range(i+1,len(strs) ):
                
                if sorted(strs[i]) == sorted(strs[j]):
                    
                    sub_list.append(strs[j])
                    seen.add(strs[j])
            
            result.append(sub_list)

        return result