


def pyramid(n):
  for i in range(1, n + 1):
    line_str = ""
    
    for j in range(1, (i + 1) // 2 + 1):
      line_str += str(j)
    
    for j in range(i // 2, 0, -1):
      line_str += str(j)
      
    print(line_str)

pyramid(5)

