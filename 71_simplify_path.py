class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        state_map = {
            '/': {
                'filename': 'filename',
                '.': '.',
                '/': '/'
            },
            'filename' : {
                'filename': 'filename',
                '.': 'filename',
                '/': '/', # push stack
            },
            '.': {
                'filename': 'filename',
                '.': '..',
                '/': '/',
            },
            '..': {
                'filename': 'filename',
                '.': 'filename',
                '/': '/' # pop stack
            }
        }
        if path[-1] != '/': path += '/'
        stack = []
        state = '/'
        filename_str = ''
        for c in path:
            input_case = 'filename'
            if c == '.':
                input_case = '.'
            elif c == '/':
                input_case = '/'
            print state, input_case, stack, filename_str

            if state == '/':
                filename_str = ''

            if input_case in ['filename', '.']:
                filename_str += c

            # push
            if state == 'filename' and  input_case == '/':
                stack.append(filename_str)

            # pop
            if state == '..' and  input_case == '/':
                if stack: stack.pop()

            state = state_map[state][input_case]

        result = "/" + '/'.join(stack)
        return result
if __name__ == "__main__":
    print Solution().simplifyPath("/a//b////c/d//././/..")