# import numpy as np
# import pandas as pd

# value1 = {
#     "ram" : 16,
#     "price" : 170000,
#     "Storage" : 1000,
#     "CPU_ranking" : 70,
#     "gpu_ram" : 8,
#     "screen_size" : 15.6,
#     "gpu_benchmark" : 175,
#     "ram_type_tokenized" : 6,
#     "screen_resolution":1440,
#     "battery_backup" : 4.5,
#     "weight" : 1.3
# }

# value2 = {
#     "ram" : 16,
#     "price" : 1_60_000,
#     "Storage" : 1000,
#     "CPU_ranking" : 60,
#     "gpu_ram" : 8,
#     "screen_size" : 16.0,
#     "gpu_benchmark" : 190,
#     "ram_type_tokenized" : 6,
#     "screen_resolution":1440,
#     "battery_backup" : 1.0,
#     "weight" : 2.5
# }

# lis = {1:value1,2:value2}

# returns dict in a sorted order decreasing order of the score

class Gaming:
    
    def casual_gamer(self,data):
        scores = []
        
        self.max_price = max(data.values(), key=lambda x: x.get("price", 0)).get("price", 0)
        
        for value in data.values():
            scores.append(self.__casual_game_score(value))
            
        tuple_list = [(key, value, score) for key, value, score in zip(data.keys(), data.values(), scores)]
        sorted_tuples = sorted(tuple_list, key=lambda x: x[2], reverse=True)
        sorted_data = {key: value for key, value, _ in sorted_tuples}
        
        return sorted_data
        # return 1
    
    def heavy_gamer(self,data):
        
        scores = []
        
        self.max_price = max(data.values(), key=lambda x: x.get("price", 0)).get("price", 0)
        
        for value in data.values():
            scores.append(self.__heavy_game_score(value))
            
        tuple_list = [(key, value, score) for key, value, score in zip(data.keys(), data.values(), scores)]
        sorted_tuples = sorted(tuple_list, key=lambda x: x[2], reverse=True)
        sorted_data = {key: value for key, value, _ in sorted_tuples}
        
        return sorted_data
    
    
    def __casual_game_score(self,value:dict)->float:
        
        ram_weights = {32:0.8, 16:1.0,  4:0.4,  8:0.6}
        ram_normalised = ram_weights.get(value["ram"],0)
        
        max_price = self.max_price
        
        price_normalised = 1 - value["price"]/max_price
        
        storage_weights = {1000:1.0,  512:0.6, 1024:0.8, 1512:0.6,  516:0.6, 2000:0.4, 1256:0.6}
        storage_normalised = storage_weights.get(value["Storage"],0)
        
        screen_weights = {1440:0.8, 1080:1.0, 2160:0.6,  720 : 0.8}
        screen_normalised = screen_weights.get(value["screen_resolution"],0)
        
        
        cpu_ranking_normalised = 1 - value["CPU_ranking"]/342
            
        gpu_ram_weights = {8 : 0.6,  4 : 0.8,  6 : 1.0,  0 : 0.2, 16 : 0.6, 10 : 0.7, 12 : 0.7}
        gpu_ram_normalised = gpu_ram_weights.get(value["gpu_ram"],0) 

        screen_size_normalised = value["screen_size"]/18.0
        
        gpu_score_normalised = value["gpu_benchmark"]/233.0
        
        ram_type_weights = {7 : 0.6, 6 : 1.0, 4 : 0.8}
        ram_type_normalised = ram_type_weights.get(value["ram_type_tokenized"],0)
        
        
        score = ((ram_normalised * 7) + (price_normalised*10) + (storage_normalised * 6) + (screen_normalised * 7) + 
                    + (cpu_ranking_normalised * 7) + (gpu_ram_normalised * 5) + (screen_size_normalised * 5) + (gpu_score_normalised * 8)
                    + (ram_type_normalised*5))
        
        return (score/6)

    
    def __heavy_game_score(self,value:dict)->float:
        
        ram_weights = {32:1.0, 16:0.8,  4:0.3,  8:0.5}
        ram_normalised = ram_weights.get(value["ram"],0)
        
        max_price = self.max_price
        
        price_normalised = 1 - value["price"]/max_price
        
        storage_weights = {1000:0.7,  512:0.4, 1024:0.7, 1512:1.0,  516:0.4, 2000:0.8, 1256:0.8}
        storage_normalised = storage_weights.get(value["Storage"],0)
        
        screen_weights = {1440:1.0, 1080:0.7, 2160:0.8,  720 : 0.6}
        screen_normalised = screen_weights.get(value["screen_resolution"],0)
        
        cpu_ranking_normalised = 1 - value["CPU_ranking"]/342
    
        gpu_ram_weights = {8 : 0.8,  4 : 0.4,  6 : 0.6,  0 : 0.2, 16 : 0.8, 10 : 0.9, 12 : 1.0}
        gpu_ram_normalised = gpu_ram_weights.get(value["gpu_ram"],0) 

        screen_size_normalised = value["screen_size"]/18.0
        
        gpu_score_normalised = value["gpu_benchmark"]/233.0
        
        ram_type_weights = {7 : 0.9, 6 : 1.0, 4 : 0.4}
        ram_type_normalised = ram_type_weights.get(value["ram_type_tokenized"],0)
        
        
        score = ((ram_normalised * 6) + (price_normalised*6) + (storage_normalised * 6) + (screen_normalised * 7) + 
                    + (cpu_ranking_normalised * 9) + (gpu_ram_normalised * 5) + (screen_size_normalised * 6) + (gpu_score_normalised * 9)
                    + (ram_type_normalised*6))
        
        return (score/6)

