def merge_schedule(s, e):
    result = []
    for idx in xrange(len(s)):
        result.append([s[idx], e[idx], 1])

    
    result.sort()
    stack = [result.pop(0)]
    max_value = stack[-1]
    while result:
        top_item = stack[-1]
        insert_item = result.pop(0)
        if top_item[1] < insert_item[0]:
            stack.append(insert_item)
        elif top_item[0] <= insert_item[0] <= top_item[1]:
            stack.pop()
            if top_item[0] < insert_item[0]:
                stack.append([top_item[0], insert_item[0] - 1, top_item[2]])
            stack.append([insert_item[0], min(top_item[1], insert_item[1]), top_item[2]+1])
            if max_value[2] < stack[-1][2]:
                max_value = stack[-1]
            if top_item[1] != insert_item[1]:
                right = [min(top_item[1],insert_item[1])+1, max(top_item[1], insert_item[1]), 1]
                for idx, item in enumerate(result):
                    if item[0] <= right[0] and item[1] < right[1]: 
                        result.insert(idx+1, right)
                        break
                else:
                    result.insert(0, right)
    return max_value


if __name__ == "__main__":
    print merge_schedule([1,3,4,5], [4,6,5,7])