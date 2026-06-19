class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write  = 0
        while read < len(chars):
            current_chars = chars[read]
            count = 0
            while read < len(chars) and chars[read] == current_chars:
                read += 1
                count += 1
            chars[write] = current_chars
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
     
        return write
