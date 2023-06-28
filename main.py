class Node:
    def __init__(self, data):
        self.data = data#значение
        self.next = None#указатель на следующий элемент списка


class LinkedList:
    def __init__(self):#конструктор
        self.head = None

    def append(self, data):#функция добавления элементка в список
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def __str__(self):#функция преобразования списка в строку(для удобства, чтобы выводить функцией print)
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.data))
            current_node = current_node.next
        return ' -> '.join(nodes)


    def shaker_sort(self, verbose=False):#функция сортировки линейного списка шейкерным способом(вместе с итерациями)
      iteration = 1
      sorted = False
      while not sorted:
        sorted = True
        current = self.head
        while current.next is not None:
            if current.data > current.next.data:
                current.data, current.next.data = current.next.data, current.data
                sorted = False
            current = current.next
        if sorted:
            break
        current = current.next
        while current != self.head:
            prev = self.head
            while prev.next != current:
                prev = prev.next
            if prev is None and current.data < prev.data:
                prev.data, current.data = current.data, prev.data
                sorted = False
            current = prev
        if verbose:
            print(f"Итерация {iteration}: {self}")
            iteration += 1

if __name__ == '__main__':
    linked_list = LinkedList()#создаем список 

    n = int(input("Введите количество элементов которое хотите добавить в линейный список: "))#ввод размера списка 
    for _ in range(n):#цикл заполнения созданного списка
        print("Введите число ",_+1," = ",end=" ")
        num = int(input())#указываем элемент списка
        linked_list.append(num)#добавляем элемент в список

    print("Исходный список:")
    print(linked_list)#вывод списка на экран

    linked_list.shaker_sort(verbose=True)#сортировка списка шейкерным способом

    print("Отсортированный список:")
    print(linked_list)#вывод отсортированного списка 
