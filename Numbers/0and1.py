def replace_zeros_with_ones(n):
if not isinstance(n, int):
    return 0  

  s = str(n)
  new_s = s.replace('0', '1')
  return int(new_s)
