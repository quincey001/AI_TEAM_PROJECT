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

The seach agent finds solutions for a given incomplete sudoku puzzle using Depth-first seach and Breadth-first search.
To solve sudoku puzzles using seach algorithms, go to SudokuSearchAgent directory, and simply run:

```bash
python main.py agent puzzle
```

replace **agent** with **dfs** to use DFS algorithm and with **bfs** to use BFS algorithm.
replace puzzle with the name of the puzzles exist in samples folder.

for example, the below command will run dfs agent for puzzle number 1:

```bash
python main.py dfs 1
```

## Backtracking Agent

To use Backtracking Agent, follow the instruction below. make sure that you are in Backtracking folder: 

```bash
pip install -r requirements.txt
```

```bash
python main.py
```
## Sudoku CNN Algorithm

To use this agent, go to SudokuCNNSolver folder. We have already included the pretrained model `best_weights.hdf5` which can be used to
solve the different categories of sudoku puzzles. 

## To install the required dependencies, execute the following command - 

```bash
pip install -r requirements.txt
```

### Execute the following command to run the model against different categories of sudoku puzzles - 

```bash
python AnalyseCNNmodel.py
```

## Sudoku Genetic Algorithm

genetic algorithm is a search heuristic method to solve the problem, self-discovery and make judgement quickly and efficiently. this algorithm is inspired by Darwinism, which is a biological evolution theory that all species arise through natural selection. A genetic algorithm generates a patch of generations with possible solutions for the research problem and selects the fittest individuals which are parents to reproduce the next child generation. Evaluate them to get the fittest children as the next parents to get the finalized best solution.

## To install the required dependencies, execute the following command - 

```bash
pip install -r requirements.txt
```

Then simply run

```bash
python ShowResults.py
```