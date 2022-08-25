#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
name_def = dir(hidden_4)
for i in range(len(name_def)):
    if(name_def[i][:2] != '__'):
        print(name_def[i])