class Student:
    
    def light_student(self,data):
        scores = []
        
        self.max_price = max(data.values(), key=lambda x: x.get("price", 0)).get("price", 0)
        
        for value in data.values():
            scores.append(self.__light_student_score(value))
            
        tuple_list = [(key, value, score) for key, value, score in zip(data.keys(), data.values(), scores)]
        sorted_tuples = sorted(tuple_list, key=lambda x: x[2], reverse=True)
        sorted_data = {key: value for key, value, _ in sorted_tuples}
        
        return sorted_data
    
    def medium_student(self,data):
        scores = []
        
        self.max_price = max(data.values(), key=lambda x: x.get("price", 0)).get("price", 0)
        
        for value in data.values():
            scores.append(self.__medium_student_score(value))
            
        tuple_list = [(key, value, score) for key, value, score in zip(data.keys(), data.values(), scores)]
        sorted_tuples = sorted(tuple_list, key=lambda x: x[2], reverse=True)
        sorted_data = {key: value for key, value, _ in sorted_tuples}
        
        return sorted_data
    
    def heavy_student(self,data):
        scores = []
        
        self.max_price = max(data.values(), key=lambda x: x.get("price", 0)).get("price", 0)
        
        for value in data.values():
            scores.append(self.__heavy_student_score(value))
            
        tuple_list = [(key, value, score) for key, value, score in zip(data.keys(), data.values(), scores)]
        sorted_tuples = sorted(tuple_list, key=lambda x: x[2], reverse=True)
        sorted_data = {key: value for key, value, _ in sorted_tuples}
        
        return sorted_data

    
    def __light_student_score(self,value:dict)->float:
        
        ram_weights = {16:0.4,  4:1.0,  8:0.8}
        ram_normalised = ram_weights.get(value["ram"],0)

        
        max_price = self.max_price
        
        price_normalised = 1 - value["price"]/max_price
        
        storage_weights = {1000:0.3,  512:1.0, 1024:0.3, 1512:0.2,  516:0.6, 2000:0.1, 1256:0.2,256:1.0,128:0.7,64:0.6,32:0.1}
        storage_normalised = storage_weights.get(value["Storage"],0)
        
        screen_weights = {1440:0.6, 1080:1.0, 2160:0.3,  720 : 0.8}
        screen_normalised = screen_weights.get(value["screen_resolution"],0)
        
        cpu_ranking_normalised = 1 - value["CPU_ranking"]/907
            
        # gpu_ram_weights = {8 : 0.1,  4 : 0.3,  6 : 0.2,  0 : 1.0, 16 : 0.1, 10 : 0.2, 12 : 0.1}
        # gpu_ram_normalised = gpu_ram_weights[value["gpu_ram"]] 
        
        screen_size_normalised = 1 - value["screen_size"]/18.0
        
        gpu_score_normalised = value["gpu_benchmark"]/102.0
        
        ram_type_weights = {2 : 0.6, 4 : 0.8,5 : 1.0,6 : 0.6,8 : 0.2}
        ram_type_normalised = ram_type_weights.get(value["ram_type_tokenized"],0)
        
        weight_normalised = 1 - value["weight"]/2.5
        
        battery_normalised = value["battery_backup"]/5.0
        
        score = ((ram_normalised * 7) + (price_normalised*10) + (storage_normalised * 7) + (screen_normalised * 5) + 
                    + (cpu_ranking_normalised * 6) + (screen_size_normalised * 5)
                    + (ram_type_normalised*6) + (weight_normalised*7) + (gpu_score_normalised * 3) + (battery_normalised*4))
        
        return (score/6)
    
    def __medium_student_score(self,value:dict)->float:
        
        ram_weights = {16:0.8,  4:0.2,  8:1.0}
        ram_normalised = ram_weights.get(value["ram"],0)
        
        max_price = self.max_price
        
        price_normalised = 1 - value["price"]/max_price
        
        storage_weights = {1000:0.8,  512:1.0, 1024:0.8, 1512:0.6,  516:1.0, 2000:0.3, 1256:0.2,256:0.4,128:0.2,64:0.1}
        storage_normalised = storage_weights.get(value["Storage"],0)
        
        screen_weights = {1440:0.8, 1080:1.0, 2160:0.6,  720 : 0.4}
        screen_normalised = screen_weights.get(value["screen_resolution"],0)
        
        cpu_ranking_normalised = 1 - value["CPU_ranking"]/907
            
        # gpu_ram_weights = {8 : 0.1,  4 : 0.3,  6 : 0.2,  0 : 1.0, 16 : 0.1, 10 : 0.2, 12 : 0.1}
        # gpu_ram_normalised = gpu_ram_weights[value["gpu_ram"]] 
        
        screen_size_normalised = 1 - value["screen_size"]/18.0
        
        gpu_score_normalised = value["gpu_benchmark"]/102.0
        
        ram_type_weights = {2 : 0.3, 4 : 0.6,5 : 1.0,6 : 1.0,8 : 0.4}
        ram_type_normalised = ram_type_weights.get(value["ram_type_tokenized"],0)
        
        weight_normalised = 1 - value["weight"]/2.5
        
        battery_normalised = value["battery_backup"]/5.0
        
        score = ((ram_normalised * 7) + (price_normalised*9) + (storage_normalised * 7) + (screen_normalised * 6) + 
                    + (cpu_ranking_normalised * 8) + (screen_size_normalised * 7)
                    + (ram_type_normalised*6) + (weight_normalised*7) + (gpu_score_normalised * 7) + (battery_normalised*6))
        
        return (score/7)

    def __heavy_student_score(self,value:dict)->float:
        
        ram_weights = {16:1.0,  4:0.2,  8:0.8}
        ram_normalised = ram_weights.get(value["ram"],0)

        max_price = self.max_price
        
        price_normalised = 1 - value["price"]/max_price
        
        storage_weights = {1000:0.7,  512:0.5, 1024:0.7, 1512:1.0,  516:0.5, 2000:0.7, 1256:0.8,256:0.4,128:0.3,64:0.2}
        storage_normalised = storage_weights.get(value["Storage"],0)
        
        screen_weights = {1440:1.0, 1080:0.8, 2160:0.8,  720 : 0.5}
        screen_normalised = screen_weights.get(value["screen_resolution"],0)
        
        cpu_ranking_normalised = 1 - value["CPU_ranking"]/907
            
        gpu_ram_weights = {2 : 0.8,4:1.0}
        gpu_ram_normalised = gpu_ram_weights.get(value["gpu_ram"],0) 
        
        screen_size_normalised = 1 - value["screen_size"]/18.0
        
        gpu_score_normalised = value["gpu_benchmark"]/102.0
        
        ram_type_weights = {2 : 0.2, 4 : 0.4,5 : 0.6,6 : 0.8,8 : 1.0}
        ram_type_normalised = ram_type_weights.get(value["ram_type_tokenized"],0)
        
        weight_normalised = 1 - value["weight"]/2.5
        
        battery_normalised = value["battery_backup"]/5.0
        
        
        score = ((ram_normalised * 8) + (price_normalised*8) + (storage_normalised * 7) + (screen_normalised * 6) + 
                    + (cpu_ranking_normalised * 8) + (screen_size_normalised * 4)
                    + (ram_type_normalised*6) + (weight_normalised*5) + (gpu_score_normalised * 8) 
                    + (gpu_ram_normalised * 5) + (battery_normalised*5))
        
        return (score/7)


