class KouModel:
    def __init__(self, r, q, sigma, lambda_, p, eta1, eta2):
        '''
        Args:
            r: risk-free rate
            q: dividend yield
            sigma: volatility
            lambda_: jump indensity
            p: probability of upward jump
            eta1: rate for upward jumps (eta1 > 1)
            eta2: rate for downward jumps (eta2 > 0)
        '''

        self.r = r
        self.q = q
        self.sigma = sigma
        self.lambda_ = lambda_
        self.p = p
        self.eta1 = eta1
        self.eta2 = eta2

        # validate parameters
        assert eta1 > 1
        assert eta2 > 0
        assert 0 <= p <= 1
  
    def _compute_jump_mean(self):
        '''
        Calculate jump expectation E[V-1] = E[e^Y]-1
        '''

        # Contribution from upward jumps
        up_jump = self.p * self.eta1/(self.eta1 - 1)
        
        # Contribution from downward jumps
        down_jump = (1-self.p) * self.eta2/(self.eta2 + 1)
        
        # Calculate E[V-1]
        return up_jump + down_jump - 1

    def _compute_jump_variance(self):
        '''
        Calculate jump variance Var[V-1] = E[(e^Y)^2] - (E[e^Y])^2
        '''
        # E[(e^Y)^2] calculation
        up_jump_squared = self.p * self.eta1/(self.eta1 - 2)
        down_jump_squared = (1-self.p) * self.eta2/(self.eta2 + 2)
        E_v_squared = up_jump_squared + down_jump_squared

        # (E[e^Y])^2 calculation
        # Use existing function to get E[e^Y]
        E_v = self._compute_jump_mean() + 1

        # Return Var[V-1]
        return E_v_squared - E_v**2