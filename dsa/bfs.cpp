#include <iostream>
#include <queue> 
using namespace std;

struct Node {
    int data;   
    Node* next; 
};

void addEdge(Node** adj, int u, int v) {
    Node* newNodeV = new Node; 
    newNodeV->data = v;
    newNodeV->next = adj[u];   
    adj[u] = newNodeV;

    Node* newNodeU = new Node; 
    newNodeU->data = u;
    newNodeU->next = adj[v];   
    adj[v] = newNodeU;        
}

void bfs(int startNode, int numNodes, Node** adj) {
    bool* visited = new bool[numNodes]; 
    for (int i = 0; i < numNodes; ++i) {
        visited[i] = false;
    }

    queue<int> q;

    visited[startNode] = true; 
    q.push(startNode);         
    cout << "BFS starting from node " << startNode << ": ";

    while (!q.empty()) {
        int currentNode = q.front();
        q.pop(); 
        cout << currentNode << " ";

        Node* temp = adj[currentNode];
        while (temp != nullptr) {     
            int neighbor = temp->data; 

            if (!visited[neighbor]) {
                visited[neighbor] = true; 
                q.push(neighbor);
            }
            temp = temp->next; 
        }
    }
    cout << endl;
    delete[] visited;
}

int main() {
    int numNodes = 7; 
    Node** adjList = new Node*[numNodes];

    for (int i = 0; i < numNodes; ++i) {
        adjList[i] = nullptr;
    }

    addEdge(adjList, 0, 1);
    addEdge(adjList, 0, 2);
    addEdge(adjList, 1, 3);
    addEdge(adjList, 1, 4);
    addEdge(adjList, 2, 5);
    addEdge(adjList, 2, 6);

    bfs(0, numNodes, adjList);
    delete[] adjList;

    return 0;
}