# Continued Fractions

    • Continued fractions are a way of expressing real numbers through a sequence of integer divisions.

    • These have the following general form:            
                 
                1
        a₀ + -----------------
                    1
            a₁ + -------------
                        1
                a₂ + ---------
                    a₃ + ...

        
        * a₀ is an integer and a₁, a₂ . . . are positive integers
  
    • For example, let (a₀, a₁, a₂, a₃) = (1, 2, 3, 4)

                   1
        1  + ---------------
                     1
            2  + -----------
                        1
                3  + -------
                        4 

    * this has the continued fraction list written as [1; 2, 3, 4]
  
    • To compute the value of this continued fraction, start from the right of the continued fraction list and work your way to the left:

        (1) 3 + 1/4 = 13/4

        (2) 2 + 4/13 = 30/13

        (3) 1 + 13/30 = 43/30

        thus the value of the continued fractions is 43/30

    • A convergent (Cᵢ) is the fraction you get if you stop the continued fraction at each level (i):

        C₀ = a₀ = 1

        C₁ = a₀ + 1/a₁ = 1 + 1/2 = 3/2

        C₂ = a₀ + 1/(a₁ + 1/a₂) = 1 + 1/(2 + 1/3) = 1 + 1/(7/3) = 1 + 3/7 = 10/7 

        C₃ = a₀ + 1/(a₁ + 1/(a₂ + 1/a₃)) = 1 + 1/(2 + 1/(3 + 1/4)) = 1 + 1/(2 + 1/(13/4)) = 1 + 1/(2 + 4/13) = 1 + 1/(30/13) = 1 + 13/30 = 43/30

        * notice how each convergent gets closer to the true value