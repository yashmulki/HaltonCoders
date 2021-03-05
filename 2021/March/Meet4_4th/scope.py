# Scope
# -------------------------------------------------------------------------------------------------
# Compared to other languages, scope is pretty simple in Python (which may be a bad thing). "Scope"
# basically refers to where "names" are visible; if a name is visible, it is "in scope." Names
# refer to, well, anything with a name: variables, functions, classes, etc. Visibility refers to
# whether or not you can access the name; if you can use a variable, call a function, etc.

# The widest scope is the *global* scope (actually, not quite; more on that later). The global 
# scope encompasses all of your code, and names defined there can be accessed anywhere (provided 
# they arent shadowed; more on this later too).

# This variable (a) is in the global scope, so you can access it from anywhere after this point.
a = 1

# This variable (b) is also in the global scope. Notice how you can access `a` because it is in the
# global scope.
b = a + 1


def a_function():
    # Inside this function is a new scope, a local scope. This scope is "narrower" than the global
    # scope, which just means you can access all the names from the global scope from this local
    # scope, but not the other way around.

    # For example, the following variable (c) can be accessed from within this specific function, 
    # but not outside it, or in another function. Notice that it is still possible to access `a` 
    # and `b`, since they are in the global scope (you can't actually assign new values to them,
    # though; more details later).
    c = a + b
    print(c)


# print(c) <- This raises an error, since `c` is only defined in the local scope of `a_function`.

# However, if you call the function, Python will "enter" the function's scope, and the names
# defined in that scope will become accessible.
a_function()

# All variables are defined in the global scope as long as they aren't in a function. Below, since
# True is true (wow!), `d` will be defined (in the global scope), but `e` won't. 
if True:
    d = 10
else:
    e = 20

print(d)
# print(e) <- This raises an error, since `e` wasn't defined.


def another_function():
    # print(c) <- This raises an error, since `c` was defined in the scope of a different function.

    # Here, we define a new variable called `d`. Notice that this is a new definition, and that we
    # aren't just assigning a new value to the global scope's `d`.
    d = 30

    # What does this do? Technically, you should be able to access names defined in the global 
    # scope from anywhere, but now there's a `d` defined in this local scope! As it turns out, if
    # something in a local scope shares a name with something in the global scope, Python will opt
    # to use the name in the most local scope (30 in this case). This is called name shadowing; we
    # say that the local `d` shadows the global `d`.
    print(d)

    # Actually, there is a way to assign to the global `d` instead of defining a new one. However,
    # doing this is heavily discouraged, so if you want to learn about it, search for "global and
    # nonlocal keywords python" online.


another_function()  # This prints 30.

# Also, note that assigning something else to the `d` in the global scope doesn't change the `d` in
# `another_function`'s scope, since they're different.
d = 40
another_function()  # This still prints 30.

# Interestingly, you can shadow built-in names too, like the `int` function. In a sense, the scope
# built-ins are in is even wider than the global scope.
f = int("123")
int = print  # This has the same effect as defining a new function, like -> def int(s): print(s)

# This prints 123 since we defined our own `int` as `print`.
int("123")

# There's actually some stuff that wasn't covered here, like enclosed scopes. You probably won't
# need to know how those work specifically (they're very similar to the local function scopes we
# discussed), and if you do it should be easy enough to figure out or look up.
