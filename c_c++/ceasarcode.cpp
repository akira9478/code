// ceasarcode.cpp : ��`��T���p�����I�i���y�B
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	string str;
	cout << "�A����������s�\�L��i(��i�p_�֑�):";
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

