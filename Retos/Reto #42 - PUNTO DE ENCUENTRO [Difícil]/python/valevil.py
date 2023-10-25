def collision(
    r: tuple[float, float],
    s: tuple[float, float],
    vr: tuple[float, float],
    vs: tuple[float, float],
):
    '''The function `collision` calculates the collision point and time between two moving objects, given
    their initial positions and velocities, and prints them to the user.
    
    Parameters
    ----------
        The parameters `r` and `s` represent the initial position of objects R and S, given as a tuple of two floats (x,y).
        
        The parameters `vr` and `vs` represent the velocity of objects R and A, where `vr[0]` is the velocity in the     x-direction and `vr[1]` is the velocity in the y-direction.
    '''

    try: # What if some coord velocities are equal or none
        t_0 = (s[0] - r[0]) / (vr[0] - vs[0])
        if t_0 < 0: # If they would collide in the past then we don't care
            print(f"Objects won't collide.")
            return
    except:
        if s[0] != r[0]: # distance between them will be constant in time
            print(f"Objects won't collide.")
            return
        t_0 = "any" # If they are in the same coord time doesn't matter
        
    try:
        t_1 = (s[1] - r[1]) / (vr[1] - vs[1])
        if t_1 < 0:
            print(f"Objects won't collide.")
            return
    except:
        if s[1] != r[1]:
            print(f"Objects won't collide.")
            return
        else: t_1 = t_0

    if t_0 == t_1 or t_0 == "any":
        if (t := t_1) == "any": # This would mean they both have the same IC
            print("The objects share their movement.")
            return
        c = (s[0] + vs[0] * t, s[1] + vs[1] * t)
        print(f"Collision at x = {c[0]}, y = {c[1]} at t = {t}.")
    else:
        print(f"Objects won't collide.")


def get_input(var: str):
    while True:
        try:
            x = float(input(f"\t- {var}: ").strip())
            return x
        except ValueError as e:
            print(f"Please, enter a number.")


def get_coord():
    x = get_input("x")
    y = get_input("y")
    vx = get_input("vx")
    vy = get_input("vy")
    return (x, y), (vx, vy)


if __name__ == "__main__":
    print("Write the initial conditions of the first object.")
    r, vr = get_coord()
    print("Write the initial conditions of the second object.")
    s, vs = get_coord()
    collision(r, s, vr, vs)
