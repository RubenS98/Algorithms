//Ruben Sanchez A01021759
//Cristopher Cejudo A01025468
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
using namespace std;

int main(){
    string clauses, mStr="", vStr="", temp, variables;
    int cont=0, m, vNum, value,cont2=6, cont3=0, k, varPosition, result;
    vector<int> clausesI;
    vector<int> varValues;
    bool kSatTrue=true, clauseBool=false, tempBool;
    ifstream inFile("DatosKSat.txt");

    if (!inFile) {
        cerr << "Unable to open file datafile.txt";
        return 1;
    }
    getline(inFile,clauses);

    while(clauses[cont2]!=' '){
        vStr=vStr+clauses[cont2];
        cont2++;
    }
    stringstream firstN(vStr);
    firstN>>vNum;
    cont2++;
    while(cont2<clauses.size()){
        mStr=mStr+clauses[cont2];
        cont2++;
    }
    stringstream secondN(mStr);
    secondN>>m;

    getline(inFile,clauses);
    stringstream spacedNumbers;
    spacedNumbers<<clauses;
    while (!spacedNumbers.eof()) {
        spacedNumbers >> temp;

        if (stringstream(temp) >> result){
            clausesI.push_back(result);
        }
        temp = "";
    }
    k=clausesI.size();

    for(int i=0; i<(k*m-k); i++){
        inFile>>value;
        clausesI.push_back(value);
    }
    inFile.close();
    ifstream file("DatosKSat.txt");
    for(int i=0; i<(m+1); i++){
        getline(file,clauses);
    }
    getline(file,clauses);
    varValues.push_back(1);
    for(int i=0; i<vNum; i++){
        varValues.push_back(clauses[i]-'0');
    }
    cout<<"Solution of K-SAT"<<endl;
    for(int i=0; i<m;i++){
        cout<<"It "<<i+1<<": "<<endl;
        for(int j=0; j<k;j++){
            varPosition=clausesI[cont3];
            cout<<varPosition<<" ";
            if(varPosition>0){
                clauseBool=(clauseBool) || varValues[varPosition];
                cout<<varValues[varPosition]<<", ";
            }
            else{
                clauseBool=(clauseBool) || !varValues[-varPosition];
                cout<<!varValues[-varPosition]<<", ";
            }
            cont3++;
        }
        cout<<endl;
        cout<<"Result"<<": "<<clauseBool<<endl;
        if(!clauseBool){
            kSatTrue=false;
            break;
        }
        clauseBool=false;
    }

    if(kSatTrue){
        cout<<endl<<"Los valores de las variables satisfacen a las clausulas.";
    }
    else{
        cout<<"Los valores de las variables no satisfacen a las clausulas.";
    }

    return 0;
}
