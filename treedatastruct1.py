import sys
import os
import datetime
from playsound import playsound
import emoji 
from csv import writer

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor
    
    return elements
   
def build_tree(elements):
    root1 = BinarySearchTreeNode(elements[0]) 
    for i in range(1,len(elements)):
        root1.add_child(elements[i])
    return root1

def build_tree1(elements1):

    root2 = BinarySearchTreeNode(elements1[0])
    
    for i in range(1,len(elements1)):
        root2.add_child(elements1[i])

    return root2


def goodstk():
    fileObj = open("StockList.txt", "r") #opens the file in read mode
    words = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    product = words
    product_tree = build_tree1(product)
    print("GOOD STOCK PORTAL")
    print("\n 1.Add Product \n 2.Open Stock Report \n 3.Search a product \n 4.Sort the Stock \n 5.Remove a Stock \n 6.Stock Analysis \n 7. Back ")
   
    choice = int(input("Enter your choice: "))
    if(choice == 2):
        listToStr = '\n'.join([str(elem) for elem in words])
        print(listToStr)
        print("")
        goodstk()
        
    elif(choice == 3):
        data = input("Enter Product Name: ")
        res = product_tree.search(data)
        if res == True:
            print("Stock Present")
        else:
            print("Stock not available for that SKU")
        goodstk() 
        
    elif(choice == 4):
        print("Sorting the Whole tree using Insertion Sort")
        tree2_insertion=insertion_sort(words)
        listToStr1 = '\n'.join([str(elem) for elem in tree2_insertion])
        print(listToStr1)
        print("\n")
        goodstk()
        
    elif(choice == 5):
        deleteitem = input("Enter SKU to remove: ")
        product_tree.delete(deleteitem)
        print("List updated")
        tree2delete = product_tree.in_order_traversal()
        listToStr1 = '\n'.join([str(elem) for elem in tree2delete])
        print(listToStr1)

        with open("StockList.txt", "r") as f:
            data = f.readlines()
        with open("StockList.txt", "a") as f:
            for line in data :
            		if line.strip("\n") != deleteitem :
        		       f.write(line)
        goodstk()

    elif(choice == 6):
        sorted =  product_tree.in_order_traversal()
        least = sorted[1]
        print("\nFresh Dated Stock: ",product_tree.find_max())
        print("Early Dated Stock: ",least)
        print("\nExpiry Stock Analysis for fresh dated stock")
        leaststock = product_tree.find_max()
        my = int(datetime.datetime.now().month) #6
        dm = leaststock.split("/")
        dm1 = least.split("/")#1
        res = [dm[0]]
        res1 = [dm1[0]]
        stockage = ('\n'.join([str(elem) for elem in res1]))
        stk = int(stockage)
        stockdetails = int(my-stk)
        if (stockdetails) >= 6:
                print(least,"Stock Expired")
                fname = 'StockList.txt'
                f = open(fname)
                output = []
                for line in f:
                    if not least in line:
                        output.append(line)
                f.close()
                f = open(fname, 'w')
                f.writelines(output)
                f.close()
                remember = open("Expiry.txt","a")
                remember.write("\n")
                remember.write(least)
                remember.close()
        elif stockdetails < 0:
                print(least,"Stock Expired")
                f = open(fname)
                output = []
                for line in f:
                    if not least in line:
                        output.append(line)
                f.close()
                f = open(fname, 'w')
                f.writelines(output)
                f.close()
                remember = open("Expiry.txt","a")
                remember.write(least)
                remember.close()
        else:
            print("Stock Good",6- stockdetails," months to expire")
        goodstk()
        
    elif(choice == 7):
        mainmenu()
    
    elif(choice == 1):

        productt = input("Enter Manufacturing Date of Product(mm/yyyy): ")
        namee = input("Enter Name of Product: ")
        fin_pro = productt+" "+namee
        root1 = BinarySearchTreeNode(fin_pro)
        root1.add_child(fin_pro)
        remember = open("StockList.txt","a")
        remember.write("\n")
        remember.write(fin_pro)
        remember.close()
        print("Product Added")
        List=[fin_pro]
        with open('data.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(List)
            f_object.close()
        goodstk()
        
    else:
        goodstk()
        print("Enter Correct Choice")
        
        
def expstk():
    fileObj = open("Expiry.txt", "r") #opens the file in read mode
    exp = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    expiryy = exp
    expiry_tree = build_tree(expiryy)
        
    print("\nEXPIRY STOCK PORTAL")
    print("\n 1. Print Stock \n 2.Sort Expiry Stock \n 3.Search SKU \n 4.Back")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        listToStr = '\n'.join([str(elem) for elem in exp])
        print(listToStr)
        print("")
        expstk()
    elif(choice == 2):
        print("Sorting the Whole tree using Insertion Sort")
        tree2_insertion=insertion_sort(expiryy)
        listToStr1 = '\n'.join([str(elem) for elem in tree2_insertion])
        print(listToStr1)
        print("\n")
        expstk()
    elif(choice == 3):
        data = input("Enter SKU Name: ")
        res = expiry_tree.search(data)
        if res == True:
            print("Stock Present")
        else:
            print("Stock not available for that SKU")
        expstk()
    elif(choice == 4):
        mainmenu()
        
        
def clstk():
         print("CLOSING STOCK PORTAL")
         fileObj = open("StockList.txt", "r") #opens the file in read mode
         words = fileObj.read().splitlines() #puts the file into an array
         fileObj.close()
         product = words
         fileObj = open("Expiry.txt", "r") #opens the file in read mode
         exp = fileObj.read().splitlines() #puts the file into an array
         fileObj.close()
         expiryy = exp
         print("\nClosing Stock Report")
         tree2_insertion=insertion_sort(expiryy)
         listToStr1 = '\n'.join([str(elem) for elem in tree2_insertion])
         print(listToStr1)
         tree2_insertion=insertion_sort(product)
         listToStr1 = "\n".join([str(elem) for elem in tree2_insertion])
         print(listToStr1)

        
        
def mainmenu():
    print("HOME ")
    print(" 1.Good Stock Portal \n 2.Expiry Stock Portal \n 3.Closing Stock Report \n 4.Exit")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        goodstk()
    elif(choice == 2):
        expstk()
    elif(choice == 3):
        clstk()
    elif(choice == 4):
        print("              Application closed                ")
        print("************************************************")
        sys.exit()
    else:
        print("Input error")
        mainmenu()
        
        
print("************************************************")
print("*------------INVENTORY MANAGEMENT--------------*")
print("*          MAVERICKS SUPERSTOCKISTS            *")
print("*       STOCK MANAGEMENT FOR ALL NEEDS         *")
print("************************************************")
playsound("britannia.mp3")

    
while True:
    os.system('cls')
    mainmenu()
