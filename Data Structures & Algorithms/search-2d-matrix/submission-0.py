class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Use binary search to find column, then use binary seaach to find row.
        
        n = len(matrix) # Rows
        m = len(matrix[0]) # Columns

        x = 0
        y = len(matrix[0]) - 1

        c_r = -1

        l_r = 0
        r_r = n - 1

        while l_r <= r_r:
            m_r = (l_r + r_r) // 2
            print("m_r: " + str(m_r))
            
            if (matrix[m_r][x] > target):
                r_r = m_r - 1

            elif (matrix[m_r][y] < target):
                l_r = m_r + 1

            else:
                print("here")
                c_r = m_r
                break
        
        print(c_r)
        if c_r == -1:
            return False

        else:
            l = 0
            r = m - 1

            while l <= r:
                m = (l + r) // 2
                print("m: " + str(m))

                if (matrix[c_r][m]) < target:
                    l = m + 1

                elif (matrix[c_r][m] > target):
                    r = m - 1

                else: 
                    return True
        
        return False









