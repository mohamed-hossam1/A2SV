# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        counter_of_boomerangs = 0
        
        for point_1 in points:
            
            x1, y1 = point_1
            
            distance_count_dict = defaultdict( int )
            
            
            for point_2 in points:
                
                x2, y2 = point_2
                
                diff_x = x2-x1
                diff_y = y2-y1
                
                dist = diff_x ** 2 + diff_y ** 2
                
                distance_count_dict[ dist ] += 1
                
            
            for d in distance_count_dict:
                
                n = distance_count_dict[d]
                
                counter_of_boomerangs += n * (n-1)
                
        
        return counter_of_boomerangs