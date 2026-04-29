class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", 
                "Thursday", "Friday", "Saturday"]
        
      
        days_in_month = [31, 28, 31, 30, 31, 30, 
                         31, 31, 30, 31, 30, 31]
        
      
        def is_leap(y):
            return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
        
        total_days = 0
        
        for y in range(1971, year):
            total_days += 366 if is_leap(y) else 365
        
        
        for m in range(1, month):
            if m == 2 and is_leap(year):
                total_days += 29
            else:
                total_days += days_in_month[m - 1]
        
    
        total_days += day
        
        return week[(total_days + 4) % 7]