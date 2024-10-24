import numpy as np
from itertools import product

# Define the 3D block
b0 = np.array([
    [
        [0, 1],
        [0, 1],
        [1, 1],
        [1, 1]
    ],
    [
        [0, 1],
        [0, 1],
        [0, 0],
        [0, 0],
    ],
    [
        [0, 1],
        [0, 1],
        [0, 0],
        [0, 0],
    ]
])

# Assuming we have six identical blocks
blocks = [b0.copy() for _ in range(6)]

# Define the 3D board size (4x4x4)
board_size = (4, 4, 4)
board = np.zeros(board_size, dtype=int)

# Function to generate all unique orientations of a 3D block without reflections
def get_unique_orientations_3d_no_reflections(block):
    orientations = []
    seen_hashes = set()
    # Possible rotations: 0°, 90°, 180°, 270° around each axis
    rotations = [0, 1, 2, 3]
    for rx, ry, rz in product(rotations, repeat=3):
        rotated = block.copy()
        if rx > 0:
            rotated = np.rot90(rotated, rx, axes=(1, 2))
        if ry > 0:
            rotated = np.rot90(rotated, ry, axes=(0, 2))
        if rz > 0:
            rotated = np.rot90(rotated, rz, axes=(0, 1))
        # Compute a hashable representation
        occupied_positions = np.argwhere(rotated > 0)
        if occupied_positions.size == 0:
            continue
        occupied_positions -= occupied_positions.min(axis=0)  # Normalize position
        shape_hash = tuple(map(tuple, sorted(occupied_positions.tolist())))
        # Check for uniqueness
        if shape_hash not in seen_hashes:
            seen_hashes.add(shape_hash)
            orientations.append(rotated)
    return orientations

# Generate all unique orientations for each block without reflections
block_orientations = []
for idx, block in enumerate(blocks):
    orientations = get_unique_orientations_3d_no_reflections(block)
    block_orientations.append(orientations)
    print(f"Block {idx}: {len(orientations)} unique orientations")

# Initialize the used blocks list
used_blocks = [False] * len(blocks)

# Function to check if a block can be placed at a given position
def can_place(board, block, x, y, z):
    block_shape = block.shape
    board_shape = board.shape
    if (x + block_shape[0] > board_shape[0] or
        y + block_shape[1] > board_shape[1] or
        z + block_shape[2] > board_shape[2]):
        return False
    # Check for overlap
    block_mask = block > 0
    board_subsection = board[x:x+block_shape[0], y:y+block_shape[1], z:z+block_shape[2]]
    if np.any(np.logical_and(board_subsection > 0, block_mask)):
        return False
    return True

# Function to place a block on the board
def place_block(board, block, x, y, z, block_id):
    block_mask = block > 0
    board[x:x+block.shape[0], y:y+block.shape[1], z:z+block.shape[2]][block_mask] = block_id

# Function to remove a block from the board
def remove_block(board, block, x, y, z):
    block_mask = block > 0
    board[x:x+block.shape[0], y:y+block.shape[1], z:z+block.shape[2]][block_mask] = 0

# Recursive function to solve the puzzle
def solve(board, blocks, block_orientations, used_blocks):
    if all(used_blocks):
        return True  # All blocks have been placed successfully
    for i, used in enumerate(used_blocks):
        if not used:
            used_blocks[i] = True
            for orientation in block_orientations[i]:
                for x in range(board.shape[0]):
                    for y in range(board.shape[1]):
                        for z in range(board.shape[2]):
                            if can_place(board, orientation, x, y, z):
                                place_block(board, orientation, x, y, z, i+1)
                                if solve(board, blocks, block_orientations, used_blocks):
                                    return True
                                remove_block(board, orientation, x, y, z)
            used_blocks[i] = False
            # If none of the orientations could be placed, backtrack
            return False
    return False

# Start solving the puzzle
if solve(board, blocks, block_orientations, used_blocks):
    print("Solution found:")
    print(board)
else:
    print("No solution found.")

# Optional: Visualize the solution
def visualize_board(board):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    occupied_positions = np.argwhere(board > 0)
    block_ids = board[board > 0]
    ax.scatter(occupied_positions[:, 0], occupied_positions[:, 1], occupied_positions[:, 2], c=block_ids, cmap='tab10')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

# Uncomment to visualize the solution
visualize_board(board)
