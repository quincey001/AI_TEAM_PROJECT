
## Sudoku Constraint Satisfaction Agent

This agent will solve any Sudoku puzzle using constraing satisfaction with Pulp package from python. 

## To install the required dependencies, execute the following command 

```bash
pip install -r requirements.txt
```
 ## Run the program
 
replace puzzle with the name of the puzzles exist in samples folder.

```bash
python main.py puzzle
```

for example, the below command will run dfs agent for puzzle number 1:

```bash
python main.py 1
```
The output should look like this:

```bash
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
