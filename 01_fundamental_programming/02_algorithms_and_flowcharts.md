
## **Understanding Algorithms and Flowcharts**  
### **Introduction:**  
An **algorithm** is a step-by-step set of instructions to solve a problem. Before we write code, we often use **flowcharts** to visually represent these steps. This makes it easier to understand and communicate the logic behind a solution.

### **Key Concepts:**  
1. **What is an algorithm?** – A set of well-defined instructions.  
2. **Flowchart symbols and their meanings.**  
3. **Decision making in algorithms (IF-ELSE conditions).**  
4. **Loops and repetition in algorithms.**  

### **Example:**  
**Algorithm for checking if a number is even or odd:**  
1. Start  
2. Input a number  
3. If the number is divisible by 2, print "Even"  
4. Else, print "Odd"  
5. End  

**Flowchart Representation:**  
🟢 **Start** → 🔷 **Input Number** → 🔲 **Check If Number % 2 == 0** → ⬜ "Even" / "Odd" → 🔴 **End**

## Questions
1. **What makes an algorithm efficient, and why does efficiency matter?**  

    A major criterion for a good algorithm is its efficiency. That is, how much time and memory are required to solve a particular problem.

2. **What are the key differences between an algorithm and a program?**  

    Algorithm - it is a well defined, systematic logical approach that comes with a step by step procedure for computers to solve any given program.

    Program - it refers to the code (written by programmers) for any program that follows the basic rules of the concerned programming language.

3. **How would you design an algorithm to find the shortest path between two locations?**  

    To find the shortest path between two locations, you can use an algorithm like Dijkstra's algorithm. The algorithm keeps track of the shortest distance from each node to the starting node. It updates these values if it finds a shorter path.

4. **Can you think of an everyday task that can be represented as an algorithm? How would you write it?**  

    Algorithm : Making a Cup of Coffee

    Inputs :
    - Coffee
    - Water
    - Milk (optional)
    - Sugar (optional)
    - Mug
    - Spoon

    Steps :
    1. Start
    2. Boil water
    3. Place a coffee mug on the table
    4. Add 1-2 teasponns of coffee into the mug
    5. (optional) Add sugar to taste
    6. Pour hot water into the mug
    7. Stir the mixture with a spoon
    8. (Optional) Add milk and stir again
    9. Let it cool slightly
    10. Enjoy your coffee
    11. End

5. **What are the main components of a flowchart, and how do they help in understanding algorithms?**  

    The main components of a flowchart are symbols, flowlines, and boxes. These components help in understanding algorithms by visually representing the steps in a process.

6. **Find two different flowcharts for sorting numbers and compare their effectiveness.**  

    1. Bubble Sort Flowchart

    Effectiveness :
    - Easy to understand & implement.
    - Inefficient for large datasets.
    - Slow compared to other sorting methods.

    2. Quick Sort Flowchart

    Effectiveness :
    - Fast for large datasets.
    - Efficient with memory.
    - More complex to implement than Bubble Sort.

7. **Why is decision-making (IF-ELSE conditions) important in algorithms?**  

    it helps your code make decisions based on data, making it responsice real-world situations.

8. **How would you modify a simple algorithm to handle unexpected errors or conditions?**  

    You can log relevant information about the error, such as the input data, the state of the system, and the traceback. Implementing try catch block or exception handling in your code can help manage errors gracefully, allowing the program to continue running or providing meaningful feedback to the user. Regularly reviewing and updating error handling strategies can also improve the robustness of your algorithm.

9. **What are the differences between linear and non-linear algorithms? Provide examples.**  

    in a linear data structure, the data elements connect to each other sequentially. A user can transverse each element through a single run. The examples of linear data structures such as list, array, stack, and queue

    while, in a non linear data structure, the data elements connect to each other hierarchically. Thus, they are present at various levels. The examples of non linear data structure such as map, graph, and tree

10. **How can flowcharts help in debugging and understanding software systems?**  

    Flowcharts aid in debugging and understanding software system by providing a visual representation of the logical flow of a program, allowing developers to easily trace the execution path, identify potential problem areas, and pinpoint where errors might be occuring within the code.