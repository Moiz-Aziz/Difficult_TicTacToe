import random


# Todo: Compolete the remaining give the number:

class DumbAi():
    
        
    
    def GetAvailableValues(self, board: list) -> list:
        
        sortedBoard: list[int] = []
        
        for items in board:
            if items == "X" or items == "O":
                continue
            sortedBoard.append(items)
                
        return sortedBoard
    
    
    def GetPlayerValues(self, playerNumber: int, playerType: str, board: list, win: int) -> list:
        if board[win] == "X" or board[win] == "O":
                    
            if playerNumber == 0:
                playerType = board[win]
                    
            if board[win] == playerType:
                playerNumber += 1
            else:
                playerNumber = 0
                playerType = ""
                
        return [playerNumber, playerType]
    
    
    def ExtractSignificantList(self, winning: list, board: list)     -> list:
        
        significantListOfValues: list = []
        
        for wins in winning:
            
            playerType = ""
            playerNumber = 0
            
            for win in wins:
                
                
                players = self.GetPlayerValues(playerNumber=playerNumber, playerType=playerType, board=board, win=win)
                playerType = players[1]
                playerNumber = players[0]
            
            
            significantListOfValues.append([playerNumber, playerType, wins])
                    
                
        return significantListOfValues
                
                
                            
    def GetBestSignificant(self, significantList: list) -> int:
        
        highestPlayerNumber = 0
        highestPlayerType = ""
        specials: list = [0, 2, 4, 6, 8]
        bestlist = [specials]
        
        for i in significantList:
            
            if highestPlayerNumber < i[0]:
                highestPlayerNumber = i[0]
                highestPlayerType = i[1]
                bestlist[0] = i[-1]
            
            
            if highestPlayerNumber == i[0] and highestPlayerType != i[1]:
                
                if i[1] == "O":
                    highestPlayerType == i[0]
                    bestlist[0] = i[-1]
                    
        
        if highestPlayerNumber < 2:
            bestlist[0] = specials
                    
        return bestlist



    def GetNotDumbComputerNumber(self, availableTries: list[int], bestlist: list[int]):
        
        bestlistssingular: list[int] = bestlist[0]
        
        probableValues: list[int] = []
        
        
        for values in availableTries:
            values -= 1
            
            if values in bestlistssingular:
                probableValues.append(values)
                
                
        
        
        
        # if len(probableValues) == 5:
        #     return 4
        
        # if len(probableValues) == 4 and 4 in probableValues:
        #     return 4
        
        
        
        if len(probableValues) == 0:
            return availableTries[0]-1
        return random.choice(probableValues)
    
    
    def LittleDumbAi(self, board: list[int]) -> int:
        
        computerChoices: list[int] = self.GetAvailableValues(board=board)
        computer: int = self.GetRandomComputerChoice(computerChoices)
        return computer
    
    def NotSoDumbAi(self) -> int:
        
        availableTries: list[int] = self.GetAvailableValues(board=self.board)
        bestList: list[int] = self.GetBestSignificant(self.ExtractSignificantList(self.wins, self.board))
        computer: int = self.GetNotDumbComputerNumber(availableTries, bestList)
        print(f"(Smart-Computer-O) Choosed ({computer+1})")    
        return computer
        
        
        
        
        
    
    
    def GetRandomComputerChoice(self, sortedBoard: list) -> int:
        computerChoice = random.choice(sortedBoard)
        print(f"(Dumb-Computer-O) Choosed ({computerChoice})")    
        return computerChoice-1
        
        
        
    
    
    
    
                
                
 
 
 
                