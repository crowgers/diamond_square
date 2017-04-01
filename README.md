# Diamond_Square

Implementation of Diamond Square algorithm.  Used Matplotlib version 1.5.3 and Numpy version 1.11.2.
IDE: Jetbrains Pycharm Community edition. Link: https://www.jetbrains.com/pycharm/download/#section=windows

Input values are the G_SIZE which defines grid length according to (2^G_SIZE + 1) & G_MAX_RND for minimum and maximum random number.
G_SIZE also serves as a measure of level which is looped 0 -> G_SIZE.  Where 0 represents large shapes and G_SIZE represents small shapes according to below image. Source: https://en.wikipedia.org/wiki/Diamond-square_algorithm.

![](https://raw.githubusercontent.com/crowgers/Diamond_Square/master/Images/Diamond_Square Algorithm.png)

The function _rnjesus takes single input value N and gerenates a random value between -N -> +N.

The grid is seeded with 4 random values in range -G_MAX_RND -> +G_MAX_RND.
Each point is computed by taking the average and adding a random number to it. This random number is reduced at each level (see above) according to G_SIZE/(level+1).  This is a crude impimentation but allows for sufficently random terrain & sufficient smoothness.

Square step (so called as reference points form a square) is computed simply.
C is the computed point using marked points below.

      NW          NE
            C
      SW          SE

Diamond step (so called a reference points form a diamond) requires a wrapping if the index are minimum and maximum values.
The loop also has some redundancies as two points will be looked at twice however once a point has been assigned a value it will not be recomputed.

N,W,S,E are computed using surrounding reference points. NN, WW, EE, SS are points which wrap if outside index range.

                  NN
            NW    N     NE
      WW    W     C     E     EE
            SW    S     SE
                  SS

TODO-
Add a smoothing function as 3D plot looks aweful.
![](https://raw.githubusercontent.com/crowgers/Diamond_Square/master/Images/DiamondSquare3D.png)
![](https://raw.githubusercontent.com/crowgers/Diamond_Square/master/Images/DiamondSquare3D-2.png)

Code is sufficiently small to leave in one file although could potentially split functions into a methods file and have a short ~10-15 line main file which loads them as needed.

Sample images

![](https://raw.githubusercontent.com/crowgers/Diamond_Square/master/Images/DiamondSquare_262k.png)
![](https://raw.githubusercontent.com/crowgers/Diamond_Square/master/Images/DiamondSquare_262k-1.png)
![](https://raw.githubusercontent.com/crowgers/Diamond_Square/master/Images/DiamondSquare_1M.png)
![](https://raw.githubusercontent.com/crowgers/Diamond_Square/master/Images/DiamondSquare_1M-1.png)
![](https://raw.githubusercontent.com/crowgers/Diamond_Square/master/Images/DiamondSquare_1M-2.png)
![](https://raw.githubusercontent.com/crowgers/Diamond_Square/master/Images/DiamondSquare_Noisy.png)

