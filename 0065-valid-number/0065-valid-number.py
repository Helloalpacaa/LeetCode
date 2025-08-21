class Solution:
    def isNumber(self, s: str) -> bool:
        # [optional sign] (integer or decimal) [optional exponent (e|E + signed integer)]
        seen_digit, seen_dot, seen_exp, seen_digit_after_exp = False, False, False, True

        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
                if seen_exp:
                    seen_digit_after_exp = True

            elif char in ['+', '-']:
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False
            
            elif char == '.':
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            
            elif char in ['e', 'E']:
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit_after_exp = False
            
            else:
                return False
        
        if seen_exp and not seen_digit_after_exp:
            return False
        
        return seen_digit