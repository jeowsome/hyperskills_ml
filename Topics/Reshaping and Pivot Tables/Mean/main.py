import pandas as pd

travel_log = {'country': {0: 'United Kingdom', 1: 'Germany', 2: 'Czech Republic', 3: 'Georgia', 4: 'Netherlands', 5: 'Greece', 6: 'Spain', 7: 'Germany', 8: 'Czech Republic', 9: 'Georgia', 10: 'Netherlands', 11: 'Greece', 12: 'United Kingdom', 13: 'Germany', 14: 'Czech Republic', 15: 'Netherlands', 16: 'Greece', 17: 'Spain', 18: 'United Kingdom', 19: 'Germany', 20: 'Czech Republic', 21: 'Georgia', 22: 'Netherlands', 23: 'United Kingdom', 24: 'Germany', 25: 'Czech Republic', 26: 'Georgia', 27: 'Netherlands', 28: 'Greece', 29: 'Spain', 30: 'Czech Republic', 31: 'Georgia', 32: 'Netherlands', 33: 'Greece', 34: 'Spain', 35: 'Germany', 36: 'Georgia', 37: 'Netherlands', 38: 'Greece', 39: 'Spain'}, 'main_goal': {0: 'cuisine tasting', 1: 'part-time job', 2: 'music festival', 3: 'snowboarding', 4: 'sightseeing', 5: 'street photography', 6: 'chilling', 7: 'cuisine tasting', 8: 'part-time job', 9: 'music festival', 10: 'snowboarding', 11: 'sightseeing', 12: 'street photography', 13: 'chilling', 14: 'cuisine tasting', 15: 'music festival', 16: 'snowboarding', 17: 'sightseeing', 18: 'sightseeing', 19: 'street photography', 20: 'chilling', 21: 'cuisine tasting', 22: 'part-time job', 23: 'snowboarding', 24: 'sightseeing', 25: 'street photography', 26: 'chilling', 27: 'cuisine tasting', 28: 'part-time job', 29: 'music festival', 30: 'sightseeing', 31: 'street photography', 32: 'chilling', 33: 'cuisine tasting', 34: 'part-time job', 35: 'music festival', 36: 'sightseeing', 37: 'street photography', 38: 'chilling', 39: 'cuisine tasting'}, 'duration_of_stay': {0: 5, 1: 15, 2: 2, 3: 14, 4: 19, 5: 3, 6: 7, 7: 4, 8: 7, 9: 6, 10: 13, 11: 17, 12: 8, 13: 14, 14: 11, 15: 10, 16: 12, 17: 13, 18: 2, 19: 8, 20: 17, 21: 19, 22: 31, 23: 4, 24: 6, 25: 11, 26: 13, 27: 4, 28: 7, 29: 5, 30: 3, 31: 6, 32: 4, 33: 3, 34: 10, 35: 4, 36: 7, 37: 11, 38: 2, 39: 6}}

df = pd.DataFrame(travel_log)
