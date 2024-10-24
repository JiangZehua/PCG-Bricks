import numpy as np

# Define the board
board = np.zeros((6, 6), dtype=int)

# Define the blocks
b0 = np.array([
    [1, 1],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
])

b1 = np.array([
    [1, 1],
    [1, 1],
    [1, 0],
    [1, 0],
])

b2 = np.array([
    [1, 1, 0],
    [1, 1, 1],
    [1, 0, 0],
])

b3 = np.array([
    [1, 0],
    [1, 0],
    [1, 1],
    [1, 0],
    [1, 0],
])

b4 = np.array([
    [1, 1, 0],
    [1, 1, 0],
    [0, 1, 1],
])

b5 = np.array([
    [0, 0, 1],
    [0, 1, 1],
    [0, 1, 0],
    [1, 1, 0],
])

blocks = [b0, b1, b2, b3, b4, b5]

# Function to generate all unique orientations of a block
def get_unique_orientations(block):
    orientations = []
    for rotation in range(4):
        rotated = np.rot90(block, rotation)
        for flip in [False, True]:
            if flip:
                flipped = np.fliplr(rotated)
            else:
                flipped = rotated
            # Check for uniqueness
            if not any(np.array_equal(flipped, x) for x in orientations):
                orientations.append(flipped)
    return orientations

# Generate all unique orientations for each block
block_orientations = []
for block in blocks:
    orientations = get_unique_orientations(block)
    block_orientations.append(orientations)

# Initialize the used blocks list
used_blocks = [False] * len(blocks)

# Function to check if a block can be placed at a given position
def can_place(board, block, row, col):
    block_height, block_width = block.shape
    board_height, board_width = board.shape
    if row + block_height > board_height or col + block_width > board_width:
        return False
    # Check for overlap
    block_mask = block > 0
    board_subsection = board[row:row+block_height, col:col+block_width]
    if np.any(np.logical_and(board_subsection > 0, block_mask)):
        return False
    return True

# Function to place a block on the board
def place_block(board, block, row, col, block_id):
    block_height, block_width = block.shape
    block_mask = block > 0
    board[row:row+block_height, col:col+block_width][block_mask] = block_id

# Function to remove a block from the board
def remove_block(board, block, row, col):
    block_height, block_width = block.shape
    block_mask = block > 0
    board[row:row+block_height, col:col+block_width][block_mask] = 0

# Recursive function to solve the puzzle
def solve(board, blocks, block_orientations, used_blocks):
    if all(used_blocks):
        if np.all(board > 0):
            return True
        else:
            return False
    for i, used in enumerate(used_blocks):
        if not used:
            used_blocks[i] = True
            for orientation in block_orientations[i]:
                for row in range(board.shape[0]):
                    for col in range(board.shape[1]):
                        if can_place(board, orientation, row, col):
                            place_block(board, orientation, row, col, i+1)
                            if solve(board, blocks, block_orientations, used_blocks):
                                return True
                            remove_block(board, orientation, row, col)
            used_blocks[i] = False
            return False
    return False

# Start solving the puzzle
if solve(board, blocks, block_orientations, used_blocks):
    print("Solution found:")
    print(board)
else:
    print("No solution found.")
