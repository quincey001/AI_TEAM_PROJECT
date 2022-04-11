# AI_TEAM_PROJECT

## Sudoku Search Agent

The seach agent finds solutions for a given incomplete sudoku puzzle using Depth-first seach and Breadth-first search.
To solve sudoku puzzles using seach algorithms, go to SudokuSearchAgent directory.

## To install the required dependencies, execute the following command 

``` pip install -r requirements.txt```

```bash
python main.py agent puzzle
```

 ## simply run

replace **agent** with **dfs** to use DFS algorithm and with **bfs** to use BFS algorithm.
replace puzzle with the name of the puzzles exist in samples folder.

for example, the below command will run dfs agent for puzzle number 1:

```bash
python main.py dfs 1
```
The output should look like this:

```bash
Depth First Search
Solution Found in 134 steps
8 5 1 9 4 3 7 2 6 
9 2 6 1 7 8 3 4 5 
4 7 3 6 5 2 8 9 1 
5 6 8 7 2 4 9 1 3 
1 9 7 3 8 6 2 5 4 
3 4 2 5 1 9 6 8 7 
2 1 9 4 6 7 5 3 8 
7 3 4 8 9 5 1 6 2 
6 8 5 2 3 1 4 7 9 
```
if you like to try Breadth-first search agent, run the command below:
```bash
python main.py bfs 1
```
The output should look like this:

```bash
Breadth First Search
Solution Found in 220 steps
8 5 1 9 4 3 7 2 6 
9 2 6 1 7 8 3 4 5 
4 7 3 6 5 2 8 9 1 
5 6 8 7 2 4 9 1 3 
1 9 7 3 8 6 2 5 4 
3 4 2 5 1 9 6 8 7 
2 1 9 4 6 7 5 3 8 
7 3 4 8 9 5 1 6 2 
6 8 5 2 3 1 4 7 9 
```
