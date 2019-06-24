//Ruben Sanchez A01021759
//Cristopher Cejudo A01025468
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
using namespace std;

class Vertex{
    public:
    int number;
    map <int, Vertex> neighbours;
    bool visited=false;
};
//1 (1,2) (1,3) (1,4) (2,3) (2,5) (2,6) (3,7) (3,8) (4,8) (7,9)
//10 (10,20) (10,30) (10,40) (20,30) (30,50)
int main(){
    int head=0;
    int cont=0;
    int it=1;
    int cont2=0;
    int first;
    int second;
    int sizeA;
    string graph="";
    string subGraph1="";
    string subGraph2="";
    map <int, Vertex> vertices;
    queue <Vertex> cola;
    queue <Vertex> colaT;

    cout << "Input the data. In one line, first input the number of the first node that will be visited and then ";
    cout<<endl;
    cout << "input the pairs of numbers that represent the links between nodes.";
    cout<<endl;
    cout << "Example: 1 (1,2) (1,3) (1,4) (2,3) (2,5) (2,6) (3,7) (3,8) (4,8) (7,9)";
    cout<<endl;
    cin >> head;

    getline(cin,graph);

    cout<<endl;

    for(int i=0; i<graph.size(); i++){
        if(graph[i]=='('){
            Vertex vertice;
            cont2=i+1;
            while(graph[cont2]!=','){
                subGraph1=subGraph1+graph[cont2];
                cont2++;
            }
            //cout<<subGraph1<<" ";
            stringstream firstN(subGraph1);
            firstN>>first;
            if(vertices.count(first)==0){
                vertice.number=first;
                vertices[first]=vertice;
            }
            cont2=cont2+1;
            while(graph[cont2]!=')'){
                subGraph2=subGraph2+graph[cont2];
                cont2++;
            }
            //cout<<subGraph2<<" ";
            stringstream secondN(subGraph2);
            secondN>>second;
            if(vertices.count(second)==0){
                vertice.number=second;
                vertices[second]=vertice;
            }
            vertices[first].neighbours[second]=vertices[second];
            vertices[second].neighbours[first]=vertices[first];

            subGraph1="";
            subGraph2="";
        }
    }

    cout<<endl;
    //cout<<vertices.size();
    sizeA=vertices.size();

    int arreglo[vertices.size()];

    for(int i=0; i<vertices.size(); i++){
        arreglo[i]=0;
    }

    for(int i=1; i<vertices.size()+1; i++){
        if(vertices[i].number==head){
            cola.push(vertices[i]);
            arreglo[cont]=vertices[i].number;
            vertices[i].visited=true;
            cont++;
        }
    }
    cout<<"Iteration 0\t";
    cout<<"Queue: ["<<cola.front().number<<"]\t";
    cout<<"Array: ["<<arreglo[0]<<"]";
    cout<<endl;

    while(cola.empty()==false){
        Vertex verticeC;
        verticeC=cola.front();
        cola.pop();
        for(int j=1; j<verticeC.neighbours.size()+1; j++){
            if(verticeC.neighbours[j].number!=0){
                if(!vertices[verticeC.neighbours[j].number].visited){
                    cola.push(vertices[verticeC.neighbours[j].number]);
                    arreglo[cont]=verticeC.neighbours[j].number;
                    cont++;
                    vertices[verticeC.neighbours[j].number].visited=true;
                }
            }
        }
        colaT=cola;
        cout<<"Iteration "<<it<<"\t";
        cout<<"Queue: [";
        while (!cola.empty()) {
            cout << cola.front().number<<", ";
            cola.pop();
        }
        cola=colaT;
        cout<<"]\t";
        cout<<"Array: [";
        for(int k=0; k<sizeA; k++){
            cout<<(arreglo[k])<<", ";
        }
        cout<<"]\t";
        cout<<endl;
        it++;
    }

    return 0;
}
