ASCII = "ascii"
UTF_8 = "utf-8"
UTF_16 = "utf-16"

def read_file(filename, en=UTF_8):
    output = ""
    with open(filename, encoding=en) as fin:
        for line in fin:
            output += line
    return output


def write_file(filename, contents, en=UTF_8):
    with open(filename, "w", encoding=en) as fout:
        fout.write(contents)

def write_html_file(filename, content):
    with open(filename, "w") as fout:
        fout.write("<html>")
        fout.write(content)
        fout.write("</html>")

text = read_file("input.txt", UTF_8)


write_file("text_in_UTF_16.txt", text, UTF_16)

with open("code_points.txt", "w") as code_points_file:
    for char in text:
        code_point = f"U+{ord(char):04X}" 
        code_points_file.write(code_point + "\n")

html_content = ""
for char in text:
    code_point = f"&#{ord(char)};" 
    html_content += code_point

write_html_file("text_in_HTML.html", html_content)

print("Process completed. Files have been generated as required.")
