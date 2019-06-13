def firstOccurrence(s, p):
    def is_match(s, p):
        if not s and not p:
            return True

        if not p:
            return True
        
        if not s:
            return False

        if s[0] == p[0] or p[0] == '*':
            return is_match(s[1:], p[1:])

    for idx in xrange(len(s)):
        if is_match(s[idx:], p):
            return idx
    return -1

def lastStoneWeight(a):
    a_map = {}
    for value in a:
        a_map[value] = a_map.get(value, 0) + 1

    result = [item[0] for item in a_map.iteritems() if item[1] % 2 ==1 ]
    
    while len(result) > 1:
        v1, v2 = result.pop(), result.pop()
        value = v1 - v2
        if value:
            result.append(value)
            result.sort()
    
    return result[0] if result else 0
    
#     while a_map:
#         max_value = max(a_map.keys())
#         if len(a_map) == 1:
#             return max_value if a_map[max_value] % 2 == 1 else 0

#         if a_map[max_value] % 2 == 0:
#             del a_map[max_value]
#             continue
#         del a_map[max_value]

#         second_value = max(a_map.keys())
#         a_map[second_value] -= 1
#         if a_map[second_value] == 0:
#             del a_map[second_value]

#         r = max_value - second_value
#         a_map[r] = a_map.get(r, 0) + 1


def investment(s, e):
    result = []
    for idx in xrange(len(s)):
        result.append([s[idx], e[idx], 1])

    result.sort()
    stack = [result.pop(0)]
    max_value = stack[-1]
    while result:
        top = stack[-1]
        cur = result.pop(0)

        if top[1] < cur[0]:
            stack.append(cur)
        elif top[0] <= cur[0] <= top[1]:
            stack.pop()
            if top[0] != cur[0]:
                stack.append([top[0], cur[0]-1, top[2]])
            stack.append([cur[0], min(cur[1], top[1]), top[2] + 1 ])

            if max_value[2] < stack[-1][2]:
                max_value = stack[-1]
            if cur[1] != top[1]:
                right =  [min(cur[1], top[1]) + 1 , max(cur[1], top[1]), 1]
                for idx, item in enumerate(result):
                    if right[0] < item[0]  or \
                       (item[0] == right[0] and right[1] <= item[1]):
                        result.insert(idx, right)
                        break
                else:
                    result.append(right)

    return max_value

if __name__ == "__main__":
    print lastStoneWeight([2, 4, 5])
    print lastStoneWeight([1, 2, 3, 4, 5, 6, 7, 8])

    # print lastStoneWeight([1, 2, 3, 6, 7, 7])
    # print firstOccurrence('xabcdey','ab*de')
    # print investment([1,2,3,3,3], [2,2,3,4,4])
    # print investment([1,2,1,2,2], [3,2,1,3,3])
