import os
res = {
    # 此处省略数千行
    "reptile": "reptile.md",
    "republic": "republic.md",
    "repulsive": "repulsive.md",
    "reputation": "reputation.md",
    "request": "request.md",
    "request": "request.md",
    "require": "require.md",
    # 此处省略数千行
}

def main():
    path = r"D:\Desktop\weici\docs\3"
    for i in os.listdir(path):
        if i=="README.md":
            continue
        f = open(os.path.join(path, i, "README.md"), "w")
        f.write(f"* {i}{i.lower()}\n\n")
        for j in os.listdir(os.path.join(path, i)):
            if j=="_sidebar.md" or j=="README.md":
                continue
            f.write("* ["+list(res.keys())[list(res.values()).index(j)]+"]")
            f.write(f"(3/{i}/{j})\n\n")
        f.close()

main()