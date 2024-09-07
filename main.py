# main.py

from cityu_pack.sub_class_pack.class_module import ClassModule
from cityu_pack.sub_func_pack.func_module import add, multiply

if __name__ == "__main__":
    # Using ClassModule
    class_module = ClassModule(global_init_param=1)
    print("ClassModule Add:", class_module.add(3, 5))
    print("ClassModule Multiply:", class_module.multiply(3, 5))
    
    # Using func_module functions
    print("Function Add:", add(3, 5))
    print("Function Multiply:", multiply(3, 5))
