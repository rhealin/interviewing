def matched(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0

## works if checking for multiple types of parentheses
def parentheses_match(input):
  stack = []
  push_chars, pop_chars = "<({[", ">)}]"
  for c in input:
    if c in push_chars:
      stack.append(c)
    elif c in pop_chars:
      if not len(stack):
        return False
      else:
        stack_top = stack.pop()
        balancing_bracket = push_chars[pop_chars.index(c)]
        if stack_top != balancing_bracket:
          return False
    else:
      continue
  return not len(stack)