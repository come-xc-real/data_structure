from SqStack import SqStack

def pop_stack(st, st_out):
    if st.data:
        st_out.append(st.gettop())
        st.pop()
    return st, st_out


def push_stack(st, list_stack_else):
    if list_stack_else:
        st.push(list_stack_else[0])
    return st, list_stack_else[1:]


def makef(alist):
    for i in alist:
        if i[2] != [0, 0]:
            return True
    return False

def main_s(all_res, list_stack, fist_=True):
    if fist_:
        all_res.append([[list_stack[0]], [], [len(list_stack), len(list_stack)-1]])
        list_stack = list_stack[:]


    len_all_res = len(all_res)
    for i in range(len_all_res):
        if len(all_res[i][0]) + len(all_res[i][1]) != len(list_stack):
            for j in range(3):
                if j == 0 and all_res[i][2][0]>0:
                    st = SqStack()
                    st.push_list(all_res[i][0])
                    list_stack_else = list_stack[len(all_res[i][1]) + len(st.data):]
                    st_out = all_res[i][1][:]
                    st, list_stack_else = push_stack(st, list_stack_else)
                    all_res.append([st.data, st_out, [all_res[i][2][0], all_res[i][2][0] - 1]])
                if j == 1 and all_res[i][2][1] > 0:
                    st = SqStack()
                    st.push_list(all_res[i][0])
                    st_out = all_res[i][1][:]
                    st, st_out = pop_stack(st, st_out)
                    all_res.append([st.data, st_out, [all_res[i][2][0], all_res[i][2][1]-1]])
            all_res.remove(all_res[i])

    for i in range(len(all_res)):
        if not list_stack[len(all_res[i][1]) + len(all_res[i][0]):]:
            for j in range(len(all_res[i][0])-1, -1, -1):
                all_res[i][1].append(all_res[i][0][j])
            all_res[i] = [[], all_res[i][1], [0, 0]]

    return all_res


if __name__ == '__main__':
    all_res = []
    list_stack = [1, 2, 3, 4, 5]
    res = main_s(all_res, list_stack)

    while makef(res):
        res = main_s(res, list_stack, fist_=False)
        b = []
        for i in res:
            if i not in b:
                b.append(i)
        res = b

    for i in res:
        print(i)
    print(len(res))

# for i in range(len(list_stack)):  # 第一次出栈数
#     st = SqStack()
#     st_out = []
#     st.push_list(list_stack[:i + 1])
#     list_stack_else = list_stack[i+1:]
#     st_out = pop_stack(st, st_out)                  #初始化
#
#
#
#
#     st_out = pop_stack(st, st_out)
#     list_stack_else = push_stack(st, list_stack_else)
#
#
#
#
#     print(f"栈元素：{st.data}")
#     if not list_stack_else:
#         for out_data in st.all_out():
#             st_out.append(out_data)
#     print(f"出栈元素{st_out}")
#     print(f"剩余入栈元素：{list_stack_else}")
#     print("++++++++++++++++++++++++++++++++++++++++")
