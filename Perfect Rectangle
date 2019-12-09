class Solution:
    def insertCorner(self, cornerMap, x, y, val):
        if (x, y) in cornerMap and cornerMap[(x, y)] & val:
            return False
        cornerMap[(x, y)] |= val
        return True
        
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        print(rectangles[0][0])
        print(rectangles[0][1])
        print(rectangles[0][2])
        print(rectangles[0][3])
        minx = maxx = rectangles[0][0]
        miny = maxy = rectangles[0][1]
        cornerMap = collections.defaultdict(int)
        for bx, by, tx, ty in rectangles:
            minx, maxx = min(minx, bx), max(maxx, tx)
            miny, maxy = min(miny, by), max(maxy, ty)
            if not self.insertCorner(cornerMap, bx, by, 1): return False
            if not self.insertCorner(cornerMap, tx, by, 2): return False
            if not self.insertCorner(cornerMap, bx, ty, 4): return False
            if not self.insertCorner(cornerMap, tx, ty, 8): return False
        validCorner = {1, 2, 4, 8}
        validInterior = {3, 5, 10, 12, 15}
        for x, y in cornerMap:
            if x in (minx, maxx) and y in (miny, maxy):
                if cornerMap[(x, y)] not in validCorner:
                    return False
            else:
                if cornerMap[(x, y)] not in validInterior:
                    return False
        return True
        
