def monkey_problem():
    state = {
        "monkey": "floor",
        "monkey_loc": "left",
        "box_loc": "right",
        "bananas": "reachable"
    }

    def show(action):
        print(f"Action: {action}")
        print(f"State: {state}\n")

    state["monkey_loc"] = "right"
    show("Monkey walks to the box")

    state["box_loc"] = "middle"
    state["monkey_loc"] = "middle"
    show("Monkey pushes the box to the middle")

    state["monkey"] = "box"
    show("Monkey climbs on the box")

    print("Monkey gets the bananas")

monkey_problem()
