from PyQt5 import QtCore, QtWidgets

class Steps_window:
    def setupUi(self, Dialog, steps):
        Dialog.setObjectName("StepsDialog")
        Dialog.resize(837, 699)
        Dialog.setMinimumSize(QtCore.QSize(800, 800))
        Dialog.setMaximumSize(QtCore.QSize(1000, 1000))

        # Create a grid layout
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        # Title label
        self.stepsLabel = QtWidgets.QLabel(Dialog)
        self.stepsLabel.setText("Answer")
        self.stepsLabel.setStyleSheet("font-size: 20px; margin-bottom: 20px; font-weight: bold;")
        self.stepsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.stepsLabel, 0, 1, 1, 3)

        # Create a grid to show the 8-puzzle
        self.puzzleGrid = QtWidgets.QGridLayout()
        self.gridLayout.addLayout(self.puzzleGrid, 0, 0, 1, 1)

        # Create the 3x3 grid of labels
        self.puzzle_labels = [[QtWidgets.QLabel(Dialog) for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.puzzle_labels[i][j].setFixedSize(100, 100)
                self.puzzle_labels[i][j].setAlignment(QtCore.Qt.AlignCenter)
                self.puzzle_labels[i][j].setStyleSheet("border: 2px solid black; font-size: 24px; font-weight: Bold; border-radius: 5px; background-color: #3B4252; color: #ECEFF4; border: 2px solid #4C566A;")
                self.puzzleGrid.addWidget(self.puzzle_labels[i][j], i, j)

        # Step counter label
        self.step_counter_label = QtWidgets.QLabel(Dialog)
        self.step_counter_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.step_counter_label, 2, 0, 1, 3)

        # Total cost label
        self.total_cost_label = QtWidgets.QLabel(Dialog)
        self.total_cost_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.total_cost_label, 5, 0, 1, 3)

        # Nodes expanded label
        self.nodes_expanded_label = QtWidgets.QLabel(Dialog)
        self.nodes_expanded_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.nodes_expanded_label, 4, 0, 1, 3)

        # Search depth label
        self.search_depth_label = QtWidgets.QLabel(Dialog)
        self.search_depth_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.search_depth_label, 3, 0, 1, 3)

        # Running time label
        self.running_time_label = QtWidgets.QLabel(Dialog)
        self.running_time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.running_time_label, 6, 0, 1, 3)

        # Create navigation buttons
        self.previousButton = QtWidgets.QPushButton("Previous", Dialog)
        self.nextButton = QtWidgets.QPushButton("Next", Dialog)
        self.previousButton.setFixedSize(100, 40)  # Set the size of the Previous button
        self.nextButton.setFixedSize(100, 40)      # Set the size of the Next button
        self.previousButton.clicked.connect(self.show_previous_step)
        self.nextButton.clicked.connect(self.show_next_step)
        self.gridLayout.addWidget(self.previousButton, 0, 1)
        self.gridLayout.addWidget(self.nextButton, 0, 3)

        # Create the OK button
        self.okButton = QtWidgets.QPushButton("Play Again", Dialog)
        self.okButton.setFixedSize(170, 40)        # Set the size of the OK button
        self.okButton.clicked.connect(Dialog.accept)
        self.gridLayout.addWidget(self.okButton, 0, 2)

        # Apply stylesheet to buttons after they are created
        self.previousButton.setStyleSheet("QPushButton { background-color: #A3BE8C; color: #2E3440; font-size: 18px; font-weight: Bold } QPushButton:hover { background-color: #1976D2; }")
        self.nextButton.setStyleSheet("QPushButton { background-color: #A3BE8C; color: #2E3440; font-size: 18px; font-weight: Bold } QPushButton:hover { background-color: #1976D2; }")
        self.okButton.setStyleSheet("QPushButton { background-color: #A3BE8C; color: #2E3440; font-size: 18px; font-weight: Bold } QPushButton:hover { background-color: #1976D2; }")

        # Initialize step index
        self.steps = steps
        self.current_step_index = 0
        self.previous_state = None
        self.populate_steps(steps)
        
        # Set theme (background color, text color, etc.)
        Dialog.setStyleSheet("""
            QWidget {
                background-color: #2E3440;
                color: #D8DEE9;
            }
            QLabel {
                color: #D8DEE9;
                font-size: 16px;
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
        """)

    def update_step_display(self):
        if self.steps and isinstance(self.steps, dict):
            path = self.steps['path']
            if self.current_step_index < len(path):
                self.update_grid(path[self.current_step_index])
                self.total_cost_label.setText(f"Total Cost to reach the Goal: {self.steps['path_cost']}")
                self.step_counter_label.setText(f"Step: {self.current_step_index + 1}/{len(path)}")
            else:
                self.clear_grid()
                self.step_counter_label.setText("")
                self.total_cost_label.setText("")

        # Update button states
        self.previousButton.setEnabled(self.current_step_index > 0)
        self.nextButton.setEnabled(self.current_step_index < self.steps_length - 1)

    def populate_steps(self, steps):
        # Format the steps for display in the puzzle grid
        self.steps = steps
        self.steps_length = len(steps['path']) if isinstance(steps, dict) else 0

        if self.steps_length > 0:
            self.update_grid(self.steps['path'][0])  # Display the first step in the grid
            self.total_cost_label.setText(f"Total Cost to reach the Goal: {self.steps['path_cost']}")
            self.nodes_expanded_label.setText(f"Nodes Expanded: {self.steps['nodes_expanded']}")
            self.search_depth_label.setText(f"Search Depth: {self.steps['search_depth']}")
            self.step_counter_label.setText(f"Step: 1/{self.steps_length}")
            self.running_time_label.setText(f"Running Time: {self.steps['running_time']:.4f} seconds")
            
            self.total_cost_label.setStyleSheet("color: #A3BE8C; font-size: 20px;   font-weight: Bold; ")
            self.nodes_expanded_label.setStyleSheet("color: #A3BE8C; font-size: 20px;   font-weight: Bold;")
            self.search_depth_label.setStyleSheet("color: #A3BE8C; font-size: 20px;   font-weight: Bold;")
            self.step_counter_label.setStyleSheet("color: #A3BE8C; font-size: 20px;   font-weight: Bold;")
            self.running_time_label.setStyleSheet("color: #A3BE8C; font-size: 20px;   font-weight: Bold;")
            
        else:
            self.clear_grid()  # Clear the grid if no solution is found

        # Enable or disable buttons based on the current step index
        self.previousButton.setEnabled(self.current_step_index > 0)
        self.nextButton.setEnabled(self.current_step_index < self.steps_length - 1)

    def update_grid(self, state):
        
        if isinstance(state, int):
            state = str(state)
    
        if len(state) == 8:
            state = "0" + state
        
        # Update the 3x3 grid to display the current puzzle state
        grid_values = [int(char) for char in state]
        previous_grid_values = [int(char) for char in self.previous_state] if self.previous_state else None

        for i in range(3):
            for j in range(3):
                value = grid_values[i * 3 + j]
                label = self.puzzle_labels[i][j]
                label.setText(str(value) if value != 0 else "")

                # Highlight the moved tile
                if previous_grid_values and value != 0 and value != previous_grid_values[i * 3 + j]:
                    label.setStyleSheet("border: 2px solid black; font-size: 24px; font-weight: Bold; border-radius: 5px; background-color: #88C0D0; color: #2E3440;")
                else:
                    label.setStyleSheet("border: 2px solid black; font-size: 24px; font-weight: Bold; border-radius: 5px; background-color: #3B4252; color: #ECEFF4; border: 2px solid #4C566A;")

        self.previous_state = state

    def clear_grid(self):
        # Clear the puzzle grid
        for i in range(3):
            for j in range(3):
                self.puzzle_labels[i][j].setText("")
                
    def show_previous_step(self):
        if self.current_step_index > 0:
            self.current_step_index -= 1
            self.update_step_display()

    def show_next_step(self):
        if self.current_step_index < self.steps_length - 1:
            self.current_step_index += 1
            self.update_step_display()