"""Nested Comment Thread Renderer
Task: Render nested comment threads with indentation using recursion."""


def comments(lst, indent=0):
    indentation = indent * " "
    for i in lst:
        print(f"{indentation}[{i['author']}]: {i['text']}")

        if i["replies"]:
            comments(i["replies"], indent + 4)


comment_lst = eval(input("Enter comments list: "))
comments(comment_lst)
