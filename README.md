# Duplicate-File-Handler-JetBrains-Academy
This project jetbrains academy https://hyperskill.org/projects/176

## Work on project. Stage 1/4: Here come the files
### Objectives
In this stage, your program should:

1. Accept a command-line argument that is a root directory with files and folders. 
Print ```Directory is not specified``` if there is no command-line argument;
2. Iterate over folders and print file names with their paths. The direction of the slashes in the printed out paths do not matter.
Tests are platform independent, so different style of slashes ("/" or "\") are valid.

Note that here and throughout the project, the password is different every time you check your code.

#### Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

##### Example 1

Suppose, you have the following set of files and folders:


```shell
+---[root_folder]
    |
    +---wall.png
    +---pass.txt
    +---[docs]
    |   |
    |   +---project.py
    |   +---calc.xls
    |   +---tutorial.mp4
    |   +---[res]
    |       |
    |       +---data.json
    |   +---[output]
    |       |
    |       +---result.json
    +---[masterpiece]
        |
        +---rick_astley_never_gonna_give_you_up.mp3
```

Program output:

```shell
> python handler.py root_folder

root_folder/wall.png
root_folder/pass.txt
root_folder/docs/project.py
root_folder/docs/calc.xls
root_folder/docs/tutorial.mp4
root_folder/docs/res/data.json
root_folder/docs/output/result.json
root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3
```
