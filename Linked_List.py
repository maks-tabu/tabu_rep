#!/usr/bin/env python
# coding: utf-8

# ### Методы класса LinkedList
# 
# $Add$ - добавляет элемент в конец списка.
# 
# $Remove$ - удаляет первый элемент списка со значением, равным переданному. Возвращает true, если элемент был удален и false в противном случае.
# 
# $Contains$ - возвращает true или false в зависимости от того, присутствует ли искомый элемент в списке.
# 
# $GetEnumerator$ - возвращает экземпляр IEnumerator, который позволяет итерироваться по элементам списка.
# 
# $Clear$ - удаляет все элементы из списка.
# 
# $CopyTo$ - копирует содержимое списка в указанный массив, начиная с указанного индекса.
# 
# $Count$ - возвращает количество элементов списка. Возвращает 0, если список пустой.
# 
# $IsReadOnly$ - возвращает true, если список только для чтения.

# In[1]:


from typing import TypeVar, Generic, List, Generator
T = TypeVar('T')


# In[48]:


class Node(Generic[T]):
    """Описание"""
    def __init__(self, value: int = None) -> None:
        self.value: int = value
        self.next_node(None)
        
    def next_node(self, node: T) -> None:
        self._next: T = node   


# In[339]:


class LinkedList():
    def __init__(self) -> None:
        self._firstN: Node = Node(None)
        self.__countN: int = 0
        self.__read_only: bool = False
    
    def _block(func):
        def wrapped(self, *args, **kwargs):
            if (self.__read_only == False):
                func(self, *args, **kwargs)
            else:
                print('Только для чтения')
        return wrapped

    @_block
    def add(self, val: int, ind: int = None) -> None:
        if (ind == None):
            ind = self.__countN
        if (self._firstN.value == None):
            self._firstN.value = val
        elif (ind == 0):
            newN = Node(val)
            newN.next_node(self._firstN)
            self._firstN = newN
        else:
            for activeN in self.getgenerator(ind):
                lastN = activeN
            newN = Node(val)
            if (ind < self.__countN):
                newN.next_node(lastN._next)
            lastN.next_node(newN)
        self.__countN += 1
    
    @_block
    def remove(self, delval: int) -> None:
        if (self._firstN.value == delval):
            self._firstN = self._firstN._next
            self.__countN -= 1
        else:
            for activeN in self.getgenerator():
                nextN = activeN._next
                if (nextN != None):
                    if (nextN.value == delval):
                        self.__countN -= 1
                        activeN.next_node(nextN._next)
                        break
                else:
                    print("No such number")
    
    def contains(self, val: int) -> bool:
        for activeN in self.getgenerator():
            if (activeN.value == val):
                return True
        return False        

    def getgenerator(self, end: int = None) -> Generator:
        if (end == None):
            end = self.__countN
        iterN = self._firstN
        for i in range(end):
            iternext = iterN._next
            yield iterN
            iterN = iternext 
    
    @_block
    def clear(self) -> None:
        self._firstN: Node = Node(None)  
        self.__countN = 0
                
    def copyto(self, inpList: List = [], ind: int = None) -> List:
        if (ind == None):
            ind = len(inpList)    
        if (ind > len(inpList)) or (ind < 0):
            raise AttributeError('Ошибка в указании индекса')
        if (ind == 0):    
            newList = []   
            aftrList = inpList
        elif (ind == len(inpList)):
            newList = inpList  
            aftrList = []
        else:
            newList = inpList[:ind]
            aftrList = inpList[ind:]               
        for activeN in self.getgenerator():
            newList.append(activeN.value)
        for el in aftrList:
            newList.append(el)
        return newList
    
    @_block
    def inverse(self) -> None:  
        bfrN = None
        activeN = self._firstN
        for i in range(self.__countN):
            aftrN = activeN._next
            activeN.next_node(bfrN)
            bfrN = activeN
            activeN = aftrN
        self._firstN = bfrN
            
    def count(self) -> int:
        return self.__countN
    
    def __repr__(self) -> str:
        out = []
        for activeN in self.getgenerator():
            out.append(str(activeN.value))
        return '\n'.join(out)
    
    def readonly(self, p: bool = None):
        if (p == None):
            self.__read_only = not self.__read_only 
        elif (type(p) == bool):
            self.__read_only = p
        else:
            print('Должен быть тип boolean')


# In[340]:


def makeLinkedList(list_val: List) -> LinkedList:
    _LL = LinkedList()   
    if (len(list_val) != 0):
        for elem in list_val:
            _LL.add(elem)
    return _LL       


# In[341]:


my_list: List = [1,2,3,4,5]
LL1: LinkedList = makeLinkedList(my_list)

