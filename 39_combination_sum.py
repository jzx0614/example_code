class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        output = []
        def find_element(e_list, candidates_idx, target):
            if target == 0:
                print e_list, target, candidates_idx
                output.append(e_list[:])
                return True
            for num in candidates[candidates_idx:]:
                if target >= num:
                    e_list.append(num)
                    find_element(e_list, candidates_idx, target - num)
                    e_list.pop()
                    candidates_idx += 1

            return False

        find_element([], 0, target)
        return output

if __name__ == "__main__":    
    print Solution().combinationSum([8,2,6,3], 13)
