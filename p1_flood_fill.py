class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
            TIme Complexity: O(m)
            Space Complexity: O(n)
            Approach:
                - we apply simple bfs over here
                - if the neighboring elements have value equal to current element 
                then append it to the queue and change the value of the neighboring 
                element to the color we want
                - once the queue is zero
                - return the image
        """
        st_cl = image[sr][sc]
        m = len(image)
        n = len(image[0])
        q = [[sr,sc]]
        image[sr][sc] = color
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        count = 0
        while (len(q) > 0):
            size = len(q)
            for i in range(0, size):
                flood = q.pop(0)
                for dir in dirs:
                    r = flood[0] + dir[0]
                    c = flood[1] + dir[1]
                    if r >= 0 and c >= 0 and r < m and c < n and image[r][c] == st_cl:
                        q.append([r, c])
                        image[r][c] = color
            if count >= 4:
                break
            count +=1
        return image