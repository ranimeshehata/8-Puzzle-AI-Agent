from dfs import dfs_solver
from Iterative_dfs import iterative_dfs_solver
from BFS import BfsAlgorithm
from AStar import AStarAlgorithm
from steps import Steps_window
from PyQt5 import QtCore, QtGui, QtWidgets

class EightPuzzleGUI(object):
    def set_board(self, puzzle):    # Initialize board puzzle
        puzzle.setObjectName("Puzzle")
        puzzle.resize(837, 699)
        puzzle.setMinimumSize(QtCore.QSize(800, 800))
        puzzle.setMaximumSize(QtCore.QSize(1000, 1000))
        puzzle.setIconSize(QtCore.QSize(20, 20))
        puzzle.setAnimated(True)
        puzzle.setDocumentMode(False)
        puzzle.setTabShape(QtWidgets.QTabWidget.Rounded)
        puzzle.setDockNestingEnabled(False)

        self.centralwidget = QtWidgets.QWidget(puzzle)
        self.centralwidget.setObjectName("centralwidget")
        
        # Create the grid layout and center it
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setAlignment(QtCore.Qt.AlignCenter)
        # Add a text label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setText("Enter the initial state of the 8-puzzle")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 20px; margin-bottom: 20px; font-weight: bold;")
        self.gridLayout.addWidget(self.label, 0, 10, 3, 1)
        # Set up frame for grid
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(400, 400))
        self.frame.setMaximumSize(QtCore.QSize(400, 400))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # Create grid layout for line edits (input boxes)
        self.lineEdit_list = []
        for row in range(3):
            for col in range(3):
                lineEdit = QtWidgets.QLineEdit(self.frame)
                lineEdit.setObjectName(f"lineEdit_{row}_{col}")
                font = QtGui.QFont()
                font.setPointSize(30)
                font.setBold(True)
                font.setWeight(75)
                lineEdit.setFont(font)
                lineEdit.setAlignment(QtCore.Qt.AlignCenter)
                lineEdit.setMaximumSize(QtCore.QSize(100, 100))

                # Add to layout and list
                self.gridLayout_2.addWidget(lineEdit, row, col)
                self.lineEdit_list.append(lineEdit)

        # Add grid layout to central layout
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        # Solve button at the bottom
        self.solveButton = QtWidgets.QPushButton(self.centralwidget)
        self.solveButton.setText("Solve")
        self.solveButton.setStyleSheet("QPushButton { background-color: #A3BE8C; color: #2E3440; font-size: 18px; font-weight: Bold } QPushButton:hover { background-color: #1976D2; }")
        self.gridLayout.addWidget(self.solveButton, 1, 0, 1, 1, QtCore.Qt.AlignCenter)

        # Algorithm selection
        self.algorithmLabel = QtWidgets.QLabel("Choose Algorithm:")
        self.gridLayout.addWidget(self.algorithmLabel, 4, 0, 1, 1, QtCore.Qt.AlignCenter)

        self.algorithmGroup = QtWidgets.QButtonGroup(self.centralwidget)
        self.dfsRadio = QtWidgets.QRadioButton("DFS")
        self.bfsRadio = QtWidgets.QRadioButton("BFS")
        self.idfsRadio = QtWidgets.QRadioButton("IDFS")
        self.aStarRadio = QtWidgets.QRadioButton("A*")
        
        self.dfsRadio.setStyleSheet("color: #D8DEE9; font-size: 16px;")
        self.bfsRadio.setStyleSheet("color: #D8DEE9; font-size: 16px;")
        self.idfsRadio.setStyleSheet("color: #D8DEE9; font-size: 16px; margin-left: 5px;")
        self.aStarRadio.setStyleSheet("color: #D8DEE9; font-size: 16px;")

        self.algorithmGroup.addButton(self.dfsRadio)
        self.algorithmGroup.addButton(self.bfsRadio)
        self.algorithmGroup.addButton(self.idfsRadio)
        self.algorithmGroup.addButton(self.aStarRadio)

        self.gridLayout.addWidget(self.dfsRadio, 5, 0, 1, 1, QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.bfsRadio, 6, 0, 1, 1, QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.idfsRadio, 7, 0, 1, 1, QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.aStarRadio, 8, 0, 1, 1, QtCore.Qt.AlignCenter)

        # A* distance method selection (initially hidden)
        self.distanceMethodLabel = QtWidgets.QLabel("Choose Distance Method:")
        self.distanceMethodLabel.setVisible(False)
        
        self.distanceMethodLabel.setStyleSheet("color: #D8DEE9; font-size: 16px; font-weight: bold;")

        self.manhattanRadio = QtWidgets.QRadioButton("Manhattan")
        self.manhattanRadio.setVisible(False)
        self.euclideanRadio = QtWidgets.QRadioButton("Euclidean")
        self.euclideanRadio.setVisible(False)
        
        self.manhattanRadio.setStyleSheet("color: #D8DEE9; font-size: 16px;")
        self.euclideanRadio.setStyleSheet("color: #D8DEE9; font-size: 16px;")

        # Add distance method options to layout (initially hidden)
        self.gridLayout.addWidget(self.distanceMethodLabel, 9, 0, 1, 1, QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.manhattanRadio, 10, 0, 1, 1, QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.euclideanRadio, 11, 0, 1, 1, QtCore.Qt.AlignCenter)

        # Connect radio buttons to show/hide distance method options
        self.aStarRadio.toggled.connect(self.update_distance_method_visibility)

        # Connect solve button to the solve method
        self.solveButton.clicked.connect(self.solve)

        puzzle.setCentralWidget(self.centralwidget)

        # Set theme (background color, text color, etc.)
        puzzle.setStyleSheet("""
            QWidget {
                background-color: #2E3440;
                color: #D8DEE9;
            }
            QLineEdit {
                background-color: #3B4252;
                color: #ECEFF4;
                border: 2px solid #4C566A;
                border-radius: 5px;
            }
            QLineEdit:focus {
                border: 2px solid #88C0D0;
            }
            QLabel {
                color: #D8DEE9;
                font-size: 16px;
            }
        """)

        self.retranslateUi(puzzle)
        QtCore.QMetaObject.connectSlotsByName(puzzle)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "8-Puzzle Solver"))

    def update_distance_method_visibility(self):
        if self.aStarRadio.isChecked():
            self.distanceMethodLabel.setVisible(True)
            self.manhattanRadio.setVisible(True)
            self.euclideanRadio.setVisible(True)
        else:
            self.distanceMethodLabel.setVisible(False)
            self.manhattanRadio.setVisible(False)
            self.euclideanRadio.setVisible(False)

    def show_steps(self, steps):
        self.steps_window = QtWidgets.QDialog()
        self.steps_ui = Steps_window()
        self.steps_ui.setupUi(self.steps_window, steps)
        self.steps_window.exec_()
        
    def show_no_solutoin(self):
        QtWidgets.QMessageBox.warning(None, "No Solution", "No solution found for this puzzle.")
        
    
    def solve(self):
        # Collect numbers from the grid
        grid_values = [lineEdit.text() for lineEdit in self.lineEdit_list]
    
        # Check if the grid is empty
        if all(value == "" for value in grid_values):
            QtWidgets.QMessageBox.warning(None, "Input Error", "Please fill the grid before solving.")
            return
        
        # Validate input: 9 distinct numbers between 0 and 8
        if len(grid_values) != 9:
            QtWidgets.QMessageBox.warning(None, "Input Error", "Please enter exactly 9 numbers.")
            return

        try:
            numbers = list(map(int, grid_values))
        except ValueError:
            QtWidgets.QMessageBox.warning(None, "Input Error", "Please fill the grid before solving.")
            return

        # Check for numbers out of range or duplicates
        if any(num < 0 or num > 8 for num in numbers):
            QtWidgets.QMessageBox.warning(None, "Input Error", "Please enter numbers within the range of 0 to 8.")
            return
        
        if len(set(numbers)) != 9:
            QtWidgets.QMessageBox.warning(None, "Input Error", "Please enter distinct numbers (no duplicates).")
            return

        # Validate algorithm selection
        if not any([self.dfsRadio.isChecked(), self.bfsRadio.isChecked(), self.idfsRadio.isChecked(), self.aStarRadio.isChecked()]):
            QtWidgets.QMessageBox.warning(None, "Algorithm Selection Error", "Please choose an algorithm to solve the puzzle.")
            return
        
        if self.aStarRadio.isChecked() and not any([self.manhattanRadio.isChecked(), self.euclideanRadio.isChecked()]):
            QtWidgets.QMessageBox.warning(None, "Distance Method Selection Error", "Please choose a distance method for A*.")

        # Construct the initial state from numbers
        start_state = ''.join(map(str, numbers))  # Convert each number to a string before joining
        end_state = "012345678"
        
        if self.dfsRadio.isChecked():
            dfs = dfs_solver(start_state, end_state)
            result = dfs.search()
            if result == -1:
                self.show_no_solutoin()
                print("No solution found for this puzzle.")
            else: 
                print("DFS :")
                print(result)
                self.show_steps(result)  # Show the steps in the Steps_window
        elif self.idfsRadio.isChecked():
            iterative_dfs = iterative_dfs_solver(start_state, end_state)
            result = iterative_dfs.iterative_dfs()
            if result == -1:
                self.show_no_solutoin()
                print("No solution found for this puzzle.")
            else: 
                print("ITERATIVE DFS :")
                print(result)
                self.show_steps(result)  # Show the steps in the Steps_window
        elif self.bfsRadio.isChecked():
            bfs = BfsAlgorithm(start_state)
            result = bfs.bfs_search()
            if result == -1:
                self.show_no_solutoin()
                print("No solution found for this puzzle.")
            else: 
                print("BFS :")
                print(result)
                self.show_steps(result)
        elif self.aStarRadio.isChecked():
            if self.manhattanRadio.isChecked():
                distance_method = "manhattan"
                a_star = AStarAlgorithm(start_state)
                result = a_star.search(start_state)
                if result == -1:
                    self.show_no_solutoin()
                    print("No solution found for this puzzle.")
                else: 
                    print("A* :")
                    print(a_star.path_finder())
                    print("Nodes expanded: ", a_star.nodes_expanded())
                    print("Max Depth: ", a_star.search_depth())
                    print("Path cost/level of goal: ", a_star.path_cost())
                    print("Running time: ", a_star.running_time())
                    steps = {
                        'path': a_star.path_finder(),
                        'path_cost': a_star.path_cost(),
                        'nodes_expanded': a_star.nodes_expanded(),
                        'search_depth': a_star.search_depth(),
                        'running_time': a_star.running_time()
                    }
                    self.show_steps(steps)
            elif self.euclideanRadio.isChecked():
                distance_method = "Euclidean"
                a_star = AStarAlgorithm(start_state, distance_method)
                result = a_star.search(start_state)
                if result == -1:
                    self.show_no_solutoin()
                    print("No solution found for this puzzle.")
                else: 
                    print("A* :")
                    print(a_star.path_finder())
                    print("Nodes expanded: ", a_star.nodes_expanded())
                    print("Max Depth: ", a_star.search_depth())
                    print("Path cost/level of goal: ", a_star.path_cost())
                    print("Running time: ", a_star.running_time())
                    steps = {
                        'path': a_star.path_finder(),
                        'path_cost': a_star.path_cost(),
                        'nodes_expanded': a_star.nodes_expanded(),
                        'search_depth': a_star.search_depth(),
                        'running_time': a_star.running_time()
                    }
                    self.show_steps(steps)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = EightPuzzleGUI()
    ui.set_board(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    