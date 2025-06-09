
class Counter_A8:
    object_count = 0 

    def __init__(self):
        Counter_A8.object_count += 1
        print(f"Counter object created. Total objects: {Counter_A8.object_count}")

    @classmethod
    def get_total_objects(cls):
        print(f"Total number of Counter objects created: {cls.object_count}")


print("Creating Counter objects...")
c1_a8 = Counter_A8()
c2_a8 = Counter_A8()
c3_a8 = Counter_A8()

Counter_A8.get_total_objects()