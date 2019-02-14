
//***************************************************************
//                   HEADER FILE USED IN PROJECT
//****************************************************************


#include<fstream.h>
#include<ctype.h>
#include<iomanip.h>
#include<conio.h>
#include<stdio.h>
#include<dos.h>
#include<iostream.h>
#include<process.h>
#include<string.h>



void passwordcheck();
		// function to check password
void line(int n=78);

class account
{
	int acno;
	char name[50];
	float deposit;
	char type;
public:
	void create_account();	//function to get data from user
	void show_account();	//function to show data on screen
	void modify();   //function to get new data from user
	void dep(float);	//function to accept amount and add to balance amount
	void draw(float);	//function to accept amount and subtract from balance amount
	void report();	//function to show data in tabular format
	int retacno();	//function to return account number
	float retdeposit();	//function to return balance amount
	char rettype();	//function to return type of account
};         //class ends here

void account::create_account()
{
	cout<<"\nEnter The account No. :";
	cin>>acno;
	cout<<"\n\nEnter The Name of The account Holder : ";
	gets(name);
	cout<<"\nEnter Type of The account (Current-C Saving-S) : ";
	cin>>type;
	type=toupper(type);
	cout<<"\nEnter The Initial amount(>=500 for Saving and >=1000 for current ) : ";
	cin>>deposit;
	cout<<"\n\n\nAccount Created..";
}

void account::show_account()
{
	cout<<"\nAccount No. : "<<acno;
	cout<<"\nAccount Holder Name : ";
	cout<<name;
	cout<<"\nType of Account : ";
	if(type=='S') cout<<"Saving";
	else if(type=='C')cout<<"Current";
	cout<<"\nBalance amount : "<<deposit;
}


void account::modify()
{
	cout<<"\nThe account No."<<acno;
	cout<<"\n\nEnter The Name of The account Holder : ";
	gets(name);
	cout<<"\nEnter Type of The account Current/Saving(C/S) : ";
	cin>>type;
	type=toupper(type);
	//cout<<"\nEnter The amount : ";
	//cin>>deposit;
}



void account::dep(float x)
{
	deposit+=x;
}

void account::draw(float x)
{
	deposit-=x;
}

void account::report()
{
	cout<<acno<<setw(10)<<" "<<name<<setw(10)<<" "<<type<<setw(6)<<deposit<<endl;
}

int account::retacno()
{
	return acno;
}

float account::retdeposit()
{
	return deposit;
}

char account::rettype()
{
	return type;
}


//***************************************************************
//    	function declaration
//****************************************************************
void write_account();	//function to write record in binary file
void display_sp(int);	//function to display account details given by user
void modify_account(int);	//function to modify record of file
void delete_account(int);	//function to delete record of file
void display_all();		//function to display all account details
void deposit_withdraw(int, int); // function to desposit/withdraw amount for given account
void intro();	//introductory screen function

//***************************************************************
//    	THE MAIN FUNCTION OF PROGRAM
//****************************************************************
int main()
{
	char ch;
	int num;
	clrscr();
	passwordcheck();
	line();
	cout<<"\n\n****************:A A A A A A A A A A A A A A A A :***************\n\n";
			 line();
			 line();
	do
	{
		clrscr();
		cout<<"\n\n\n\tMAIN MENU";
		cout<<"\n\n\t01. NEW ACCOUNT";
		cout<<"\n\n\t02. DEPOSIT AMOUNT";
		cout<<"\n\n\t03. WITHDRAW AMOUNT";
		cout<<"\n\n\t04. BALANCE ENQUIRY";
		cout<<"\n\n\t05. ALL ACCOUNT HOLDER LIST";
		cout<<"\n\n\t06. CLOSE AN ACCOUNT";
		cout<<"\n\n\t07. MODIFY AN ACCOUNT";
		cout<<"\n\n\t08. EXIT";
		cout<<"\n\n\tSelect Your Option (1-8) ";
		cin>>ch;
		clrscr();
		switch(ch)
		{
		case '1':
			write_account();
			break;
		case '2':
			cout<<"\n\n\tEnter The account No. : "; cin>>num;
			deposit_withdraw(num, 1);
			break;
		case '3':
			cout<<"\n\n\tEnter The account No. : "; cin>>num;
			deposit_withdraw(num, 2);
			break;
		case '4':
			cout<<"\n\n\tEnter The account No. : "; cin>>num;
			display_sp(num);
			break;
		case '5':
			display_all();
			break;
		case '6':
			cout<<"\n\n\tEnter The account No. : "; cin>>num;
			delete_account(num);
			break;
		 case '7':
			cout<<"\n\n\tEnter The account No. : "; cin>>num;
			modify_account(num);
			break;
		 case '8':
			cout<<"\n\n\tThanks for using bank managemnt system";
			break;
		 default :cout<<"\a";
		}
		getch();
		}while(ch!='8');
	return 0;
}


//***************************************************************
//    	function to write in file
//****************************************************************

void write_account()
{
	account ac;
	ofstream outFile;
	outFile.open("utk.dat",ios::binary|ios::app);
	ac.create_account();
	outFile.write((char *) &ac, sizeof(account));
	outFile.close();
}

//***************************************************************
//    	function to read specific record from file
//****************************************************************

