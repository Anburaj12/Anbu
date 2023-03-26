from functools import reduce
def function(car_models):
    a=[reduce(lambda a,x:x,i.split()) for i in model]
    print("'",','.join(a),"'")
model = ["Honda Civic","Honda Accord","Toyota Camry",
          "Ford Fusion","Ford Escape","Nissan Escape"
    ,"Nissan Sentra","Hyundai Elantra"]
function(model)