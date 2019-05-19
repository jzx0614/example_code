class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        output = set()
        def find_element(e_list, candidates_idx, target):
            if target == 0:
                print e_list, target, candidates_idx
                output.add(tuple(e_list))
                return True
            for num in candidates[candidates_idx:]:
                if target >= num:
                    e_list.append(num)
                    find_element(e_list, candidates_idx+1, target - num)
                    candidates_idx += 1
                    e_list.pop()

            return False

        find_element([], 0, target)
        return map(list, output)

if __name__ == "__main__":    
    print Solution().combinationSum2([10,1,2,7,6,1,5], 8)
