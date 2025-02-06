from django.shortcuts import render
from django.http import JsonResponse
from htmlcss.models import Laptop
from htmlcss.greedy import Student,Gaming,Business
import json
from pathlib import Path
# Create your views here.

def home(request):
    # if request.method=='POST':
    # data= JsonResponse.json.load(request)['user_specs']
    
    directory = Path(r"D:\dell_hackathon\BuyFair\DFF\mysite\user_inputs")

    json_files = list(directory.glob("user-data(*).json"))

    if json_files:
        json_files.sort(key=lambda file: int(file.stem.replace("user-data(", "").replace(")", "")))

        highest_number_json = json_files[-1]
        with open(highest_number_json, "r") as file:
            data = json.load(file)
    
    # data = {}
    
    # try:
        # with open(json_file_path, 'r') as json_file:
            # data = json.load(json_file)
        
        primary= int(data['primary_profile']) #gsb
        if primary != 2:
            secondary=int(data['secondary_profile']) #gs
            exp=int(data['expandable_memory']) #gs
            
        resolution=int(data['resolution']) #gsb
        if primary != 1:
            proc=int(data['processor']) #gb
        if primary == 0:
            graphics=int(data['graphics']) #g
            os = 1
        if primary != 0:
            os= int(data['os']) #sb
        touch=int(data['touch']) #gsb
        
        laptop_type_dict = {0 : 1,1 : 2,2 : 2}
        laptop_type = laptop_type_dict.get(primary,2)
        
        price_dict = {0 : 50_000, 1 : 1_00_000, 2 : 1_50_000,3 : 2_00_000,4:3_00_000}
        price=price_dict.get(int(data["price"]),1_00_000)
        
        gpu_brand_dict = {0:"nvidia",1:"amd"}
        if primary == 0:
            gpu_brand = gpu_brand_dict.get(graphics,"nvidia")
        
        company_dict = {1 : "asus",2:"hp",3 : "lenovo",4:"dell",5:"msi",6:"realme",7 : "avita", 8 : "acer",9 : "samsung",10 : "infinix",11 : "lg",12 : "apple",13 : "nokia",14 : "redmi",15 : "mi",16 : "vaio"}
        
        laptopdb=Laptop.objects.all()
        
        
        laptopdb = laptopdb.filter(price__lte=price)
        
        if primary != 0:
            laptopdb = laptopdb.filter(os=os)
        
        
        if os != 4:    
            
            if primary == 1 and secondary ==1:
                laptopdb = laptopdb.filter(type=1)
            else:
                laptopdb = laptopdb.filter(type=laptop_type)
            
            if primary != 1:
                laptopdb = laptopdb.filter(processor=proc)
            if primary == 0:
                laptopdb = laptopdb.filter(gpu_name__icontains = gpu_brand)
            laptopdb = laptopdb.filter(sr=resolution)
            if primary != 2:
                laptopdb = laptopdb.filter(expand=exp)
            laptopdb = laptopdb.filter(ts=touch)
        
        data_dict = {}
        i = 0
        for laptop in laptopdb:
            data_dict[i] = {
                            "ram" : laptop.ram_gb,
                            "price" : laptop.price,
                            "Storage" : laptop.storage,
                            "CPU_ranking" : laptop.cpu,
                            "gpu_ram" : laptop.dedicated,
                            "screen_size" : laptop.screen_size,
                            "gpu_benchmark" : laptop.gpu_bench,
                            "ram_type_tokenized" : laptop.ram_typetokenized,
                            "screen_resolution" : laptop.sr,
                            "battery_backup" : laptop.bat_bac,
                            "weight" : laptop.weight,
                            "name":laptop.name,
                            "link" : laptop.link,
                            "gpu_name" : laptop.gpu_name,
                            "processor_name" : laptop.pro_name,
                            "storage_type" : laptop.ssd,
                            "ram_type" : laptop.ram_type,
                            "expandable_memory" : laptop.expand,
                            "laptop_brand" : company_dict.get(laptop.com,"unknown")
                            }
            i+=1
            
        

        if len(data_dict) < 6 and os != 4:
            extra=Laptop.objects.all()
            extra = extra.filter(price__lte=price)
            # extra = extra.filter(type = laptop_type)
            if primary == 1 and secondary ==1:
                extra = extra.filter(type=1)
            else:
                extra = extra.filter(type=laptop_type)
            i = len(data_dict)
            
            for laptop in extra:
                data_dict[i] = {
                                "ram" : laptop.ram_gb,
                                "price" : laptop.price,
                                "Storage" : laptop.storage,
                                "CPU_ranking" : laptop.cpu,
                                "gpu_ram" : laptop.dedicated,
                                "screen_size" : laptop.screen_size,
                                "gpu_benchmark" : laptop.gpu_bench,
                                "ram_type_tokenized" : laptop.ram_typetokenized,
                                "screen_resolution" : laptop.sr,
                                "battery_backup" : laptop.bat_bac,
                                "weight" : laptop.weight,
                                "name":laptop.name,
                                "link" : laptop.link,
                                "gpu_name" : laptop.gpu_name,
                                "processor_name" : laptop.pro_name,
                                "storage_type" : laptop.ssd,
                                "ram_type" : laptop.ram_type,
                                "expandable_memory" : laptop.expand,
                                "laptop_brand" : company_dict.get(laptop.com,"unknown")
                                }
                i+=1
                if i == 6:
                    break
                
        
        if primary == 0:
            object = Gaming()
            if secondary == 0:
                data_dict = object.casual_gamer(data_dict)
            elif secondary == 1:
                data_dict = object.heavy_gamer(data_dict)
        elif primary == 1:
            object = Student()
            if secondary == 0:
                data_dict = object.light_student(data_dict)
            elif secondary == 1:
                data_dict = object.heavy_student(data_dict)
        elif primary == 2:
            object = Business()
            data_dict = object.business(data_dict)
            
        top = data_dict[0]
        other_5 = dict(list(data_dict.items())[1:6])
        
        return render(request,'sample.html',{"laptopdb":other_5,"top":top})
        
            
    # except FileNotFoundError:
    #     print("too bad")
    # except json.JSONDecodeError as e:
    #     print("Too bad you got this thing "+e)

def index(request):
    return render(request,'index.html')