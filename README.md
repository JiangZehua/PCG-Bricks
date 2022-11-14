# PCG-Bricks: Procedural Conten Generation placing Brick-like objects

This is a toy library for procedurally generating content in the form of brick-like objects. It is based on the [3D PCG Paper](https://arxiv.org/abs/2206.13623) by us, implementing the LEGO ish ideas. This is just a playground for me to write some dirty code and tell myself I can write a new gym environment. Also this is a test bed for weird packages I want to try out. 
Built on top of previous genius works [gym-pcgrl](https://github.com/amidos2006/gym-pcgrl) and [control-pcgrl](https://github.com/smearle/control-pcgrl).

## To Do / Potential Features
1. Supervised way to generate structures (given a structure in LEGO / Minecraft, generate a similar structure), use least number of bricks / least number of steps to achieve this; find the "crucial bricks types" without which the structure cannot be built.
2. Use same set of bricks to generate 2 different structures (transfer between structures)
3. Make it text guided (generate a structure given a text description)
4. Make it image guided (generate a structure given an image)
5. Not only voxel based

## Implementation
1. use a tree structure to represent each point in the block? If you want to remove the block, you need to remove all the points in that action patch. Also need to represent the slubs (the points that can connect 2 bricks together) create a class for each brick type
2. [copilot propose this, also sounds interesting]use a graph structure to represent the structure, each node is a brick, each edge is a slub. If you want to remove a brick, you need to remove all the edges that connect to that brick. Also need to represent the slubs (the points that can connect 2 bricks together) create a class for each brick type