def generate_tree(g):
    M = [0] * (g + 1)
    F = [0] * (g + 1)
    M[0] = 1

    tree_str = "Generational Tree:\n"
    tree_str += f"Generation 0: M = {M[0]}, F = {F[0]}\n"

    for i in range(g):
        M[i + 1] = F[i]
        F[i + 1] = M[i] + F[i]
        tree_str += f"{'    ' * (i + 1)}└── Generation {i + 1}: M = {M[i + 1]} (from F{i} = {F[i]}), F = {F[i + 1]} (from M{i} = {M[i]} + F{i} = {F[i]})\n"

    return tree_str, M, F

# Input the number of generations
g = int(input("Input the number of generations: "))
tree_str, M, F = generate_tree(g)
print(tree_str)
print(f"Total population in generation {g}: M = {M[g]}, F = {F[g]}, Total = {M[g] + F[g]}")
