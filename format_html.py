from collections import defaultdict

formatting = {
    "b": [[0, 5]],
    "i": [[1, 3]],
}
s = "ABCDE"

def format_html(s, formatting):
    format_by_index = defaultdict(set)
    for quality in formatting:
        for arr in formatting[quality]:
            for i in range(arr[0], arr[1]):
                format_by_index[i].add(quality)
    stack = []
    html = ""
    for i in range(len(s)):
        if i > 0:
            to_remove = format_by_index[i-1] - format_by_index[i]
            while to_remove:
                quality = stack.pop()
                if quality in to_remove:
                    to_remove.remove(quality)
                html += "</{}>".format(quality)
                
        for quality in format_by_index[i]:
            if quality not in stack:
                stack.append(quality)
                html += "<{}>".format(quality)
                
        
        html += s[i]
        
    while stack:
        html += "</{}>".format(stack.pop())
                
    return html
        
    
print(format_html(s, formatting))