class Business:
    
    def business(self,data):
        scores = []
        
        self.max_price = max(data.values(), key=lambda x: x.get("price", 0)).get("price", 0)
        
        for value in data.values():
            scores.append(self.__business_score(value))
            
        tuple_list = [(key, value, score) for key, value, score in zip(data.keys(), data.values(), scores)]
        sorted_tuples = sorted(tuple_list, key=lambda x: x[2], reverse=True)
        sorted_data = {key: value for key, value, _ in sorted_tuples}
        
        return sorted_data
    
    def __business_score(self,value:dict)->float:
        
        ram_weights = {16:1.0,  4:0.2,  8:0.8}
        ram_normalised = ram_weights.get(value["ram"],0)

        max_price = self.max_price
        
        price_normalised = 1 - value["price"]/max_price
        
        storage_weights = {1000:0.7,  512:0.5, 1024:0.7, 1512:1.0,  516:0.5, 2000:0.7, 1256:0.8,256:0.4,128:0.3,64:0.2}
        storage_normalised = storage_weights.get(value["Storage"],0)
        
        screen_weights = {1440:1.0, 1080:0.8, 2160:0.8,  720 : 0.5}
        screen_normalised = screen_weights.get(value["screen_resolution"],0)
        
        cpu_ranking_normalised = 1 - value["CPU_ranking"]/907
            
        # gpu_ram_weights = {2 : 0.8,4:1.0}
        # gpu_ram_normalised = gpu_ram_weights.get(value["gpu_ram"],0) 
        
        screen_size_normalised = 1 - value["screen_size"]/18.0
        
        # gpu_score_normalised = value["gpu_benchmark"]/102.0
        
        # ram_type_weights = {2 : 0.2, 4 : 0.4,5 : 0.6,6 : 0.8,8 : 1.0}
        # ram_type_normalised = ram_type_weights.get(value["ram_type_tokenized"],0)
        
        weight_normalised = 1 - value["weight"]/2.5
        
        battery_normalised = value["battery_backup"]/5.0
        
        score = ((ram_normalised * 7) + (price_normalised*6) + (storage_normalised * 6) + (screen_normalised * 8) + 
                    + (cpu_ranking_normalised * 4) + (screen_size_normalised * 6)
                     + (weight_normalised*11) + (battery_normalised*12))
        
        return (score/6)

# obj = Business()
# lis = obj.business(lis)
# print(lis)       