    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas)<sum(cost):
            return -1
        start=0
        curr_gas=0
        for i in range(len(gas)):
            curr_gas+=gas[i]-cost[i]
            if curr_gas<0:
                start+=1
                curr_gas=0
        return start
