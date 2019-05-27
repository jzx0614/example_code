class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        buffer = []
        word_number = 0
        output = []
        for word in words:
            if len(buffer) and len(word) + word_number + len(buffer) > maxWidth:
                if len(buffer) == 1:
                    output.append(buffer[0].ljust(maxWidth))
                else:
                    space, remind = divmod((maxWidth - word_number), len(buffer)-1)
                    for r in xrange(remind):
                        buffer[r+1] = ' ' + buffer[r+1]
                    output.append((' ' * space).join(buffer))
                buffer, word_number = [], 0
            buffer.append(word)
            word_number += len(word)

        output.append(' '.join(buffer).ljust(maxWidth))
        return output
            
if __name__ == "__main__":
    # print Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
    print Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
    # print Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)