# Duplicate-File-Handler-JetBrains-Academy
This project jetbrains academy https://hyperskill.org/projects/176

## Work on project. Stage 2/4: How much does it weigh?
### Objectives
Keep the functionality from the previous stage. To complete this stage, your program should:

1. Accept a command-line argument that is a root directory with files and folders. 
Print ```Directory is not specified``` if there is no command-line argument;
2. Read user input that specifies the file format (see examples). Empty input should match any file format;
3. Print a menu with two sorting options: ```Descending``` and ```Ascending```. They both represent the respective order by size of groups of files. Read the input.
Print ```Wrong option``` if any other input is entered. Repeat until a correct input is provided;
4. Iterate over folders and print the information about files of the same size: their size, path, and names.

Please note: you should use full path to file **from root directory** when printing or reading.

Note that here and throughout the project, the password is different every time you check your code.

#### Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

##### Example 1

Suppose, you have the following set of files and folders:


```shell
+---[root_folder]
    +---gordon_ramsay_chicken_breast.avi /4590560 bytes
    +---[audio]
    |   |
    |   +---voice.mp3 /2319746 bytes
    |   +---sia_snowman.mp3 /4590560 bytes
    |   +---nea_some_say.mp3 /3232056 bytes
    |   +---[classic]
    |   |   |
    |   |   +---unknown.mp3 /3422208 bytes
    |   |   +---vivaldi_four_seasons_winter.mp3 /9158144 bytes
    |   |   +---chopin_waltz7_op64_no2.mp3 /9765504 bytes
    |   +---[rock]
    |       |
    |       +---smells_like_teen_spirit.mp3 /4590560 bytes
    |       +---numb.mp3 /5786312 bytes
    +---[masterpiece]
        |
        +---rick_astley_never_gonna_give_you_up.mp3 /3422208 bytes
```

Program output:

```shell
> python handler.py root_folder

Enter file format:
>mp3

Size sorting options:
1. Descending
2. Ascending

Enter a sorting option:
> 3

Wrong option

Enter a sorting option:
> 2

3422208 bytes
root_folder/audio/classic/unknown.mp3
root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3

4590560 bytes
root_folder/audio/rock/smells_like_teen_spirit.mp3
root_folder/audio/sia_snowman.mp3
```
