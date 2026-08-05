SEPERATOR = '🤣'
EMPTY = '😭'
def replace(input_list, from_val, to_val):
    input_list.append(from_val)
    from_index = input_list.index(from_val)
    while from_index != len(input_list) - 1:
        input_list[from_index] = to_val
        from_index = input_list.index(from_val, from_index)
    input_list.pop()

class Solution:

    def encode(self, strs: List[str]) -> str:
        replace(strs, "", EMPTY)
        return SEPERATOR.join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) < 1:
            return []
        final_list = s.split(SEPERATOR)
        replace(final_list, EMPTY, "")

        return final_list