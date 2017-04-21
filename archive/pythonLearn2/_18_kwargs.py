"""18 **kwargs"""
def my_keyword_argument_function(**kwargs):
    if kwargs["name"] == "tyler hardy":
        kwargs["name"] = "Tyler Verl Hardy"
    print(kwargs)
    print(type(kwargs))

my_keyword_argument_function(name="tyler hardy", height="6", weight="240")

