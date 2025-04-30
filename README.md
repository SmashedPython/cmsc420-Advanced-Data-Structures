# 🌲 CMSC420: Advanced Data Structures

This repository contains Python implementations of several advanced data structures developed as part of **Advanced Data Structures**. These structures include both balanced trees and probabilistic or spatial partitioning structures, each optimized for specific tasks in efficient data organization and search.

---

## 📁 Data Structures Overview

### 1. 🔢 Binary Search Tree (BST) – [`bst/`]

**Concept:**  
A binary tree in which each node’s left subtree contains only nodes with keys less than the node’s key, and the right subtree only keys greater. Enables efficient search, insertion, and deletion with O(log n) average-case time complexity.

**Diagram:**
```
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```

**Implementation Highlights:**
- Recursive insert, search, and delete.
- Not self-balancing, so worst-case time is O(n).

---

### 2. 🌳 B-Tree – [`b tree/`]

**Concept:**  
A self-balancing multi-way search tree optimized for systems that read and write large blocks of data. Widely used in databases and filesystems.

**Diagram (B-tree of order 3):**
```
        [10 | 20]
       /   |   \
     [5] [15] [25 30]
```

**Implementation Highlights:**
- Nodes contain multiple keys and children.
- Automatically splits nodes during insertion.
- Maintains balance and shallow height.

---

### 3. 🧠 Scapegoat Tree – [`scapegoat tree/`]

**Concept:**  
A binary search tree that rebalances itself by rebuilding subtrees when balance is violated. It avoids rotations by restructuring entire subtrees when needed.

**Diagram (after insertion of 7):**
```
Insert 7 causes imbalance → rebuild:
        6
       / \
      3   9
     / \   \
    1   5   10
```

**Implementation Highlights:**
- Uses α-balance condition.
- Subtrees are rebuilt when out of balance.
- Amortized O(log n) time for insertions and deletions.

---

### 4. 🧵 Skip List – [`skip list/`]

**Concept:**  
A probabilistic data structure with multiple levels of sorted linked lists to achieve fast search, insertion, and deletion, similar to balanced trees.

**Diagram:**
```
Level 3:  ----> 20 ---------------->
Level 2:  ----> 20 ----> 40 ------->
Level 1:  10 -> 20 -> 30 -> 40 -> 50
```

**Implementation Highlights:**
- Randomized layer heights via coin flips.
- Average time complexity: O(log n).
- Simple alternative to red-black trees.

---

### 5. 🔍 K-D Tree – [`kd tree/`]

**Concept:**  
A binary tree used for organizing points in a k-dimensional space. Useful for range searches and nearest neighbor queries in 2D/3D applications.

**Diagram (2D k-d tree):**
```
       (30, 40)
       /      \
   (20, 10)   (40, 50)
    /             \
(10, 5)          (50, 30)
```

**Implementation Highlights:**
- Alternates splitting axis at each level.
- Supports efficient multidimensional queries.
- Used in computer vision, robotics, etc.

---

### 6. 🔗 Clustering – [`cluster/`]

**Concept:**  
Implements a basic unsupervised clustering algorithm (e.g., K-Means) that groups data points based on proximity in feature space.

**Diagram (K-Means Example):**
```
[●●] ← Cluster 1 (Red)
[○○○] ← Cluster 2 (Blue)
[▲▲▲] ← Cluster 3 (Green)
         ↓
   Centroids move until stable
```

**Implementation Highlights:**
- Random initialization of centroids.
- Iterative assignment and centroid update.
- Uses Euclidean distance for cluster matching.

---

## 🛠 How to Run

All code is written in **pure Python 3.7+** and requires **no external libraries**.

To test a structure:

```bash
cd "folder_name"
python your_script.py  # if provided
```

Each folder may contain:
- `.py` implementation file(s)
- (Optional) test or demo script
- In-code comments and documentation

---

## 🧠 Topics Covered

- Balanced Trees: Scapegoat Tree, B-Tree
- Probabilistic Structures: Skip List
- Multidimensional Structures: K-D Tree
- Classical Trees: Binary Search Tree
- Unsupervised Learning: Clustering Algorithms

---

## 📂 Folder Structure

```
cmsc420-Advanced-Data-Structures/
├── bst/                 # Binary Search Tree
├── b tree/              # B-Tree
├── kd tree/             # K-D Tree
├── scapegoat tree/      # Scapegoat Tree
├── skip list/           # Skip List
├── cluster/             # K-Means Clustering
└── README.md            # This file
```

---

## 📚 License

This code is provided for academic and personal learning use only. Please cite if reused in other projects or teaching material.

---

**Course:** Advanced Data Structures  
