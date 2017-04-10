# Diamond_Square

Implementation of Diamond Square algorithm.  Used Matplotlib version 1.5.3 and Numpy version 1.11.2.
Editor:Atom.io Link:https://atom.io/ 
Terminal: Powershell(don't judge me).

Input values are the ds_steps which defines grid length according to (2^ds_steps + 1) & max_rnd for minimum and maximum random number.
ds_steps also serves as a measure of level which is looped 0 -> ds_steps.  Where 0 represents large shapes and ds_steps represents small shapes according to below image. Source: https://en.wikipedia.org/wiki/Diamond-square_algorithm.

![](https://raw.githubusercontent.com/crowgers/Diamond_Square/master/Images/Diamond_Square_Algorithm.png)

The function _rnjesus takes single input value N and gerenates a random value between -N -> +N.

The grid is seeded with 4 random values in range -max_rnd -> +max_rnd.
Each point is computed by taking the average and adding a random number to it. This random number is reduced at each level (see above) according to ds_steps/(level+1).  This is a crude implementation but allows for sufficiently random terrain & sufficient smoothness.
Experiementing with gaussian random numbers and other such methods to get a better smoothing. 

Square step (so called as reference points form a square) is computed simply.
C is the computed point using marked points below.

      NW          NE
            C
      SW          SE

Diamond step (so called as reference points form a diamond) requires a wrapping if the index is at minimum and maximum grid values.
The loop also has some redundancies as some points will be looked at twice however once a point has been assigned a non-zero value it will not be recomputed.

N,W,S,E are computed using surrounding reference points. NN, WW, EE, SS are points which wrap if outside index range.

                  NN
            NW    N     NE
      WW    W     C     E     EE
            SW    S     SE
                  SS

TODO-
Add a smoothing function as 3D plot looks aweful.
Rename some variables to be more obvious
Reduce number of input arguments to some functions for clarity.
Add in function to take user input.  
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

