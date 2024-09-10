package sid;

import java.util.Scanner;

public class Demo {
	public static void main(String[] args) {
	Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		int []ar=new int[n];
		for(int i=0;i<ar.length;i++)
		{
			ar[i]=scan.nextInt();
		}
		for(int i=0;i<ar.length;i++)
		{
			for(int j=i+1;j<ar.length;j++)
			{
				if(ar[j]>ar[i])
				{
				int temp=ar[i];
				ar[i]=ar[j];
				ar[j]=temp;
				}
			}
		}
		for(int i=0;i<ar.length;i++)
		{
			System.out.print(ar[i]+" ");
		}
		
	} 
}
