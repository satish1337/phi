import matplotlib.pyplot as plt
import numpy as np

from matplotlib import animation, rc

# Display matplotlib animations as HTML5 videos in a Jupyter Notebook
rc('animation', html='html5')

def animate_transform(A, grid=None, num_steps=50, repeat=False):
    """
        Animates the effect a transform has on a given grid.
        If no grid is given, one will be generated.

        You can expect a small delay while the function generates the animation.
    """
    def colorizer(x, y):
        """Map x-y coordinates to a unique rgb color"""
        r = min(1, 1 - y/3)
        g = min(1, 1 + y/3)
        b = 1/4 + x/16
        return r, g, b

    def stepwise_transform(A, grid, num_steps):
        """
            Returns a list of transformed grids,
            stepping slowly from the given `grid` to
            the grid `A @ grid`.
        """
        # create empty array of the right size
        transgrid = np.zeros((num_steps + 1, ) + np.shape(grid))
        # compute intermediate transforms
        for i in range(num_steps + 1):
            intermediate = np.eye(2) + i / num_steps * (A - np.eye(2))
            # apply intermediate matrix transformation
            transgrid[i] = intermediate @ grid
        return transgrid

    if grid is None:
        # Create a grid of points in x-y space
        xvals = np.linspace(-4, 4, 9)
        yvals = np.linspace(-3, 3, 7)
        grid = np.column_stack([[x, y] for x in xvals for y in yvals])

    # Map grid coordinates to colors. Done only for xygrid, not all grids.
    colors = list(map(colorizer, grid[0], grid[1]))
    intermediate_transforms = stepwise_transform(A, grid, num_steps)
    fig = plt.figure(figsize=(6, 6))

    xmin = min(min(grid[0]), min(intermediate_transforms[-1][0]))
    xmax = max(max(grid[0]), max(intermediate_transforms[-1][0]))
    ymin = min(min(grid[1]), min(intermediate_transforms[-1][1]))
    ymax = max(max(grid[1]), max(intermediate_transforms[-1][1]))

    ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
    scatter = ax.scatter([], [], c=colors)
    # Prevent `%matplotlib inline` from displaying the above scatter plot.
    plt.close()

    def update(i):
        """Draws the ith intermediate transform"""
        scatter.set_offsets(intermediate_transforms[i].T)
        return scatter,

    return animation.FuncAnimation(fig,
                                   update,
                                   interval=50,
                                   frames=num_steps,
                                   blit=True,
                                   repeat=repeat)


  A = np.column_stack([[1, 0], [2, 1]])
  anim = animate_transform(A, repeat=True)
  anim.save('shear.mp4')
  anim

