import randomclass Agent:        def __init__(self, environment, agents, x, y):        """        Agent that interacts with the environment and other Agent() instances.        Parameters        ----------        environment : List of lists (2D list).            Each list inside the main list is a row. Each row is a y-coordinate            and each entry in each row is an x-coordinate. Number of entries             per row must be equal to number of total rows (square matrix).        agents : list of Agent()            List of Agent() instances that will interact with each other.        x : int.            Starting x-coordinate of our Agent() instance in the environment.            Private variable.        y : int.            Starting x-coordinate of our Agent() instance in the environment.            Private variable.        Returns        -------        None.        """        self.environment = environment        self.store = 0        self._size = len(environment)        self.agents = agents        self.__x = x        self.__y = y    def __str__(self):        """        Called when printing our Agent(). Prints out information about the        current state of our instance. Especially useful when debugging.        Returns        -------        str            "Agent at coordinates (x,y). Stores: (agent's current stores)".        """        """This return following string when we print(Agent)"""        return f"Agent at coordinates ({self.__x}, {self.__y}). Stores: \            {self.store}."    @property    def y(self):        """        Property: y-coordinate.        Returns        -------        int.            y coordinate.        """        return self.__y    @y.setter    def set_y(self, y):           """        Setting the y-coordinate. If the input parameter y is None, we choose a        random y-coordinate in the environment grid.        Parameters        ----------        y : int.            DESCRIPTION.        Returns        -------        None.        """                     if y is None:            self.__y = random.randint(0,self._size)        else:            self.__y = y             @y.getter    def get_y(self):        """        Get value of attribute y.        Returns        -------        int.            y-coordinate.        """        return self.__y        @property    def x(self):        """        Property: x-coordinate.        Returns        -------        int.            x-coordinate.        """        return self.__x        @y.setter    def set_x(self, x):        """        Setting the x-coordinate. If the input parameter x is None, we choose a        random x-coordinate in the environment grid.        Parameters        ----------        x : int.            DESCRIPTION.        Returns        -------        None.        """          if x is None:            self.__x = random.randint(0,self._size)        else:            self.__x = x             @y.getter    def get_x(self):        """        Get value of attribute x.        Returns        -------        int.            x-coordinate.        """        return self.__x    def distance_between(self, agent):        """                Parameters        ----------        agent : TYPE            DESCRIPTION.        Returns        -------        None.        """        """ Finds the distance between the current agent and another agents_a"""        return(((self.__x - agent.__x)**2) +     ((self.__y - agent.__y)**2))**0.5    def move(self):        """        This function randomly moves the agent in the x or y direction by         1 unit each time it is called.        """        if random.random() < 0.5:            self.__y = (self.__y + 1) % (self._size - 1)        else:            self.__y = (self.__y - 1) % (self._size - 1)                if random.random() < 0.5:            self.__x = (self.__x +1) % (self._size - 1)        else:            self.__x = (self.__x -1) % (self._size - 1)                def eat(self): # can you make it eat what is left?        """         If there are 10 or more units of resources, this function depletes the        resources in the environment by 10 units if an Agent has landed there,        and makes them store 10.         """        if self.environment[self.__y][self.__x] >= 10:            self.environment[self.__y][self.__x] -= 10            self.store += 10        else:            self.store += self.environment[self.__y][self.__x]            self.environment[self.__y][self.__x] = 0    def share_with_neighbours(self, neighbourhood):        '''This function looks for other agents that are at a distance of        neighbourhood, and will share in equal parts its store (of food).'''        for agent in self.agents:            if self.distance_between(agent) <= neighbourhood:                tot = self.store + agent.store                average = tot/2                self.store = average                agent.store = average            else:                pass