# AI GROUP PROJECT
### CS7IS2-202122 ARTIFICAL INTELLIGENCE

Sudoku puzzle is a classic problem in which missing digits
are to be placed into a 9x9 grid of squares that are split into 3x3 boxes so
that the numbers 1 through 9 appear only once in every row, column, and
box. Although every Sudoku puzzle has solution, they involve different
levels of hardship. In this paper, we introduce, implement and analyze
some of the AI algorithms suitable including uniformed-search, genetic
algorithms, constraint satisfaction and convolutional neural network to
solve any given Sudoku puzzles. The results are compared with respect
to the time taken and memory consumed by each algorithms

## Sudoku Search Agent

## Sudoku Search Agent

The seach agent finds solutions for a given incomplete sudoku puzzle using Depth-first seach and Breadth-first search.
To solve sudoku puzzles using seach algorithms, go to SudokuSearchAgent directory.

### To install the required dependencies, execute the following command 

``` pip install -r requirements.txt```

```bash
python main.py agent puzzle
```

 ### simply run

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


## Backtracking Agent

To use Backtracking Agent, follow the instruction below. make sure that you are in Backtracking folder: 

### To install the required dependencies, execute the following command:
```bash
pip install -r requirements.txt
```

```bash
python main.py
```
## Sudoku CNN Algorithm

To use this agent, go to SudokuCNNSolver folder. We have already included the pretrained model `best_weights.hdf5` which can be used to
solve the different categories of sudoku puzzles. 

### To install the required dependencies, execute the following command:

```bash
pip install -r requirements.txt
```

### Execute the following command to run the model against different categories of sudoku puzzles - 

```bash
python AnalyseCNNmodel.py
```

## Sudoku Genetic Algorithm

genetic algorithm is a search heuristic method to solve the problem, self-discovery and make judgement quickly and efficiently. this algorithm is inspired by Darwinism, which is a biological evolution theory that all species arise through natural selection. A genetic algorithm generates a patch of generations with possible solutions for the research problem and selects the fittest individuals which are parents to reproduce the next child generation. Evaluate them to get the fittest children as the next parents to get the finalized best solution.

### To install the required dependencies, execute the following command:

```bash
pip install -r requirements.txt
```

### Run the program by executing:

```bash
python ShowResults.py
```
