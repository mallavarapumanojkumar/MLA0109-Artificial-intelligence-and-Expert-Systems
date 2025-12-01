steps = [
    (0, 0),
    (3, 0),
    (0, 3),
    (3, 3),
    (2, 4),
    (2, 0)
]

print("Step | Jug1 | Jug2")
print("------------------")
for i, (a, b) in enumerate(steps):
    print(f"{i:<4} | {a:<4} | {b:<4}")
