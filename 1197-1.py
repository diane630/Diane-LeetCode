# IMC OA solution
# A: starting of knight, x1, y1
# B：ending of knight, x2, y2
# C: starting of bishop, x3, y3 (don't move)
# board: m x n

from collections import deque

class Solution:
    def min_step(self, x1, y1, x2, y2, x3, y3, m, n):
        if (x1, y1) == (x2, y2):
            return 0

        knight_offset = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, -1), (2, 1), (-2, 1), (-2 ,-1)]
        knight_pos = deque([(x1, y1, True)]) # x, y, bishop exist?
        knight_visited_with_bishop = set()
        knight_visited_without_bishop = set()

        def is_threatened(x1, y1, x2, y2) -> bool:
            if abs(x1 - x2) == abs(y1 - y2):
                return True
            return False

        step = 0
        while knight_pos:
            step += 1
            for i in range(len(knight_pos)):
                c = knight_pos.popleft()
                for (x_offset, y_offset) in knight_offset:
                    new_x = c[0] + x_offset
                    new_y = c[1] + y_offset
                    new_bishop_exist = c[2]
                    if (new_x, new_y) == (x2, y2):
                        # ending
                        return step
                    if new_bishop_exist and (new_x, new_y) == (x3, y3):
                        # eat the bishop
                        new_bishop_exist = False
                    if not (0 <= new_x < m and 0 <= new_y < n):
                        continue
                    if new_bishop_exist and (new_x, new_y) not in knight_visited_with_bishop and not is_threatened(new_x, new_y, x3, y3):
                        knight_pos.append((new_x, new_y, new_bishop_exist))
                        knight_visited_with_bishop.add((new_x, new_y))
                    if not new_bishop_exist and (new_x, new_y) not in knight_visited_without_bishop:
                        knight_pos.append((new_x, new_y, new_bishop_exist))
                        knight_visited_without_bishop.add((new_x, new_y))
        return -1

a = Solution()
ans = a.min_step(0, 0, 4, 3, 3, 0, 5, 5)
print(ans)