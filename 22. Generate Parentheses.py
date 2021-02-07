class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        next_layer = {}
        if n ==0:
            return []
        else:
            current_layer = {"(":[1,1]}  # (()(=0
        length =1
        while length < 2*n:
            for item, info in current_layer.items():
                score = info[0]
                num_of_left = info[1]
                if score > 2*n-length:
                    continue
                i = item
                if num_of_left < n:
                    item+="("
                    next_layer[item]= [score+1,num_of_left+1]
                if score > 0:
                    i += ")"
                    next_layer[i]= [score-1,num_of_left]
                
            current_layer = next_layer
            next_layer = {}
            length += 1
        
        answer = []
        for item, info in current_layer.items():
            score = info[0]
            if score==0:
                answer.append(item)
        return answer