// ceasarcode.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	string str;
	cout << "輸入一串字且不能有空格(空格可用_替代):";
	cin >> str;
	int count =str.size();
	int j=0;
	while(j<26){
		cout << j << "\t" ;
	for(int i=0;i<count;i++){
		int ch = str[i];
		if(ch>=97 && ch<=122){
			if(ch+j>122) cout << char(ch+j-26);
			else cout << char(ch+j);
		}			
		else{
			cout << char(ch);
			continue;
		}
	}
	cout << endl;
	j++;
	}

	system("pause");

}

