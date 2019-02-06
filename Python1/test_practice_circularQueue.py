from circularQueue import *

if __name__ == '__main__':

    print("##### Test 1. Circular Queue #######")
    cg = CircularQueue(10)
    cg.enqueue(Person("Apple", 24))
    cg.enqueue(Person("Banna", 29))
    cg.enqueue(Person("Cutie", 21))
    cg.enqueue(Person("Daddy", 24))
    cg.enqueue(Person("Elf", 26))
    cg.enqueue(Person("Fruit", 31))
    cg.enqueue(Person("Goo", 29))
    cg.enqueue(Person("Hanna", 22))
    cg.enqueue(Person("Ivy", 24))
    person1 = cg.dequeue()
    person2 = cg.dequeue()
    cg.enqueue(Person("John", 26))
    cg.enqueue(Person("Kang", 28))
    person3 = cg.dequeue()
    peek1 = cg.peek()
    person_list = cg.multi_dequeue(3)

    print("Show Dequeue Names: ")
    print(person1)
    print(person2)
    print(person3)

    print("\nAdd "+person1.name+" age with "+person2.name+" age:")
    print(person1 + person2)

    print('\nAdd ages:')
    if peek1 > person3:
        print(peek1.name + " is older than " + person.name)
    else:
        print(person3.name + "is older than " + peek1.name)

    print("")
    print(person_list)
    print()

    print("##### Test 1. Circular Queue #######")
    cg CircularQueue(10)
    cg.enqueue("This is a String not a Person Class")
    cg.enqueue(Person("Mr A", 62))
    print(cg.dequeue())
    cg.enqueue(Person("Mr B", 49))
    print(cg.dequeue())
    cg.enqueue(Person("Mr C", 51))
    print(cg.dequeue())
    cg.enqueue(Person("Mr D", 68))
    print(cg.multi_dequeue(1))
    cg.enqueue(Person("Mr E", 55))
    print(cg.multi_dequeue(1))
    cg.enqueue(Person("Mr F", 44))
    print(cg.multi_dequeue(1))

    print("Queue Front: " + str(cg.front) + " Rear: " + str(cg.rear) )
    print()