void display_sp(int n)
{
	account ac;
	int flag=0;
	ifstream inFile;
		inFile.open("utk.dat",ios::binary);
	if(!inFile)
	{
		cout<<"File could not be opend !! Press any Key...";
		return;
	}
	cout<<"\nBALANCE DETAILS\n";
		while(inFile.read((char *) &ac, sizeof(account)))
	{
		if(ac.retacno()==n)
		{
			ac.show_account();
			flag=1;
		}
	}
		inFile.close();
	if(flag==0)
		cout<<"\n\nAccount number does not exist";
}


//***************************************************************
//    	function to modify record of file
//****************************************************************

void modify_account(int n)
{
	int found=0;
	account ac;
	fstream File;
		File.open("utk.dat",ios::binary|ios::in|ios::out);
	if(!File)
	{
		cout<<"File could not be open !! Press any Key...";
		return;
	}
		while(File.read((char *) &ac, sizeof(account)) && found==0)
	{
		if(ac.retacno()==n)
		{
			ac.show_account();
			cout<<"\n\nEnter The New Details of account...."<<endl;
			ac.modify();
			int pos=(-1)*sizeof(account);
			File.seekp(pos,ios::cur);
				File.write((char *) &ac, sizeof(account));
				cout<<"\n\n\t Record Updated....";
				found=1;
			}
	}
	File.close();
	if(found==0)
		cout<<"\n\n Sorry!  Record Not Found ....";
}

//***************************************************************
//    	function to delete record of file
//****************************************************************


void delete_account(int n)
{
	int status=0;
	account ac;
	ifstream inFile;
	ofstream outFile;
	inFile.open("utk.dat",ios::binary);
	if(!inFile)
	{
		cout<<"File could not be open !! Press any Key...";
		return;
	}
	outFile.open("Temp.dat",ios::binary);
	inFile.seekg(0,ios::beg);
	while(inFile.read((char *) &ac, sizeof(account)))
	{
		if(ac.retacno()!=n)
		{
			outFile.write((char *) &ac, sizeof(account));
			status=1;break;
		}
	}
	inFile.close();
	outFile.close();
	remove("utk.dat");
	rename("Temp.dat","utk.dat");
	if(status==1)
	cout<<"\n\n\tRecord Deleted ...";
	else
	cout<<"\n\nSorry Record Not Found....";
}

//***************************************************************
//    	function to display all accounts deposit list
//****************************************************************

void display_all()
{
	account ac;
	ifstream inFile;
	inFile.open("utk.dat",ios::binary);
	if(!inFile)
	{
		cout<<"File could not be opend !! Press any Key...";
		return;
	}
	cout<<"\n\n\t\tACCOUNT HOLDER LIST\n\n";
	cout<<"====================================================\n";
	cout<<"A/c no.      NAME           Type  Balance\n";
	cout<<"====================================================\n";
	while(inFile.read((char *) &ac, sizeof(account)))
	{
		ac.report();
	}
	inFile.close();
}

//***************************************************************
//    	function to deposit and withdraw amounts
//****************************************************************

void deposit_withdraw(int n, int option)
{
	float amt;
	int found=0;
	account ac;
	fstream File;
		File.open("utk.dat", ios::binary|ios::in|ios::out);
	int cnt=0;
	if(!File)
	{
		cout<<"File could not be open !! Press any Key...";
		return;
	}
		while(File.read((char *) &ac, sizeof(account)) && found==0)
	{
		cnt++;
		if(ac.retacno()==n)
		{
			found=1;
			ac.show_account();
			if(option==1)
			{
				cout<<"\n\n\tTO DEPOSITE AMOUNT ";
				cout<<"\n\nEnter The amount to be deposited: ";
				cin>>amt;
				ac.dep(amt);
			}
				if(option==2)
			{
				cout<<"\n\n\tTO WITHDRAW AMOUNT ";
				cout<<"\n\nEnter The amount to be withdraw: ";
				cin>>amt;
				float bal=ac.retdeposit()-amt;
				if((bal<500 && ac.rettype()=='S') || (bal<1000 && ac.rettype()=='C'))
					cout<<"Insufficience balance...";
				else
					ac.draw(amt);
					}
			int pos=(cnt-1)* sizeof(ac);
			File.seekp(pos);
			File.write((char *) &ac, sizeof(account));
			cout<<"\n\n\t Record Updated";
			}
	 }
		File.close();
	if(found==0)
		cout<<"\n\n Record Not Found ";
}
void line(int n)
	{
		for(int i=0;i<n;i++)
			{
			cout<<"Ä";
			delay(4);
			}
	}// end of print line function
 //----------------------------------------------------------------
void passwordcheck()
{
char ch;
int i,cnt=0;;
char pass[7];
char pass1[]="12345";
while(cnt<3)
	{
		cout<<"\n\tEnter the maximum 8 character access password :\t";
		i=0;
		while(ch=getch())
				{
				if(ch==13) break;
				pass[i]=ch;
				i++;
				putchar('*');
				}
	 pass[i]='\0';
		if(strcmp(pass,pass1)==0)
			{
			cout<<endl;
			line();
			cout<<"\n\n\tPassword verified........\n";
			line();
			getch();
			break;
			}
		 else
			{
			line();
			cout<<"\n\n\tInvalid password! try again\n";
			getch();
			}
	cnt++;
		if(cnt==3)
			{
			cout<<"\n\n\n \t\t\tCan't continue.....";
			getch();
			exit(1);
			}
		}
clrscr();
}//end of password check function()





//***************************************************************
//    			END OF PROJECT
//***************************************************************